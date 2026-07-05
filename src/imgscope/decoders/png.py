"""PNG decoder.

Decodes PNG files from raw bytes. PNG structure differs from BMP:
  - 8-byte signature
  - big-endian byte order (unlike BMP's little-endian)
  - data split into chunks (length + type + data + CRC)
  - pixels compressed with DEFLATE (via zlib) and pre-filtered per row

Work in progress — we build this step by step.
"""

from imgscope.core.exceptions import InvalidFormatError
from imgscope.core.image import DecodedImage

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def decode(path: str) -> DecodedImage:
    """Decode a PNG file into a DecodedImage.

    Currently a stub — implemented incrementally.
    """
    raise NotImplementedError("PNG decoder is under construction")
