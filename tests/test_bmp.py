"""Tests for the BMP decoder."""

from pathlib import Path

from imgscope.decoders import bmp

FIXTURES = Path(__file__).parent / "fixtures"


def test_decode_solid_red_4x4():
    """A 4x4 solid red BMP should decode to 16 red pixels."""
    img = bmp.decode(str(FIXTURES / "red_4x4.bmp"))

    assert img.width == 4
    assert img.height == 4
    assert img.source_format == "bmp"
    assert len(img.pixels) == 16
    assert all(p == (255, 0, 0) for p in img.pixels)


def test_metadata_present():
    """Decoded image should carry header metadata."""
    img = bmp.decode(str(FIXTURES / "red_4x4.bmp"))

    assert img.metadata["bits_per_pixel"] == 24
    assert img.metadata["compression"] == 0
    assert img.metadata["pixel_offset"] == 54
