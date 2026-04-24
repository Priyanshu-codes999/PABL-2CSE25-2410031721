# ---------- 1️⃣ Brute Force Subarray Sum ----------
def subarray_sum_bruteforce(arr):
    n = len(arr)

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            print(f"Subarray {arr[i:j+1]} Sum =", total)


# ---------- 2️⃣ Prefix Sum Method ----------
def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix


def range_sum(prefix, l, r):
    if l == 0:
        return prefix[r]
    return prefix[r] - prefix[l-1]


# ---------- 3️⃣ Subarray with Given Sum (Best Method) ----------
def subarray_with_sum(arr, k):
    prefix_sum = 0
    seen = {0: 1}
    count = 0

    for num in arr:
        prefix_sum += num

        if prefix_sum - k in seen:
            count += seen[prefix_sum - k]

        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count


# ===== Example Usage =====
arr = list(map(int, input("Enter array: ").split()))
k = int(input("Enter target sum: "))

print("\nAll subarray sums:")
subarray_sum_bruteforce(arr)

prefix = prefix_sum(arr)
print("\nPrefix array:", prefix)

print("\nSubarrays with sum =", k, ":",
      subarray_with_sum(arr, k))
