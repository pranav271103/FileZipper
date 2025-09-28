import os
import tempfile
import pytest
from huffman.core import HuffmanEncoder, HuffmanDecoder

def test_huffman_encoding_decoding():
    """Test that encoding and then decoding returns the original data."""
    # Test data
    test_data = b"this is a test string for huffman encoding"
    
    # Encode the data
    encoder = HuffmanEncoder()
    compressed_data, codes = encoder.compress(test_data)
    
    # Decode the data
    decoder = HuffmanDecoder()
    decompressed_data = decoder.decompress(compressed_data, codes)
    
    # Verify the decompressed data matches the original
    assert decompressed_data == test_data

def test_huffman_with_empty_data():
    """Test with empty input data."""
    encoder = HuffmanEncoder()
    compressed_data, codes = encoder.compress(b"")
    
    decoder = HuffmanDecoder()
    decompressed_data = decoder.decompress(compressed_data, codes)
    
    assert decompressed_data == b""

def test_huffman_with_single_character():
    """Test with a single repeated character."""
    test_data = b"aaaaaaaaaa"
    
    encoder = HuffmanEncoder()
    compressed_data, codes = encoder.compress(test_data)
    
    decoder = HuffmanDecoder()
    decompressed_data = decoder.decompress(compressed_data, codes)
    
    assert decompressed_data == test_data

def test_huffman_with_large_data():
    """Test with larger input data."""
    test_data = b"a" * 1000 + b"b" * 500 + b"c" * 250 + b"d" * 125
    
    encoder = HuffmanEncoder()
    compressed_data, codes = encoder.compress(test_data)
    
    decoder = HuffmanDecoder()
    decompressed_data = decoder.decompress(compressed_data, codes)
    
    assert decompressed_data == test_data

def test_huffman_compression_ratio():
    """Test that compression actually reduces size for repetitive data."""
    test_data = b"a" * 1000 + b"b" * 500 + b"c" * 250 + b"d" * 125
    
    encoder = HuffmanEncoder()
    compressed_data, _ = encoder.compress(test_data)
    
    # For this specific pattern, we expect some compression
    assert len(compressed_data) < len(test_data)

if __name__ == "__main__":
    pytest.main([__file__])
