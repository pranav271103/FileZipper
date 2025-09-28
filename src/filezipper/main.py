#!/usr/bin/env python3
"""
Huffman File Zipper - A command-line tool for file compression using Huffman coding.
"""

import sys
from cli import main as cli_main

def main():
    """Main entry point for the Huffman Zipper."""
    try:
        cli_main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
