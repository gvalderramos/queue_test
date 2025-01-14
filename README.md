Queue Test
-------------------------------

A queue algorithm test.

Please run ./run docs for more info about the use.

# Run Scripts

This project includes a run script (if windows: `run.bat`, otherwise if UNIX: `run`) to simplify common tasks during development, testing, and deployment. Below is a detailed description of each available run command.

## Commands

### General Commands

- **help**  
  Displays a list of all available commands with their descriptions.

- **clean**  
  Cleans up all build, test, coverage, and Python artifacts. This command is a combination of the following:
  - `clean-build`
  - `clean-pyc`
  - `clean-test`

### Cleaning Commands

- **clean_build**  
  Removes all build artifacts, including directories and files related to distribution:
  - `build/`
  - `dist/`
  - `.eggs/`
  - `*.egg-info`
  - `*.egg`

- **clean_pyc**  
  Removes Python file artifacts, including:
  - `*.pyc`, `*.pyo`
  - Temporary files (`*~`)
  - Python cache directories (`__pycache__/`)

- **clean_test**  
  Removes test and coverage artifacts:
  - `.coverage`
  - `htmlcov/`
  - `.pytest_cache`

### Code Quality Commands

- **lint**  
  Alias for `lint/flake8`. Checks the code style using `flake8`.

- **format**  
  Alias for `format/black`. Formats the Python source and test folders.

### Testing and Coverage Commands

- **test**  
  Runs the test suite using `pytest`.

- **coverage**  
  Checks code coverage using `coverage.py`. This generates a coverage report in the terminal and as an HTML file in the `htmlcov/` directory. The HTML report is opened in the default web browser.

### Documentation Commands

- **docs**  
  Generates Sphinx HTML documentation, including API docs. The generated documentation is opened in the default web browser. This command:
  - Cleans the `docs/` directory.
  - Runs `sphinx-apidoc` to generate API documentation.
  - Builds the HTML documentation.

### Installation Commands

- **install**  
  Cleans the environment and installs the package to the active Python's `site-packages`.

### Other Notes

- **Default Goal**  
  Running `make` without any arguments will display the `help` command by default.
