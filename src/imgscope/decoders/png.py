"""PNG decoder.

Decodes PNG files from raw bytes. PNG structure differs from BMP:
  - 8-byte signature
  - big-endian byte order (unlike BMP's little-endian)
  - data split into chunks (length + type + data + CRC)
  - pixels compressed with DEFLATE (via zlib) and pre-filtered per row

Work in progress — we build this step by step.
"""

import zlib

from imgscope.core.exceptions import InvalidFormatError
from imgscope.core.exceptions import UnsupportedFeatureError
from imgscope.core.image import DecodedImage
from imgscope.utils.binary import read_uint32_be

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def decode(path: str) -> DecodedImage:
    """Decode a PNG file into a DecodedImage.

    Currently a stub — implemented incrementally.
    """
    with open(path, "rb") as f:
        signature = f.read(8)

        if signature != PNG_SIGNATURE:
            raise InvalidFormatError("Wrong format")

        idat_data = b""

        while True:
            length_bytes = f.read(4)
            if len(length_bytes) < 4:
                break
            length = read_uint32_be(length_bytes)
            chunk_type = f.read(4)
            data = f.read(length)
            crc = f.read(4)

            if chunk_type == b"IHDR":
                width = read_uint32_be(data, 0)
                height = read_uint32_be(data, 4)
                bit_depth = data[8]
                color_type = data[9]
            elif chunk_type == b"IDAT":
                idat_data += data
            elif chunk_type == b"IEND":
                break

        raw = zlib.decompress(idat_data)

        bpp = 3
        stride = width * bpp

        recon = []

        for row in range(height):
            filter_type = raw[row * (1 + stride)]
            row_start = row * (1 + stride) + 1

            current_row = []
            for i in range(stride):
                x = raw[row_start + i]

                a = current_row[i - bpp] if i >= bpp else 0
                b = recon[row - 1][i] if row > 0 else 0

                if filter_type == 0:
                    value = x
                elif filter_type == 1:
                    value = (x + a) % 256
                elif filter_type == 2:
                    value = (x + b) % 256
                else:
                    raise UnsupportedFeatureError(
                        f"Filter type {filter_type} not supported"
                    )

                current_row.append(value)

            recon.append(current_row)

        pixels = []
        for row in recon:
            for i in range(0, len(row), 3):
                r, g, b = row[i], row[i + 1], row[i + 2]
                pixels.append((r, g, b))

    meta_data = {
        "bit_depth": bit_depth,
        "color_type": color_type,
        "compressed_size": len(idat_data),
    }

    return DecodedImage(
        width=width,
        height=height,
        pixels=pixels,
        source_format="png",
        metadata=meta_data,
    )
