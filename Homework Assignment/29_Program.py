def minSwaps(arr, k):
    n = len(arr)

    # Count good elements
    good = sum(1 for x in arr if x <= k)

    # If already grouped or no good elements
    if good <= 1:
        return 0

    # Count bad elements in first window
    bad = sum(1 for i in range(good) if arr[i] > k)

    ans = bad

    # Slide the window
    for i in range(n - good):
        # remove left element
        if arr[i] > k:
            bad -= 1

        # add right element
        if arr[i + good] > k:
            bad += 1

        ans = min(ans, bad)

    return ans


# Test Cases
print(minSwaps([2, 1, 5, 6, 3], 3))          # 1
print(minSwaps([2, 7, 9, 5, 8, 7, 4], 6))   # 2
print(minSwaps([2, 4, 5, 3, 6, 1, 8], 6))   # 0