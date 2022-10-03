'''
sudoku.py
GitHub: https://github.com/JSquaredJace/Sudoku_Solver
Author: Jace Johnson
Version: 0.0.1
Date: 10/1/22

Program for solving Sudoku puzzles and generating random sudoku puzzles
'''
# Modules
import random

# Global variables
_EASY_MODE_PERCENT_FILLED   = 45
_MED_MODE_PERCENT_FILLED    = 38
_HARD_MODE_PERCENT_FILLED   = 28

# Classes
class Sudoku():
    '''Contains the sudoku board and methods to modify it'''
    def __init__(self):
        self.board      = []
        for _ in range(9):
            self.board.append(['.'] * 9)
        self.board_fill = _EASY_MODE_PERCENT_FILLED
        self.clear_bias = self.board_fill / 9


    #helper functions
    def set_bit(self, x, k):
        '''set the kth bit of x'''
        return (1 << k) | x
    def get_bit(self, x, k):
        '''get the kth bit of x'''
        return (x >> k) & 1
    def clear_bit(self, x, k):
        '''reset the kth bit of x'''
        return ~(1 << k) & x


    def print_board(self):
        '''print the board to the terminal'''
        for i in range(9):
            print(self.board[i])


    def change_difficulty(self, x: int):
        '''Change the difficulty of the puzzle

        Keyward arguments:
        x     difficulty level between 1 and 3
        '''
        if x == 1:
            self.board_fill     = _EASY_MODE_PERCENT_FILLED
        elif x == 2:
            self.board_fill     = _MED_MODE_PERCENT_FILLED
        elif x == 3:
            self.board_fill     = _HARD_MODE_PERCENT_FILLED
        else:
            print("Invalid difficulty selection\nDefaulting to easy difficulty")
            self.board_fill     = _EASY_MODE_PERCENT_FILLED

        self.clear_bias         = self.board_fill / 9


    def build_board(self):
        '''Fill the gameboard with valid numbers'''
        rows            = [0] * 9
        cols            = [0] * 9
        boxes           = [0] * 9
        remaining_clear = 81 - self.board_fill
        bias_correction = 0

        self.backtracking_algorithm(generation_mode = 1)

        for r in range(9):
            for c in range(9):
                #Skip remaining board if there are enough blank spaces
                if remaining_clear < 1:
                    break

                #Fill board randomly based on difficulty
                if random.randint(1, 81) > (self.board_fill - bias_correction):
                    #remove number from board
                    b                   = (r // 3) * 3 + (c // 3)
                    number              = int(self.board[r][c])
                    self.board[r][c]    = '.'
                    rows[r]             = self.clear_bit(rows[r], number)
                    cols[c]             = self.clear_bit(cols[c], number)
                    boxes[b]            = self.clear_bit(boxes[b], number)
                    remaining_clear     -= 1
                    continue

            bias_correction = (remaining_clear - ((81 - self.board_fill) / 9 \
                * (8 - r))) * self.clear_bias


    def solve_board(self):
        '''Solve the gameboard'''
        rows            = [0] * 9
        cols            = [0] * 9
        boxes           = [0] * 9
        empty_positions = []

        for r in range(9):
            for c in range(9):
                #get row, col, and box contents
                if self.board[r][c] != '.':
                    #get box number
                    b = (r // 3) * 3 + (c // 3)
                    rows[r]     = self.set_bit(rows[r], int(self.board[r][c]))
                    cols[c]     = self.set_bit(cols[c], int(self.board[r][c]))
                    boxes[b]    = self.set_bit(boxes[b], int(self.board[r][c]))
                #get locations of empty positions
                else:
                    empty_positions.append([r, c])

        self.backtracking_algorithm(empty_positions, rows, cols, boxes)


    def backtracking_algorithm(
        self,
        empty_positions             = None,
        rows                        = None,
        cols                        = None,
        boxes                       = None,
        index                       = 0,
        generation_mode             = 0,
        generation_first_pass       = 1):
        '''Apply backtracking algorithm to solve Sudoku and create solvable
        Sudoku

        Keyward arguments:
        empty_positions   Positions on the board that do not have numbers
        rows              Contents of each row on the board
        cols              Contents of each column on the board
        boxes             Contents of each box on the board
        index             EmptyPosition index to track recursion
        generation_mode   Sets the function to generation mode

        Outputs:
        True    all empty positions on the board have been filled
        False   one or more previous filled numbers are incorrect (used for
                backtracking)
        '''
        #default values
        if empty_positions is None:
            empty_positions = []
        if rows is None:
            rows            = [0] * 9
        if cols is None:
            cols            = [0] * 9
        if boxes is None:
            boxes           = [0] * 9

        #fill Empty Positions with entire grid coordinates in generation mode
        if (generation_mode == 1) and (generation_first_pass == 1):
            empty_positions = []
            for r in range(9):
                for c in range(9):
                    empty_positions.append([r, c])

        #check if all empty positions on the board have been filled
        if index == len(empty_positions):
            return True

        #get row, column, and box numbers
        r, c    = empty_positions[index]
        b       = (r // 3) * 3 + (c // 3)

        #Random numbers used for generation mode
        number = random.randint(0, 8)
        for num in range(9):
            #increment number
            if generation_mode == 1:
                number = (number % 9) + 1
            else:
                number = num + 1
            #if numbrer exists in row, col, or box, skip it
            if (self.get_bit(rows[r], number)) or \
                (self.get_bit(cols[c], number)) or \
                (self.get_bit(boxes[b], number)):
                continue

            #add valid number to board
            self.board[r][c]    = str(number)
            rows[r]             = self.set_bit(rows[r], number)
            cols[c]             = self.set_bit(cols[c], number)
            boxes[b]            = self.set_bit(boxes[b], number)

            #call function with incremented index
            if self.backtracking_algorithm(
                empty_positions,
                rows,
                cols,
                boxes,
                (index + 1),
                generation_mode,
                generation_first_pass = 0):
                return True
            #Clear bits if next position could not find a working value
            self.board[r][c]    = '.'
            rows[r]             = self.clear_bit(rows[r], number)
            cols[c]             = self.clear_bit(cols[c], number)
            boxes[b]            = self.clear_bit(boxes[b], number)
        #return false if no numbers work for the current board
        return False

# ''' Test Code '''
# sudoku_puzzle = Sudoku()
# sudoku_puzzle.change_difficulty(2)
# sudoku_puzzle.build_board()
# sudoku_puzzle.print_board()
# print('')
# sudoku_puzzle.solve_board()
# sudoku_puzzle.print_board()
