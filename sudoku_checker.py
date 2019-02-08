# Python3.6.5
# 2/5/2019
import numpy as np
import pandas as pd
from collections import Counter

correct = {1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}

board = pd.read_csv('sudoku.csv',header=None).values

assert len(board) == 9
assert len(board) == len(board.T)

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
	print('\n\nSudoku is Valid\n\n')
else:
	print('\n\nSudoku is INVALID\n\n')
