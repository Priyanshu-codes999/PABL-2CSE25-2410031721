def trap_water(arr):
    n = len(arr)
    if n == 0:
        return 0

    left, right = 0, n - 1
    left_max = right_max = 0
    water = 0

    while left <= right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water += right_max - arr[right]
            right -= 1

    return water


# Examples
print(trap_water([3,0,1,0,4,0,2]))  # 10
print(trap_water([3,0,2,0,4]))      # 7
print(trap_water([1,2,3,4]))        # 0
print(trap_water([2,1,5,3,1,0,4]))  # 9
