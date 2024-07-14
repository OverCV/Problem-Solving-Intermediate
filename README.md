# Project Documentation

This project serves as a learning exercise to explore data structures and algorithms in Python and C languages, using problems from HackerRank and LeetCode.

## Overview

The project is divided into two main parts: Python and C. Each part focuses on implementing solutions to various algorithmic challenges.

### Python Programming Language

#### Setup

1. **Create a Virtual Environment:**

   First, initialize the virtual environment:

   ```powershell
   python -m venv .venv
    ```

2. **Activate the Virtual Environment:**

   Activate the virtual environment:

   ```powershell
   .venv\Scripts\activate
   ```

3. **Install Dependencies:**

    Install required dependencies using pip:

    ```powershell
    py -m pip install -r requirements.txt
    ```

#### Running Tests with Pytest

To run the test cases for the Python part, use the following command at the root directory:

```powershell
pytest -v -s tests_hr
```

This command executes pytest with verbose output (-v) and shows stdout output (-s).

### C Programming Language

#### Setup and Compilation

1. **Install GCC Compiler:**

   Ensure that you have the GCC compiler installed on your system.

2. **Compile C Programs:**

    Compile your C code (replace main.c with your actual C source file if different):

    ```powershell
    gcc main.c -o main
    main
    ```

    This command compiles the C source file main.c and creates an executable named main. The second command runs the compiled program.
