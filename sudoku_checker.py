# Python3.6.5
# 2/5/2019
import numpy as np
import pandas as pd
from collections import Counter


def menu():
    print("\033[1;32;40m ****************************************")
    print("\033[1;32;40m  ******* Sudoku Puzzle Project *******  ")
    print("\033[1;32;40m ****************************************")

    print("\033[2;35;37m Enter the name of sudoku puzzle file : ")
    filename = input()
    check_board(filename)

def check_board(filename):
    correct = {1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}

    board = None
    with open(filename) as file:
        board = np.array([[int(digit) for digit in line.split()] for line in file])
        print(board)


    assert (len(board) == 9), "Board Length is not exactly 9x9"
    assert len(board) == len(board.T), "Board Length is not exactly 9x9"
    for l in board:
        assert len(l)==9, "Some values are missing"

    #Check Rows
    rows = [dict(Counter(row)) == correct for row in board] 

    #Check Columns
    cols = [dict(Counter(col)) == correct for col in board.T] 

    #Check Boxes
    boxes = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            box = board[i:i+3,j:j+3].flatten()
            boxes.append( dict(Counter(box)) == correct )

    if all(rows) & all(cols) & all(boxes):
        print('\n\n\033[1;32;40mSudoku is Valid\n\n')
        with open(filename+'_checked', 'w') as f:
            f.write(open(filename).read())    
    else:
        print('\n\n\033[2;31;37m Sudoku is INVALID\n\n')

if __name__ == '__main__':
    menu()

