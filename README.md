# README

## Overview
This program processes input files containing crystal and mine data, evaluates different strategies for maximizing resource collection while minimizing losses from mines, and generates output based on the best strategy.

## Features
- Reads input files with crystal and mine locations, along with their values.
- Implements different strategies to determine the best achievable score.
- Uses sorting and map-based aggregation for efficient computation.
- Implements methods for selecting optimal areas (stripperX, stripperY, best165, worst165) based on computed thresholds.
- Generates structured output with visualized boundaries.

## Input Format
Each input file follows this format:
1. **Number of crystals (n)**
2. **n lines**: Each containing three integers representing the crystal's **x-coordinate, y-coordinate, and value**.
3. **Number of mines (m)**
4. **m lines**: Each containing three integers representing the mine's **x-coordinate, y-coordinate, and negative value**.

### Example Input
```
5
1 2 10
3 4 20
5 6 30
7 8 40
9 10 50
3
2 3 -5
4 5 -10
6 7 -15
```

## Output Format
The program generates structured output depending on the optimal strategy found. The output consists of:
- The best achievable score.
- The number of edges used in the visualization.
- The edges defining the selected boundary.

### Example Output
```
1000
50, 50
(0.0, 0.0), (10.0, 0.0)
(10.0, 0.0), (10.0, 10.0)
...
```

## Compilation & Execution
### Compilation
Example - 
Use `g++` to compile the program:
```sh
 g++ -o file_name.cpp -O2
```

### Execution
Run the program with input and output redirection:
```sh
./file < input/input01.txt > output/output01.txt
```

Alternatively, batch processing can be done using:
```sh
./file
```
This will process multiple input files as defined in `inp_normal()`.

## Code Structure
- `struct node`: Defines a crystal or mine with `x, y, val` attributes.
- `_input()`: Reads input data and initializes structures.
- `stripperX()` / `stripperY()`: Determines optimal sections along the X/Y axis.
- `generate_stripperX()` / `generate_stripperY()`: Generates output for X/Y-based selection.
- `generateBest165()`: Computes the best 165 points selection.
- `generateWorst165()`: Computes the worst 165 points selection.
- `inp_normal()`: Processes multiple input files iteratively.

## Optimizations
- **Sorting for efficient selection**: Uses `sort()` and `reverse()` to select optimal elements.
- **Fast I/O**: Uses `ios_base::sync_with_stdio(false); cin.tie(NULL);` for improved performance.
- **Unrolling loops**: Uses `#pragma GCC optimize("Ofast,unroll-loops")`.
- **Efficient lookups**: Uses `map` for quick retrieval of values.

## Dependencies
- Requires C++11 or later.
- Uses standard libraries (no external dependencies).

## Notes
- The program is optimized for large inputs with up to 10,000 x 10,000 grid space.
- The generated output includes structured boundary definitions that can be used for visualization.
- Edge cases such as overlapping points and high density of mines are handled efficiently.
