# DISCLAIMER: IT IS BEST SUITED TO READ THIS FILE AT https://github.com/arya-advaith/Huckel/.

# Hückel Method Matrix Solver

A computational tool for building and diagonalizing Hückel matrices for molecular orbital calculations in quantum chemistry.

## Overview

This program creates and diagonalizes Hückel matrices based on input parameters, providing eigenvalues and eigenvectors that represent molecular orbital energies and coefficients. It can handle both linear (open) and cyclic molecular structures with customizable alpha (Coulomb) and beta (resonance) integrals.

## Features

- Support for both linear and cyclic molecular structures
- Customizable alpha (diagonal) and beta (off-diagonal) parameters
- Handling of alternating alpha and beta values for heterogeneous systems
- Efficient diagonalization using LAPACKE library
- Output of eigenvalues and eigenvectors to separate files
- Visualization tools for eigenvalue analysis

## Requirements

- GCC compiler
- LAPACKE (and LAPACK) libraries
- Standard C libraries (stdio.h, stdlib.h, math.h)
- Python with pandas and matplotlib (for visualization)

## Installation

1. Clone this repository
2. Ensure LAPACKE (theorugh LAPACK) is installed on your system
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
   - `eigenvalues_.txt`: Contains the eigenvalues (orbital energies) most probably in atomic units (Hartree `Ha`)
   - `eigenvectors.txt`: Contains the eigenvectors (orbital coefficients)

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

### Atom and Bond Alternation

- The atom alternation and bond alternation results are present in the following folders:
    1. ```bond_alternation/```

    2. ```atom_alternation/```

- After entering the folders, 2 more directories namely:
    1. ```open/```
    2. ```close/```

- There exists the files ranging from 4 atoms to about 1024 atoms. There also exists the subsequent plot to visualize the Eigenvalues and Fermi Level.

- The ```file_open.py ``` is the python scipt to plot the Fermi Level and Eigenvalues.


### Matrix Construction

- For linear systems (OPEN = 1): Only neighboring atoms are connected
- For cyclic systems (OPEN = 0): The first and last atoms are also connected
- When two alpha values are provided, they alternate along the diagonal
- When two beta values are provided, they alternate along the off-diagonals

### Diagonalization

The program uses LAPACKE's `dgeev` function to calculate the eigenvalues and eigenvectors of the Hückel matrix. This provides an efficient solution for large matrices.

### Visualization

The Python script creates a multi-panel figure that shows:
- Left panels: Even number of atoms with full electron occupation and half electron occupation.
- Right panels: Odd number of atoms with full electron occupation and half electron occupation.

This visualization is particularly useful for studying trends in electronic structure as system size increases.

### Memory Management

The code includes proper memory management: [This part was taken from another TCCM course (Advanced Computational Techniques HW)]
LINK: https://github.com/scemama/tccm-homeworks (inside project3/dynamics.pdf)
- Dynamic allocation for matrices and arrays
- Custom 2D array allocation and deallocation functions
- Proper cleanup of all allocated resources

### Inferences from the Graphs:

#### Atom and Bond alternation system which also happens to be cyclic: [ 2 $\alpha$ [2,6 ] and 2 $\beta$ [-2,-5]]

![image alt](https://github.com/arya-advaith/Huckel/blob/main/atom_alternation/close/eigenvalues_2a2b1close.png)

- As seen from the image, the Fermi Level for larger atoms tend towards:
  1) E = -1.744 Ha for Half occupued system [1 electron for 2 atoms].
  2) E =  0.3944 Ha for even atoms and 2.514 Ha for odd atoms if fully occupied [1 electron per atom].
  
#### Atom and Bond alternation system which also happens to be linear or open: [ 2 $\alpha$ [2,6 ] and 2 $\beta$ [-2,-5]]

![image alt](https://github.com/arya-advaith/Huckel/blob/main/atom_alternation/open/eigenvalues_2a2b1open.png)

- As seen from the image, the Fermi Level for larger atoms tend towards:
  1) E = -1.74 Ha for Half occupied system [1 electron for 2 atoms].
  2) E =  2 Ha if fully occupied [1 electron per atom].

#### Bond alternation system which also happens to be cyclic: [ 1 $\alpha$ [2 ] and 2 $\beta$ [-2,-5]]

![image alt](https://github.com/arya-advaith/Huckel/blob/main/bond_alternation/close/eigenvalues_1a2b1close.png)

- As seen from the image, the Fermi Level for larger atoms tend towards:
  1) E = -3.38 Ha for Half occpuied system [1 electron for 2 atoms].
  2) E =  -1 Ha for even atoms and 2 Ha for odd atoms if fully occupied [1 electron per atom].

#### Bond alternation system which also happens to be linear or open: [ 1 $\alpha$ [2] and 2 $\beta$ [-2,-5]]

![image alt](https://github.com/arya-advaith/Huckel/blob/main/bond_alternation/open/eigenvalues_1a2b1open.png)

- As seen from the image, the Fermi Level for larger atoms tend towards:
  1) E = -3.38 Ha for Half occupied system [1 electron for 2 atoms].
  2) E =  2 Ha if fully occupied [1 electron per atom].
     
## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Copyright (c) 2025 Arya Advaith Satisha
