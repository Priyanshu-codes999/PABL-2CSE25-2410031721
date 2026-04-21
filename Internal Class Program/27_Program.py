def smallestSubWithSum(x, arr):
    n = len(arr)
    
    min_len = n + 1
    curr_sum = 0
    start = 0

    for end in range(n):
        curr_sum += arr[end]

        # Shrink window while sum > x
        while curr_sum > x:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    return 0 if min_len == n + 1 else min_len


# Test Cases
print(smallestSubWithSum(51, [1, 4, 45, 6, 0, 19]))   # 3
print(smallestSubWithSum(100, [1, 10, 5, 2, 7]))      # 0