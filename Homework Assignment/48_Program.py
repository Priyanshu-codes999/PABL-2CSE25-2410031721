class Solution:
    def minPeople(self, arr):
        n = len(arr)
        intervals = []

        # Build valid coverage intervals
        for i in range(n):
            if arr[i] != -1:
                left = max(0, i - arr[i])
                right = min(n - 1, i + arr[i])
                intervals.append((left, right))

        # Sort by start time
        intervals.sort()

        count = 0
        i = 0
        covered = 0
        m = len(intervals)

        # Greedy interval covering
        while covered < n:
            farthest = covered - 1

            while i < m and intervals[i][0] <= covered:
                farthest = max(farthest, intervals[i][1])
                i += 1

            # Cannot extend coverage
            if farthest < covered:
                return -1

            count += 1
            covered = farthest + 1

        return count