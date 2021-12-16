"""
Solving KenKen puzzles using recursion in a very friendly and interactive GUI 
Sources for this project:
https://www.reddit.com/r/dailyprogrammer/comments/3snorf/20151113_challenge_240_hard_kenken_solver/
http://norvig.com/sudoku.html
https://github.com/MikeXydas/kenkenSolver/blob/master/kenKen.py
https://github.com/aimacode/aima-python/blob/master/gui/eight_puzzle.py
https://codereview.stackexchange.com/questions/223513/kenken-solver-python
https://en.wikipedia.org/wiki/Search_algorithm

from textbooks: 
1-Think Python
2-An Introduction to Tkinter
he code below is modified from this reddit post: https://www.reddit.com/r/dailyprogrammer/comments/3snorf/20151113_challenge_240_hard_kenken_solver/

Thakns to Kenneth James for answering my questions anf for giving me full approval to use it and modify it. His Github page: https://github.com/kennethjmyers/Metis-Projects/tree/master/kojak/kenken_solver

"""
from functools import reduce
import operator

def scantext(board, cage_map, cell, i):
    val, op, coords = cage_map[cell]
    vals = [board[coord] for coord in coords]
    if not all(vals):
       return True
    if op == "=":
        return i == val
    elif op == "+":
        return sum(vals) == val
    elif op == "*":
        return reduce(operator.mul, vals) == val
    elif op == "-":
        return abs(vals[0] - vals[1]) == val
    elif op == "/":
        bigger, smaller = max(vals), min(vals)
        return bigger % smaller == 0 and bigger // smaller == val

def recurse(sz, cage_map, board, cell_list, depth=0):
    if depth == len(cell_list):
        return True
    cell = cell_list[depth]
    X, Y = cell
    used = {board[(x, Y)] for x in range(sz)} | {board[(X, y)] for y in range(sz)}
    for i in set(range(1, sz+1)) - used:
        board[cell] = i
        if not scantext(board, cage_map, cell, i):
            continue
        if recurse(sz, cage_map, board, cell_list, depth+1):
            return True
    board[cell] = None

def read_file(file_name):
    # Read lines (skip empty)
    lines = []
    with open(file_name) as file:
        lines = filter(len, file.read().splitlines())

    sz, *cages = lines
    sz = int(sz)

    name_to_coord = lambda name: ('ABCDEFGHI'.index(name[0]), int(name[1])-1)
    cages = [
        (int(val), operator, [name_to_coord(coord) for coord in coords])
        for val, operator, *coords in map(str.split, cages)
    ]
    
    print(cages)
    
    cage_map = {
        coord: cage
        for cage in cages
        for coord in cage[2]
    }

    board = {
        coord: None for coord in cage_map
    }
    cell_list = list(sorted(board))
    
        
    return sz, cage_map, board, cell_list
    

def solve_puzzle(file_name, verbose=False):
    sz, cage_map, board, cell_list = read_file(file_name)
    if sz is None and cage_map is None and board is None and cell_list is None:
        return []
    recurse(sz, cage_map, board, cell_list)
    lines = []
    if verbose:
        for y in range(sz):
            line = " ".join(str(board[(x, y)]) for x in range(sz))
            print(line)
            lines.append(list())
            lines[-1] = [board[(x, y)] for x in range(sz)]
            #lines.append(line)
        return lines
    else:
        return board