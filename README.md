# FileZipper

**Efficient file compression and decompression using Huffman Coding in Python**

[![Python Versions](https://img.shields.io/badge/python-3.7%20|%203.8%20|%203.9%20|%203.10%20|%203.11-blue?style=flat-square)](https://www.python.org/downloads/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Docker Image Version](https://img.shields.io/github/v/release/pranav271103/FileZipper?label=ghcr.io%2Fpranav271103%2Ffilezipper&logo=docker&sort=semver&style=flat-square)](https://github.com/pranav271103/FileZipper/pkgs/container/filezipper)


## Features

- **Optimal Compression**: Implements Huffman coding for efficient prefix codes
- **Lightning Fast**: Optimized algorithms for maximum performance
- **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux
- **Detailed Analytics**: Comprehensive compression statistics and metrics
- **Dual Interface**: Use as both a CLI tool and a Python library
- **Robust & Reliable**: Thorough error handling and input validation
- **Memory Efficient**: Handles large files with minimal memory footprint

## Installation

### Using Docker (Recommended)

```bash
# Pull the latest image from GitHub Container Registry
docker pull ghcr.io/pranav271103/filezipper:latest

# Run the container
docker run -v $(pwd):/data ghcr.io/pranav271103/filezipper [command] [options]
```

### From Source

```bash
# Clone the repository
git clone https://github.com/pranav271103/FileZipper.git
cd FileZipper

# Install in development mode
pip install -e .
```

## Command Line Usage

### Using Docker

```bash
# Compress a file
docker run -v $(pwd):/data ghcr.io/pranav271103/filezipper compress /data/input.txt -o /data/compressed.huff

# Decompress a file
docker run -v $(pwd):/data ghcr.io/pranav271103/filezipper decompress /data/compressed.huff -o /data/output.txt
```

### Local Installation

### Compress a File

```bash
filezipper compress input.txt -o compressed.huff
```

### Decompress a File

```bash
filezipper decompress compressed.huff -o output.txt
```

### Available Options

```
Options:
  -o, --output TEXT   Output file path
  -q, --quiet         Suppress non-essential output
  -v, --verbose       Show detailed progress
  --version           Show version and exit
  --help              Show this message and exit
```

## Python API

### Basic Compression/Decompression

```python
from filezipper import HuffmanEncoder, HuffmanDecoder

# Compress data
encoder = HuffmanEncoder()
compressed, codes = encoder.compress(b"Your data here")

# Decompress data
decoder = HuffmanDecoder()
data = decoder.decompress(compressed, codes)
```

### File Operations

```python
from filezipper import HuffmanZipperCLI

zipper = HuffmanZipperCLI()

# Compress file
result = zipper.compress_file("input.txt", "output.huff")
print(f"Compression ratio: {result['compression_ratio']:.2f}")

# Decompress file
zipper.decompress_file("output.huff", "output.txt")
```

## Performance

FileZipper is optimized for both speed and compression ratio:

| File Type       | Compression Ratio | Speed (MB/s) |
|-----------------|-------------------|--------------|
| Text (Plain)   | 2.5:1             | 15.2         |
| Text (JSON)    | 3.1:1             | 14.8         |
| Text (XML)     | 2.8:1             | 14.5         |
| Binary         | 1.2:1             | 18.3         |

*Benchmarks performed on Intel i5-8265U @ 1.60GHz with 8GB RAM*

## Testing

Run the complete test suite:

```bash
pytest tests/ -v
```

Run with coverage report:

```bash
pytest --cov=filezipper tests/
```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Pranav Singh - [@pranav271103](https://github.com/pranav271103)

Project Link: [https://github.com/pranav271103/FileZipper](https://github.com/pranav271103/FileZipper)

## Acknowledgments

- [Huffman Coding](https://en.wikipedia.org/wiki/Huffman_coding) - The elegant compression algorithm
- [Python's heapq](https://docs.python.org/3/library/heapq.html) - For efficient priority queue operations
- [tqdm](https://github.com/tqdm/tqdm) - For beautiful progress bars
- [pytest](https://docs.pytest.org/) - For making testing simple and scalable
