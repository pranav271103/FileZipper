"""
Core implementation of Huffman Coding algorithm.
"""
import heapq
import os
from collections import Counter, defaultdict
from typing import Dict, List, Optional, Tuple, Union

class HuffmanNode:
    """Node class for Huffman Tree construction.
    
    Attributes:
        char: The character represented by this node (None for internal nodes).
        freq: Frequency of the character.
        left: Left child node.
        right: Right child node.
    """
    __slots__ = ['char', 'freq', 'left', 'right']
    
    def __init__(self, 
                 char: Optional[int] = None, 
                 freq: int = 0, 
                 left: Optional['HuffmanNode'] = None, 
                 right: Optional['HuffmanNode'] = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other: 'HuffmanNode') -> bool:
        # For min-heap comparison based on frequency
        return self.freq < other.freq
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HuffmanNode):
            return NotImplemented
        return self.freq == other.freq


class HuffmanEncoder:
    """Huffman encoding implementation."""
    
    def __init__(self):
        self.heap: List[HuffmanNode] = []
        self.codes: Dict[int, str] = {}
        self.reverse_mapping: Dict[str, int] = {}
    
    def _build_frequency_dict(self, data: bytes) -> Dict[int, int]:
        """Build frequency dictionary from input data.
        
        Args:
            data: Input data as bytes.
            
        Returns:
            Dictionary mapping each byte to its frequency.
        """
        return Counter(data)
    
    def _build_min_heap(self, frequency: Dict[int, int]) -> None:
        """Build a min-heap from frequency dictionary."""
        self.heap = []
        for char, freq in frequency.items():
            node = HuffmanNode(char=char, freq=freq)
            heapq.heappush(self.heap, node)
    
    def _merge_nodes(self) -> None:
        """Merge nodes to build Huffman tree."""
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            
            merged = HuffmanNode(
                freq=node1.freq + node2.freq,
                left=node1,
                right=node2
            )
            heapq.heappush(self.heap, merged)
    
    def _build_codes_helper(self, node: Optional[HuffmanNode], current_code: str) -> None:
        """Helper function to build Huffman codes recursively."""
        if node is None:
            return
        
        if node.char is not None:
            if not current_code:  # Handle single character case
                current_code = "0"
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char
            return
        
        self._build_codes_helper(node.left, current_code + "0")
        self._build_codes_helper(node.right, current_code + "1")
    
    def _build_codes(self) -> None:
        """Build Huffman codes from the Huffman tree."""
        self.codes = {}
        self.reverse_mapping = {}
        
        if not self.heap:
            return
            
        root = self.heap[0]
        if root.char is not None:  # Single character case
            self.codes[root.char] = "0"
            self.reverse_mapping["0"] = root.char
        else:
            self._build_codes_helper(root, "")
    
    def _get_encoded_data(self, data: bytes) -> str:
        """Encode input data using Huffman codes."""
        return ''.join(self.codes[byte] for byte in data)
    
    def _pad_encoded_data(self, encoded_data: str) -> str:
        """Pad encoded data to make it byte-aligned."""
        padding = 8 - len(encoded_data) % 8
        if padding != 8:  # Only pad if needed
            encoded_data += '0' * padding
        return encoded_data, padding
    
    def _get_byte_array(self, padded_encoded_data: str) -> bytearray:
        """Convert padded encoded data to bytearray."""
        if len(padded_encoded_data) % 8 != 0:
            raise ValueError("Encoded data is not properly padded")
            
        b = bytearray()
        for i in range(0, len(padded_encoded_data), 8):
            byte = padded_encoded_data[i:i+8]
            b.append(int(byte, 2))
        return b
    
    def compress(self, data: bytes) -> Tuple[bytes, Dict[int, str]]:
        """Compress input data using Huffman coding.
        
        Args:
            data: Input data as bytes.
            
        Returns:
            Tuple of (compressed_data, codes) where:
            - compressed_data: Compressed data as bytes
            - codes: Dictionary mapping bytes to their Huffman codes
        """
        if not data:
            return b'', {}
            
        frequency = self._build_frequency_dict(data)
        self._build_min_heap(frequency)
        self._merge_nodes()
        self._build_codes()
        
        encoded_data = self._get_encoded_data(data)
        padded_encoded_data, padding = self._pad_encoded_data(encoded_data)
        compressed_data = self._get_byte_array(padded_encoded_data)
        
        # Include padding info in the compressed data
        compressed_data_with_meta = bytearray()
        compressed_data_with_meta.append(padding)
        compressed_data_with_meta.extend(compressed_data)
        
        return bytes(compressed_data_with_meta), self.codes


class HuffmanDecoder:
    """Huffman decoding implementation."""
    
    def __init__(self):
        self.reverse_mapping: Dict[str, int] = {}
    
    def _remove_padding(self, padded_encoded_data: str, padding: int) -> str:
        """Remove padding from encoded data."""
        if padding > 0:
            return padded_encoded_data[:-padding]
        return padded_encoded_data
    
    def _decode_data(self, encoded_data: str) -> bytes:
        """Decode data using Huffman codes."""
        current_code = ""
        decoded_data = bytearray()
        
        for bit in encoded_data:
            current_code += bit
            if current_code in self.reverse_mapping:
                byte = self.reverse_mapping[current_code]
                decoded_data.append(byte)
                current_code = ""
        
        if current_code:  # In case of incomplete code at the end
            raise ValueError("Invalid encoded data: incomplete code at the end")
            
        return bytes(decoded_data)
    
    def decompress(self, compressed_data: bytes, codes: Dict[int, str]) -> bytes:
        """Decompress data using Huffman coding.
        
        Args:
            compressed_data: Compressed data as bytes.
            codes: Dictionary mapping bytes to their Huffman codes.
            
        Returns:
            Decompressed data as bytes.
        """
        if not compressed_data:
            return b""
            
        self.reverse_mapping = {v: k for k, v in codes.items()}
        
        # Convert compressed data to bit string
        bit_string = ""
        for byte in compressed_data:
            bit_string += f"{byte:08b}"
        
        # Remove padding
        padding = int(bit_string[:8], 2)
        encoded_data = self._remove_padding(bit_string[8:], padding)
        
        # Decode data
        return self._decode_data(encoded_data)
