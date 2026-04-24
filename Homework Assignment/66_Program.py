from collections import defaultdict

class Solution:
    def countPairs(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        m = len(arr[0])
        total = 0

        for i in range(m):
            freq = defaultdict(int)

            for s in arr:
                # Replace one position with wildcard
                pattern = s[:i] + '*' + s[i+1:]
                freq[pattern] += 1

            # Count pairs with same pattern
            for cnt in freq.values():
                total += cnt * (cnt - 1) // 2

        # Remove identical string pairs counted m times
        same = defaultdict(int)
        for s in arr:
            same[s] += 1

        for cnt in same.values():
            if cnt > 1:
                total -= m * (cnt * (cnt - 1) // 2)

        return total