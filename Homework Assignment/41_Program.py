def exist(board, word):
    rows = len(board)
    cols = len(board[0])

    def dfs(r, c, index):
        # Entire word matched
        if index == len(word):
            return True

        # Boundary / mismatch checks
        if (r < 0 or c < 0 or r >= rows or c >= cols or
            board[r][c] != word[index]):
            return False

        # Mark visited
        temp = board[r][c]
        board[r][c] = "#"

        # Explore 4 directions
        found = (
            dfs(r + 1, c, index + 1) or
            dfs(r - 1, c, index + 1) or
            dfs(r, c + 1, index + 1) or
            dfs(r, c - 1, index + 1)
        )

        # Backtrack
        board[r][c] = temp

        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False


# Test Cases
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]

print(exist(board, "ABCCED"))  # True
print(exist(board, "SEE"))     # True
print(exist(board, "ABCB"))    # False