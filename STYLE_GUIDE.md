# EnergyVision Python Style Guide

This style guide outlines the coding conventions for Python code in the EnergyVision project. Following these guidelines helps maintain consistency, readability, and quality across the codebase.

> **Note:** This guide is in part based on the [PEP 8](https://www.python.org/dev/peps/pep-0008/) and [PEP 257](https://www.python.org/dev/peps/pep-0257/) guidelines. Please ensure your contributions follow these conventions.

## 1. General Formatting

- **Maximum Line Length:**  
  Limit all lines to 79 characters. For long blocks of text (e.g., docstrings or comments), 72 characters is recommended.

- **Blank Lines:**  
  - Surround top-level function and class definitions with two blank lines.
  - Methods within a class should be surrounded by a single blank line.

## 2. Naming Conventions

- **Variables and Functions:**  
  Use lowercase letters with words separated by underscores (e.g., `data_processor`, `calculate_total`).

- **Classes:**  
  Use the CapWords (CamelCase) convention (e.g., `DataProcessor`, `EnergyAnalyzer`).

- **Constants:**  
  Use all uppercase letters with words separated by underscores (e.g., `MAX_RETRIES`, `DEFAULT_TIMEOUT`).

- **Modules and Packages:**  
  - Module names should be short, all-lowercase names.  
  - Package names should also be all lowercase, without underscores.

## 3. Imports

- **Grouping:**  
  Imports should be grouped in the following order, with a blank line between each group:
  1. Standard library imports.
  2. Third-party imports.
  3. Local application/library-specific imports.

- **Import Style:**  
  - Use absolute imports wherever possible.
  - Avoid wildcard imports (e.g., `from module import *`).

## 4. Docstrings and Comments

- **Docstrings:**  
  Write docstrings for all public modules, functions, classes, and methods using triple double-quotes (`"""`).
  Follow [PEP 257](https://www.python.org/dev/peps/pep-0257/) conventions.  
  *Example:*
  ```python
  def process_data(data):
      """
      Process the given data and return the results.

      Parameters:
          data (list): A list of data points.

      Returns:
          list: A list of processed data points.
      """
      return [d * 2 for d in data]
