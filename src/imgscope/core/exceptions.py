"""Custom exceptions for clear error reporting."""


class ImgscopeError(Exception):
    """Base class for all imgscope errors."""


class InvalidFormatError(ImgscopeError):
    """Raised when a file's signature or structure doesn't match the format."""


class UnsupportedFeatureError(ImgscopeError):
    """Raised when a valid file uses a feature the decoder doesn't handle yet."""
