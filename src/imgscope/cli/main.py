"""Command-line entry point for imgscope.

Usage (once implemented):
    imgscope decode image.png
    imgscope analyze suspicious.jpg
"""

import sys


def main() -> None:
    """CLI entry point. Dispatches to decode/analyze subcommands."""
    if len(sys.argv) < 2:
        print("Usage: imgscope <decode|analyze> <file>")
        sys.exit(1)

    # Command dispatch will go here as features land.
    print("imgscope CLI — under construction")


if __name__ == "__main__":
    main()
