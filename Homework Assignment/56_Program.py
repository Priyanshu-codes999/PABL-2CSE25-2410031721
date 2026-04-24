class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        n = len(arr)

        # Check if we can pick k elements with minimum diff >= mid
        def can_place(mid):
            count = 1
            last = arr[0]

            for i in range(1, n):
                if arr[i] - last >= mid:
                    count += 1
                    last = arr[i]

                    if count >= k:
                        return True
            return False

        low, high = 0, arr[-1] - arr[0]
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans