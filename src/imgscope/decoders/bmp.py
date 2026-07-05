"""BMP decoder.

Decodes uncompressed 24-bit BMP files from raw bytes.
Handles the classic 3-part BMP layout: File header, DIB header, pixel array.

Not yet handled (TODO): row padding for widths not divisible by 4,
bottom-up row order correction, bit depths other than 24.
"""

import struct

from imgscope.core.exceptions import InvalidFormatError, UnsupportedFeatureError
from imgscope.core.image import DecodedImage


def decode(path: str) -> DecodedImage:
    """Decode a 24-bit BMP file into a DecodedImage.

    Args:
        path: filesystem path to the .bmp file

    Returns:
        DecodedImage with RGB pixels and header metadata

    Raises:
        InvalidFormatError: if signature is not 'BM'
        UnsupportedFeatureError: if bit depth is not 24
    """
    with open(path, "rb") as f:
        file_header = f.read(14)
        dib_header = f.read(40)

    # --- File header (14 bytes, little-endian) ---
    signature, file_size, _r1, _r2, pixel_offset = struct.unpack("<2sIHHI", file_header)
    if signature != b"BM":
        raise InvalidFormatError(f"Not a BMP file (signature: {signature!r})")

    # --- DIB header (40 bytes) ---
    (
        dib_size,
        width,
        height,
        planes,
        bits_per_pixel,
        compression,
        image_size,
        x_ppm,
        y_ppm,
        colors_used,
        important_colors,
    ) = struct.unpack("<IiiHHIIiiII", dib_header)

    if bits_per_pixel != 24:
        raise UnsupportedFeatureError(
            f"Only 24-bit BMP supported (got {bits_per_pixel}-bit)"
        )

    # --- Pixel array ---
    with open(path, "rb") as f:
        f.seek(pixel_offset)
        raw = f.read()

    pixels: list[tuple[int, int, int]] = []
    for i in range(0, width * height * 3, 3):
        b, g, r = raw[i], raw[i + 1], raw[i + 2]
        pixels.append((r, g, b))  # BGR (file) -> RGB (ours)

    metadata = {
        "file_size": file_size,
        "pixel_offset": pixel_offset,
        "dib_size": dib_size,
        "bits_per_pixel": bits_per_pixel,
        "compression": compression,
        "image_size": image_size,
    }

    return DecodedImage(
        width=width,
        height=abs(height),
        pixels=pixels,
        source_format="bmp",
        metadata=metadata,
    )
