from board import board
from solver import solver
from generator import generate

board = board("random")

solver = solver(board)

if __name__ == "__main__":
    print(solver.get_board())
    solver.solve()
    print(solver.get_board())

