class Solution:
    def minDifference(self, arr):
        # Convert HH:MM:SS -> total seconds
        times = []

        for t in arr:
            h, m, s = map(int, t.split(":"))
            total = h * 3600 + m * 60 + s
            times.append(total)

        times.sort()

        ans = float('inf')

        # Adjacent differences
        for i in range(1, len(times)):
            ans = min(ans, times[i] - times[i - 1])

        # Circular difference across midnight
        day = 24 * 3600
        ans = min(ans, day - times[-1] + times[0])

        return ans