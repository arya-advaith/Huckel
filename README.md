# Hückel Method Matrix Solver

A computational tool for building and diagonalizing Hückel matrices for molecular orbital calculations in quantum chemistry.

## Overview

This program creates and diagonalizes Hückel matrices based on input parameters, providing eigenvalues and eigenvectors that represent molecular orbital energies and coefficients. It can handle both linear (open) and cyclic molecular structures with customizable alpha (Coulomb) and beta (resonance) integrals.

## Features

- Support for both linear and cyclic molecular structures
- Customizable alpha (diagonal) and beta (off-diagonal) parameters
- Handling of alternating alpha and beta values for heterogeneous systems
- Efficient diagonalization using LAPACK library
- Output of eigenvalues and eigenvectors to separate files
- Visualization tools for eigenvalue analysis

## Requirements

- GCC compiler
- LAPACK and LAPACKE libraries
- Standard C libraries (stdio.h, stdlib.h, math.h)
- Python with pandas and matplotlib (for visualization)

## Installation

1. Clone this repository
2. Ensure LAPACK and LAPACKE are installed on your system
3. Compile the program using the included makefile:

```bash
make
```
4. To clean the compilation:
```bash
make clean
```

This will create the executable named `HUCKEL`.

## Usage

### Running the C program

1. Create an `input.txt` file with the following format:

```
ATOM_NUMBER [integer]
ALPHA [value1] [value2]
BETA [value1] [value2]
OPEN [0 or 1]
```

Where:
- `ATOM_NUMBER`: Number of atoms/centers in the system
- `ALPHA`: Coulomb integral values (one or two values)
- `BETA`: Resonance integral values (one or two values)
- `OPEN`: System type (0 for cyclic, 1 for open/linear)

2. Run the program:

```bash
./HUCKEL
```

3. The program will generate two output files:
   - `eigenvalues_.txt`: Contains the eigenvalues (orbital energies)
   - `eigenvectors.txt`: Contains the eigenvectors (orbital coefficients)

### Visualization with Python

The repository includes a Python script (`fileopen.py`) for visualizing eigenvalue data:

```bash
python fileopen.py
```

This script:
- Reads eigenvalue files for various system sizes (from 4 to 1024 atoms)
- Creates plots displaying the eigenvalue distribution
- Generates both full system and half-filled system visualizations
- Saves the output as `eigenvalues_1a1b1close.png`

The visualization assumes you have generated eigenvalue files for different system sizes with the naming convention `eigenvalues_Ne_1a1b1close.txt` where N is the number of atoms.

## Input File Format

The program can handle different input formats, including:
- One or two alpha values
- One or two beta values

Example:
```
ATOM_NUMBER 1024
ALPHA 2 6
BETA -2 -5
OPEN 0
```

In this example:
- The system has 1024 atoms
- Alpha values alternate between 2 and 6
- Beta values alternate between -2 and -5
- The system is cyclic (OPEN = 0)

## Technical Details

### Matrix Construction

- For linear systems (OPEN = 1): Only neighboring atoms are connected
- For cyclic systems (OPEN = 0): The first and last atoms are also connected
- When two alpha values are provided, they alternate along the diagonal
- When two beta values are provided, they alternate along the off-diagonals

### Diagonalization

The program uses LAPACK's `dgeev` function to calculate the eigenvalues and eigenvectors of the Hückel matrix. This provides an efficient solution for large matrices.

### Visualization

The Python script creates a multi-panel figure that shows:
- Left panels: Full eigenvalue spectrum for each system size
- Right panels: Lower half of the eigenvalue spectrum (occupied orbitals when half-filled)

This visualization is particularly useful for studying trends in electronic structure as system size increases.

### Memory Management

The code includes proper memory management:
- Dynamic allocation for matrices and arrays
- Custom 2D array allocation and deallocation functions
- Proper cleanup of all allocated resources

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Copyright (c) 2025 Arya Advaith Satisha
