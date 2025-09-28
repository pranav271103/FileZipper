# Contributing to FileZipper

Thank you for considering contributing to FileZipper! We welcome all contributions, including bug reports, feature requests, documentation improvements, and code contributions.

## How to Contribute

### Reporting Issues
- Check if the issue has already been reported
- Provide a clear title and description
- Include steps to reproduce the issue
- Share the expected and actual behavior
- Include version information (Python, OS, etc.)

### Development Setup
1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/pranav271103/FileZipper.git
   cd FileZipper
   ```
3. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install development dependencies:
   ```bash
   pip install -e .[dev]
   ```
5. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

### Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
- Use type hints for all functions and methods
- Include docstrings following [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Run code formatters before committing:
  ```bash
  black .
  isort .
  ```

### Testing
- Write tests for new features and bug fixes
- Run tests locally:
  ```bash
  pytest -v
  ```
- Ensure all tests pass before submitting a pull request

### Pull Requests
1. Create a new branch for your changes
2. Make your changes with clear, logical commits
3. Update documentation as needed
4. Ensure tests pass
5. Submit a pull request with a clear description of changes

## Code of Conduct

This project adheres to the [Contributor Covenant](https://www.contributor-covenant.org/). By participating, you are expected to uphold this code.
