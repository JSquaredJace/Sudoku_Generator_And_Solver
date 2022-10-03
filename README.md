# Sudoku_Generator_And_Solver
 A simple Python module for generating and solving Sudoku puzzles. This method uses a class called **Sudoku** to manage the processes in creating a Sudoku board or solving a Sudoku board.
 
## Attributes

**board** _( list( list( int )))_ - A 2D list that stores the values of the Sudoku puzzle. Empty board positions are represented as periods ( . ).


## Methods
 
**build_board** _(None)_ - Generate a Sudoku puzzle, stored in the **board** attribute.

**change_difficulty** _(1, 2, or 3, default is 1)_ - Adjust the amount of numbers on the board when generating a Sudoku puzzle. 1 is the easiest setting (around 45 numbers), 2 is medium (around 38) and 3 is the hardest (around 28).

**print_board** _(None)_ - Print the Sudoku board to the terminal.

**solve_board** _(None)_ - Solve the Sudoku puzzle that is currently saved in the board.
 
 
## Example Usage

Create a medium difficulty Sudoku puzzle and print it to the terminal:

```
sudoku_puzzle = Sudoku()
sudoku_puzzle.change_difficulty(2)
sudoku_puzzle.build_board()
sudoku_puzzle.print_board()
```

This yeilded the following board to the terminal:

```
['8', '.', '.', '6', '.', '7', '.', '4', '5']
['1', '5', '2', '.', '3', '.', '.', '.', '.']
['.', '.', '.', '8', '.', '2', '.', '.', '.']
['5', '9', '6', '.', '.', '.', '4', '.', '2']
['.', '2', '4', '.', '8', '.', '.', '9', '7']
['.', '.', '8', '.', '.', '.', '.', '5', '6']
['.', '.', '.', '.', '.', '3', '8', '.', '4']
['9', '.', '.', '2', '.', '5', '.', '6', '1']
['2', '.', '.', '.', '6', '8', '5', '3', '9']
```
As we can see, this created a board with 38 numbers filled in, which is what we want at this difficulty. _This program adds some randomness to the board generation, so a slightly different amount of numbers may be generated._


Now let's have the computer solve this puzzle:

```
sudoku_puzzle.solve_board()
sudoku_puzzle.print_board()
```

This yeilded the following board to the terminal:

```
['8', '3', '9', '6', '1', '7', '2', '4', '5']
['1', '5', '2', '4', '3', '9', '6', '7', '8']
['4', '6', '7', '8', '5', '2', '9', '1', '3']
['5', '9', '6', '3', '7', '1', '4', '8', '2']
['3', '2', '4', '5', '8', '6', '1', '9', '7']
['7', '1', '8', '9', '2', '4', '3', '5', '6']
['6', '7', '5', '1', '9', '3', '8', '2', '4']
['9', '8', '3', '2', '4', '5', '7', '6', '1']
['2', '4', '1', '7', '6', '8', '5', '3', '9']
```
We can see here that the program was able to successfully solve the Sudoku puzzle.
