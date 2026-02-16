def min_swaps(arr, k):
    n = len(arr)
    # Count elements <= k
    good = sum(1 for x in arr if x <= k)
    # Count bad elements in first window
    bad = sum(1 for x in arr[:good] if x > k)
    ans = bad
    i, j = 0, good
    # Slide the window
    while j < n:
        if arr[i] > k:
            bad -= 1
        if arr[j] > k:
            bad += 1
        ans = min(ans, bad)
        i += 1
        j += 1
    return ans
# Examples
print(min_swaps([2,1,5,6,3], 3))        # 1
print(min_swaps([2,7,9,5,8,7,4], 6))    # 2
print(min_swaps([2,4,5,3,6,1,8], 6))    # 0
