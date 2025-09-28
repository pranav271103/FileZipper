"""
Command Line Interface for Huffman File Zipper.
"""
import os
import pickle
import sys
import argparse
from pathlib import Path
from typing import Dict, Optional, Tuple, Any

from huffman.core import HuffmanEncoder, HuffmanDecoder
from utils.file_utils import (
    get_file_size, 
    get_compression_stats, 
    get_output_path,
    format_bytes,
    format_time,
    Timer
)


class HuffmanZipperCLI:
    """Command line interface for Huffman File Zipper."""
    
    def __init__(self):
        self.encoder = HuffmanEncoder()
        self.decoder = HuffmanDecoder()
    
    def _read_file(self, file_path: str) -> bytes:
        """Read file content as bytes."""
        with open(file_path, 'rb') as f:
            return f.read()
    
    def _write_file(self, file_path: str, data: bytes) -> None:
        """Write bytes to file."""
        with open(file_path, 'wb') as f:
            f.write(data)
    
    def _save_compressed_data(
        self, 
        output_path: str, 
        compressed_data: bytes, 
        codes: Dict[int, str],
        original_size: int
    ) -> None:
        """Save compressed data and metadata to file."""
        # Create metadata dictionary
        metadata = {
            'codes': codes,
            'original_size': original_size,
            'compressed_size': len(compressed_data)
        }
        
        # Convert metadata to bytes
        metadata_bytes = pickle.dumps(metadata)
        metadata_length = len(metadata_bytes).to_bytes(4, byteorder='big')
        
        # Write to file: [metadata_length][metadata][compressed_data]
        with open(output_path, 'wb') as f:
            f.write(metadata_length)
            f.write(metadata_bytes)
            f.write(compressed_data)
    
    def _load_compressed_file(self, input_path: str) -> Tuple[bytes, Dict[int, str], int]:
        """Load compressed file and extract metadata and compressed data."""
        with open(input_path, 'rb') as f:
            # Read metadata length (first 4 bytes)
            metadata_length = int.from_bytes(f.read(4), byteorder='big')
            
            # Read metadata
            metadata_bytes = f.read(metadata_length)
            metadata = pickle.loads(metadata_bytes)
            
            # Read compressed data
            compressed_data = f.read()
            
            return compressed_data, metadata['codes'], metadata['original_size']
    
    def compress_file(
        self, 
        input_path: str, 
        output_path: Optional[str] = None,
        verbose: bool = True
    ) -> Optional[Dict[str, Any]]:
        """Compress a file using Huffman coding.
        
        Args:
            input_path: Path to input file.
            output_path: Path to output file. If None, will use input_path with .huff extension.
            verbose: Whether to print progress and statistics.
            
        Returns:
            Dictionary containing compression statistics, or None if operation failed.
        """
        try:
            if verbose:
                print(f"Compressing {input_path}...")
            
            # Read input file
            with Timer() as timer:
                data = self._read_file(input_path)
            
            original_size = len(data)
            
            if verbose:
                print(f"  Original size: {format_bytes(original_size)}")
                print(f"  Reading time: {format_time(timer.elapsed)}")
            
            # Compress data
            with Timer() as timer:
                compressed_data, codes = self.encoder.compress(data)
            
            compressed_size = len(compressed_data)
            
            if verbose:
                print(f"  Compression time: {format_time(timer.elapsed)}")
            
            # Generate output path if not provided
            output_path = get_output_path(input_path, output_path, 'huff')
            
            # Save compressed data
            with Timer() as timer:
                self._save_compressed_data(
                    output_path, 
                    compressed_data, 
                    codes,
                    original_size
                )
            
            if verbose:
                print(f"  Writing time: {format_time(timer.elapsed)}")
            
            # Calculate statistics
            stats = get_compression_stats(original_size, os.path.getsize(output_path))
            
            if verbose:
                print(f"\nCompression completed successfully!")
                print(f"  Output file: {output_path}")
                print(f"  Original size: {format_bytes(original_size)}")
                print(f"  Compressed size: {format_bytes(os.path.getsize(output_path))}")
                print(f"  Compression ratio: {stats['compression_ratio']:.2f}:1")
                print(f"  Space saved: {stats['compression_percentage']:.2f}%")
            
            return {
                'input_path': input_path,
                'output_path': output_path,
                'original_size': original_size,
                'compressed_size': os.path.getsize(output_path),
                **stats
            }
            
        except Exception as e:
            print(f"Error compressing file: {e}", file=sys.stderr)
            return None
    
    def decompress_file(
        self, 
        input_path: str, 
        output_path: Optional[str] = None,
        verbose: bool = True
    ) -> Optional[Dict[str, Any]]:
        """Decompress a file using Huffman coding.
        
        Args:
            input_path: Path to input file.
            output_path: Path to output file. If None, will use input_path without .huff extension.
            verbose: Whether to print progress and statistics.
            
        Returns:
            Dictionary containing decompression statistics, or None if operation failed.
        """
        try:
            if verbose:
                print(f"Decompressing {input_path}...")
            
            # Read and parse compressed file
            with Timer() as timer:
                compressed_data, codes, original_size = self._load_compressed_file(input_path)
            
            if verbose:
                print(f"  Reading time: {format_time(timer.elapsed)}")
            
            # Decompress data
            with Timer() as timer:
                decompressed_data = self.decoder.decompress(compressed_data, codes)
            
            decompressed_size = len(decompressed_data)
            
            if verbose:
                print(f"  Decompression time: {format_time(timer.elapsed)}")
            
            # Generate output path if not provided
            if output_path is None:
                input_path_obj = Path(input_path)
                if input_path_obj.suffix == '.huff':
                    output_path = str(input_path_obj.with_suffix(''))
                else:
                    output_path = f"{input_path}.decompressed"
            
            # Save decompressed data
            with Timer() as timer:
                self._write_file(output_path, decompressed_data)
            
            if verbose:
                print(f"  Writing time: {format_time(timer.elapsed)}")
                print(f"\nDecompression completed successfully!")
                print(f"  Output file: {output_path}")
                print(f"  Decompressed size: {format_bytes(decompressed_size)}")
            
            return {
                'input_path': input_path,
                'output_path': output_path,
                'decompressed_size': decompressed_size
            }
            
        except Exception as e:
            print(f"Error decompressing file: {e}", file=sys.stderr)
            return None


def main():
    """Main entry point for the Huffman Zipper CLI."""
    parser = argparse.ArgumentParser(
        description='Huffman File Zipper - Compress and decompress files using Huffman coding',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', required=True, help='Command to execute')
    
    # Compress command
    compress_parser = subparsers.add_parser('compress', help='Compress a file')
    compress_parser.add_argument('input', help='Input file path')
    compress_parser.add_argument('-o', '--output', help='Output file path (optional)')
    compress_parser.add_argument('-q', '--quiet', action='store_true', help='Suppress output')
    
    # Decompress command
    decompress_parser = subparsers.add_parser('decompress', help='Decompress a file')
    decompress_parser.add_argument('input', help='Input file path')
    decompress_parser.add_argument('-o', '--output', help='Output file path (optional)')
    decompress_parser.add_argument('-q', '--quiet', action='store_true', help='Suppress output')
    
    args = parser.parse_args()
    
    cli = HuffmanZipperCLI()
    
    if args.command == 'compress':
        cli.compress_file(
            input_path=args.input,
            output_path=args.output,
            verbose=not args.quiet
        )
    elif args.command == 'decompress':
        cli.decompress_file(
            input_path=args.input,
            output_path=args.output,
            verbose=not args.quiet
        )
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
