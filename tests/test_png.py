"""Tests for the PNG decoder (work in progress)."""

import pytest

from imgscope.decoders import png


def test_png_stub_raises():
    """Until implemented, decode should raise NotImplementedError."""
    with pytest.raises(NotImplementedError):
        png.decode("nonexistent.png")
