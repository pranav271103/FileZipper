"""
FileZipper - A Python implementation of file compression using Huffman Coding.

This package provides utilities for compressing and decompressing files using the
Huffman coding algorithm. It includes both a command-line interface and a Python API.
"""

from .core import HuffmanNode, HuffmanEncoder, HuffmanDecoder
from .cli import HuffmanZipperCLI

__version__ = "0.1.0"
__author__ = "Pranav Singh"

__all__ = [
    'HuffmanNode',
    'HuffmanEncoder',
    'HuffmanDecoder',
    'HuffmanZipperCLI'
]
