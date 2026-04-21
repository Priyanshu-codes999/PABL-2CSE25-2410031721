def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2

        row = mid // cols
        col = mid % cols

        val = matrix[row][col]

        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Test Cases
matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]

print(searchMatrix(matrix, 3))   # True
print(searchMatrix(matrix, 13))  # False