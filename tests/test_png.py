"""Tests for the PNG decoder (work in progress)."""

from pathlib import Path
from imgscope.decoders import png

FIXTURES = Path(__file__).parent / "fixtures"


def test_decode_solid_red_4x4():
    """A 4x4 solid red PNG should decode to 16 red pixels."""
    img = png.decode(str(FIXTURES / "red_4x4.png"))
    assert img.width == 4
    assert img.height == 4
    assert img.source_format == "png"
    assert len(img.pixels) == 16
    assert all(p == (255, 0, 0) for p in img.pixels)
