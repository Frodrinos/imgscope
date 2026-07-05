"""Shared data types for decoded images.

Every decoder, regardless of format, produces a DecodedImage. This lets the
rest of the toolkit (forensics, CLI, future GUI) work with any format uniformly.
"""

from dataclasses import dataclass, field


@dataclass
class DecodedImage:
    """A fully decoded image, format-agnostic.

    Attributes:
        width: image width in pixels
        height: image height in pixels
        pixels: list of (R, G, B) tuples, row-major, top-to-bottom
        source_format: which decoder produced this ("bmp", "png", ...)
        metadata: format-specific extra info (header fields, EXIF, etc.)
    """

    width: int
    height: int
    pixels: list[tuple[int, int, int]]
    source_format: str
    metadata: dict = field(default_factory=dict)

    def pixel_at(self, x: int, y: int) -> tuple[int, int, int]:
        """Return the (R, G, B) pixel at column x, row y."""
        return self.pixels[y * self.width + x]
