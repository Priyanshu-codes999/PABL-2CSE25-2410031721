class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)

        # Find pivot = index of minimum element
        low, high = 0, n - 1

        while low < high:
            mid = (low + high) // 2

            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid

        pivot = low

        # Binary search on virtual sorted array
        low, high = 0, n - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            real = (mid + pivot) % n

            if arr[real] <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans + 1