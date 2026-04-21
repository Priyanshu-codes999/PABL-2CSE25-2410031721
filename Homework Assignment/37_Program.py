def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

    # Mark rows and columns
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set inner cells to zero
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # First row
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # First column
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix


# Test Cases
print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))