# Sudoku Solver

A simple graphical Sudoku solver built using Python and Tkinter. This solver supports both 4x4 and 9x9 Sudoku puzzles, allows you to input values manually, and automatically solves the puzzle using backtracking. It also highlights errors in the input grid and provides user feedback.

## Features

- **Grid Size Selection**: Choose between a 4x4 or 9x9 Sudoku grid.
- **Manual Input**: Input numbers manually into the grid. Invalid entries (numbers outside the allowed range) are flagged.
- **Backtracking Algorithm**: Automatically solves the Sudoku puzzle using a backtracking algorithm.
- **Error Handling**: Checks if the initial grid has any conflicts and prevents solving if it does.
- **Clear Grid**: Clears the grid for starting a new puzzle.

## Requirements

- Python 3.x
- Tkinter (included with Python standard library)

## Installation

1. Clone the repository or download the code.
2. Install Python 3.x if you haven't already: [Download Python](https://www.python.org/downloads/)
3. No additional installations are required as Tkinter is part of Python's standard library.

## Usage

1. Run the `main.py` file to launch the application.
2. Select the Sudoku grid size (4x4 or 9x9).
3. Enter the puzzle values manually in the grid. Blank cells are represented by empty inputs.
4. Click the "Solve" button to automatically solve the puzzle.
5. If the grid has any conflicts or invalid entries, the application will prompt you with an error message.
6. To reset the board, click the "Clear" button.

## Example

1. **Grid Setup**:
    - Input the Sudoku puzzle manually or start with an empty grid.
    - For a 9x9 grid, you might input a standard puzzle.
  
2. **Solving**:
    - After filling the grid, click "Solve".
    - The solver will attempt to fill the grid and show the solved puzzle.

## Backtracking Algorithm

The solver uses the **backtracking** algorithm to solve the puzzle. It works by trying to fill in the grid one cell at a time and recursively trying possible values. If a value causes a conflict, the algorithm backtracks and tries a different value until the puzzle is solved or proven unsolvable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
