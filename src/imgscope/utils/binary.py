"""Binary reading helpers.

These wrap struct.unpack for the common cases so decoders read cleanly.
Byte order matters: BMP is little-endian, PNG/GIF/JPEG are big-endian.
"""

import struct


def read_uint16_le(data: bytes, offset: int = 0) -> int:
    """Read a 2-byte unsigned int, little-endian (BMP)."""
    return struct.unpack_from("<H", data, offset)[0]


def read_uint32_le(data: bytes, offset: int = 0) -> int:
    """Read a 4-byte unsigned int, little-endian (BMP)."""
    return struct.unpack_from("<I", data, offset)[0]


def read_uint16_be(data: bytes, offset: int = 0) -> int:
    """Read a 2-byte unsigned int, big-endian (PNG/GIF/JPEG)."""
    return struct.unpack_from(">H", data, offset)[0]


def read_uint32_be(data: bytes, offset: int = 0) -> int:
    """Read a 4-byte unsigned int, big-endian (PNG/GIF/JPEG)."""
    return struct.unpack_from(">I", data, offset)[0]
