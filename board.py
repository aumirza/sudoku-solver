from generator import generate
from copy import deepcopy

class board:

    def __init__(self,board=None):
        if board == "random":
            board = generate()
            self.board_origin = board
            self.board = deepcopy(self.board_origin)
        else:
            if not board:
                board = [   [0, 0, 0, 0, 0, 0, 0, 0, 8],
                            [0, 2, 0, 0, 5, 0, 7, 6, 0],
                            [0, 6, 0, 0, 0, 0, 0, 0, 3],
                            [5, 0, 0, 0, 0, 0, 2, 0, 7],
                            [0, 3, 0, 0, 1, 0, 0, 0, 0],
                            [2, 0, 0, 4, 0, 0, 0, 3, 0],
                            [0, 0, 0, 6, 0, 0, 0, 0, 0],
                            [8, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 2, 7, 0, 0, 4, 0]
                        ]
            self.board_origin = board
            self.board = deepcopy(self.board_origin)
        

    def __repr__(self):
        board_repr = ""
        for i in range(len(self.board)):
            if (i % 3 == 0) & (i != 0):
                board_repr += "--------------------------\n"

            for j in range(len(self.board[0])):
                if j==0:
                    board_repr += " "

                if (j % 3 == 0) & (j !=0):
                    board_repr += " | "
                    
                board_repr += str(self.board[i][j])
                board_repr += " "
            
            board_repr += "\n"
        return board_repr

    def get_empty(self):
        for row in range(len(self.board)):
            for coloumn in range(len(self.board[0])):
                if self.board[row][coloumn] == 0:
                    return (row,coloumn)

    def get_used(self):
        for row in range(len(self.board)):
            for coloumn in range(len(self.board[0])):
                if self.board[row][coloumn] and not self.board_origin[row][coloumn]:
                    yield (row,coloumn)

    def get_def_val(self):
        for row in range(len(self.board_origin)):
            for coloumn in range(len(self.board_origin[0])):
                if self.board_origin[row][coloumn]:
                    yield (row,coloumn)

    def get_val(self,row,coloumn):
        return self.board[row][coloumn]

    def check_valid(self,number,row,coloumn):

        # Check row
        for i in range(len(self.board[0])):
            if self.board[row][i] == number and coloumn != i:
                return False

        # Check column
        for i in range(len(self.board)):
            if self.board[i][coloumn] == number and row != i:
                return False

        # Check box
        box_x = coloumn // 3
        box_y = row // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.board[i][j] == number and (i!=row & j!= coloumn):
                    return False

        return True

    def fill_cell(self,number,row,coloumn):
        if not self.board_origin[row][coloumn]:
            self.board[row][coloumn] = number
    
    def reset_board(self):
        self.board = deepcopy(self.board_origin)
