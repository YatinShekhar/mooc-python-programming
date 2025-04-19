def block_correct(sudoku, row_number, column_number):

    unique_list = []
    for i in range(row_number, row_number+3):
        for j in range(column_number, column_number+3):
            if sudoku[i][j] == 0:
                continue 
            else:
                if sudoku[i][j] not in unique_list:
                    unique_list.append(sudoku[i][j])
                else:
                    return False 
    return True 

    
if __name__ == "__main__":
    
    sudoku = [
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

    print(block_correct(sudoku, 0, 0))