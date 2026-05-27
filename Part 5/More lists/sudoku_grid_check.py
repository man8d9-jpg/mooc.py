def row_correct(sudoko: list, row_no: int):
    row = sudoko[row_no]
    for i in row:
        if i != 0 and row.count(i) > 1:
            return False
    return True 

def column_correct(sudoku: list, column_no: int):
    column = []
    for i in sudoku:
        column.append(i[column_no])
    for i in column:
        if i != 0 and column.count(i) > 1:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            numbers.append(sudoku[i][j])
    for i in numbers:
        if i != 0 and numbers.count(i) > 1:
            return False
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        if row_correct(sudoku, i) == False:
            return False
    
    for i in range(9):
        if column_correct(sudoku, i) == False:
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if block_correct(sudoku, i, j) == False:
                return False
    return True


sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sudoku_grid_correct(sudoku1))

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku2)) 