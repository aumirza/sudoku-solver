class solver:
     
    def __init__(self,board):
        self.board= board

    def solve(self):
        pos = self.board.get_empty()

        if not pos:
            return True

        for i in range(1,10):
            if self.board.check_valid(i,*pos):
                self.board.fill_cell(i,*pos)

                if self.solve():
                    return True

                self.board.fill_cell(0,*pos)

        return False

    def get_board(self):
        return self.board
