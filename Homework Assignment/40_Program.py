def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])   # add current subset

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


# Test Cases
print(subsets([1,2,3]))
print(subsets([0]))