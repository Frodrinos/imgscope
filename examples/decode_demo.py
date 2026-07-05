"""Demo: decode a BMP and print basic info.

Run from project root:
    python examples/decode_demo.py
"""

from imgscope.decoders import bmp


def main() -> None:
    img = bmp.decode("tests/fixtures/red_4x4.bmp")
    print(f"Format:  {img.source_format}")
    print(f"Size:    {img.width}x{img.height}")
    print(f"Pixels:  {len(img.pixels)}")
    print(f"First:   {img.pixel_at(0, 0)}")
    print(f"Meta:    {img.metadata}")


if __name__ == "__main__":
    main()
