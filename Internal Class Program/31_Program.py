def binary_search(arr, targart):
    left, right =0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == targart:
            return mid
        elif arr[mid] < targart:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr=[1,5,7,9,35]
target = 7
result = binary_search(arr, target)
print(f"Element found at index: {result}")