def minChocolateDiff(arr, m):
    n = len(arr)

    # If students are more than packets
    if m > n:
        return -1

    # If no students or packets
    if m == 0 or n == 0:
        return 0

    # Sort packets
    arr.sort()

    min_diff = float('inf')

    # Check every window of size m
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)

    return min_diff


# Test Cases
print(minChocolateDiff([3, 4, 1, 9, 56, 7, 9, 12], 5))   # 6
print(minChocolateDiff([7, 3, 2, 4, 9, 12, 56], 3))      # 2
print(minChocolateDiff([3, 4, 1, 9, 56], 5))             # 55