"""
Utility functions for file operations and compression statistics.
"""
import os
import time
from pathlib import Path
from typing import Dict, Tuple, Optional


def get_file_size(file_path: str) -> int:
    """Get file size in bytes."""
    return os.path.getsize(file_path)


def get_compression_stats(original_size: int, compressed_size: int) -> Dict[str, float]:
    """Calculate compression statistics.
    
    Args:
        original_size: Size of original data in bytes.
        compressed_size: Size of compressed data in bytes.
        
    Returns:
        Dictionary containing compression statistics.
    """
    if original_size == 0:
        return {
            'compression_ratio': 0.0,
            'space_saving': 0.0,
            'compression_percentage': 0.0
        }
    
    compression_ratio = original_size / compressed_size
    space_saving = 1 - (compressed_size / original_size)
    compression_percentage = (1 - (compressed_size / original_size)) * 100
    
    return {
        'compression_ratio': compression_ratio,
        'space_saving': space_saving,
        'compression_percentage': compression_percentage
    }


def get_output_path(input_path: str, output_path: Optional[str] = None, 
                  extension: str = 'huff') -> str:
    """Generate output path if not provided.
    
    Args:
        input_path: Path to input file.
        output_path: Optional output path.
        extension: File extension for output file.
        
    Returns:
        Output file path.
    """
    if output_path:
        return output_path
    
    input_path = Path(input_path)
    return str(input_path.parent / f"{input_path.stem}.{extension}")


def format_bytes(size: float) -> str:
    """Format bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"


def format_time(seconds: float) -> str:
    """Format time in seconds to human-readable format."""
    if seconds < 1e-6:
        return f"{seconds * 1e9:.2f} ns"
    elif seconds < 1e-3:
        return f"{seconds * 1e6:.2f} µs"
    elif seconds < 1:
        return f"{seconds * 1000:.2f} ms"
    elif seconds < 60:
        return f"{seconds:.2f} s"
    else:
        minutes = int(seconds // 60)
        seconds = seconds % 60
        return f"{minutes}m {seconds:.2f}s"


class Timer:
    """Context manager for timing code execution."""
    
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
