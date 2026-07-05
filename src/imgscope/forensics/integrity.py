"""Integrity checks — the first forensic feature.

Compares what a file *claims* about itself (header fields) against what it
*actually* contains on disk. Mismatches reveal tampering, appended data,
or corruption that normal viewers silently ignore.

Work in progress.
"""
