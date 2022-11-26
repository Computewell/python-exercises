""" 
Write a getChessSquareColor() function that has parameters column and row. 
The function either returns 'black' or 'white' depending on the color at the specified column and row.
Hint-->Chess boards are 8 x 8 spaces in size, and the columns and rows in this program begin at 0 and end at 7
"""

def getChessSquareColor(column, row):
    if column < 1 or column > 8 or row < 1 or row > 8:
        return ''
    if column % 2 == row % 2:
        return 'white'
    else:
        return 'black'
# Test Cases
assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
assert getChessSquareColor(9, 2) == ''