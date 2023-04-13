import random
from itertools import islice
from random import sample
from multi_solver import sudokuSolve

# pattern for a baseline valid solution
def pattern(r,c,base): 
    side  = base*base
    return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): 
    return sample(s,len(s))

def generate_raw(base=3):
    side  = base*base
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c,base)] for c in cols] for r in rows ]

    return board

def make_puzzle(board):
    side = len(board)
    squares = side*side
    empties = squares * 3//4
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0
    return board


def make_unique(board):

    while True:
        solved  = [*islice(sudokuSolve(board),2)]
        if len(solved)==1:
            break
        diffPos = []
        for r in range(9):
            for c in range(9):
                if solved[0][r][c] != solved[1][r][c]:
                    diffPos.append((r,c)) 
        r,c = random.choice(diffPos)
        board[r][c] = solved[0][r][c]
    return board

def generate(): return make_unique(make_puzzle(generate_raw()))

