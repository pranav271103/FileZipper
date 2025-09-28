from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="filezipper",
    version="0.1.0",
    author="Pranav Singh",
    author_email="pranav.singh01010101@gmail.com",
    description="A Python implementation of file compression using Huffman Coding algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pranav271103/FileZipper",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=[
        "tqdm>=4.65.0",
    ],
    entry_points={
        "console_scripts": [
            "filezipper=filezipper.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: System :: Archiving :: Compression",
    ],
    keywords="compression huffman file-zipper",
)
