def combination_sum(arr, target):
    result = []
    def dfs(index, remaining, path):
        if remaining == 0:
            result.append(path[:])
            return
        # if out of bounds or remaining is negative, backtrack
        if index >= len(arr) or remaining < 0:
            return
        # include the number
        path.append(arr[index])
        dfs(index, remaining - arr[index], path)
        path.pop()
        # exclude the number
        dfs(index + 1, remaining, path)
    dfs(0, target, [])
    return result
arr = [2,3,5]
target = 8
print(combination_sum(arr, target))
