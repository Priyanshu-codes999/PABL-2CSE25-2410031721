# ---------- 1️⃣ Pair with Given Sum ----------
# 2 pointer algorithm to find a pair of numbers in an array that sum up to a target value.
def pair_sum(arr, target):
    left, right = 0, len(arr) - 1
    arr.sort()

    while left < right:
        s = arr[left] + arr[right]

        if s == target:
            return arr[left], arr[right]
        elif s < target:
            left += 1
        else:
            right -= 1

    return "No pair found"


# ---------- 2️⃣ Reverse Array ----------
def reverse_array(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# ---------- 3️⃣ Remove Duplicates (Sorted Array) ----------
def remove_duplicates(arr):
    if not arr:
        return []

    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return arr[:i+1]


# ---------- 4️⃣ Container With Most Water ----------
def max_water(height):
    left, right = 0, len(height)-1
    max_area = 0

    while left < right:
        area = min(height[left], height[right]) * (right-left)
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# ===== Example Usage =====
arr = list(map(int, input("Enter array: ").split()))
target = int(input("Enter target sum: "))

print("\nPair with sum:", pair_sum(arr, target))
print("Reversed array:", reverse_array(arr[:]))
print("Remove duplicates:", remove_duplicates(sorted(arr)))
print("Max water:", max_water(arr))