class Solution:
    def minCost(self, n, m, a, q, queries):
        ans = []

        for R, C in queries:
            # Convert 1-based indexing to 0-based
            R -= 1
            C -= 1

            total = 0

            # Section 1: Top-left
            if R > 0 and C > 0:
                mn = float('inf')
                for i in range(R):
                    for j in range(C):
                        mn = min(mn, a[i][j])
                total += mn

            # Section 2: Top-right
            if R > 0 and C < m - 1:
                mn = float('inf')
                for i in range(R):
                    for j in range(C + 1, m):
                        mn = min(mn, a[i][j])
                total += mn

            # Section 3: Bottom-left
            if R < n - 1 and C > 0:
                mn = float('inf')
                for i in range(R + 1, n):
                    for j in range(C):
                        mn = min(mn, a[i][j])
                total += mn

            # Section 4: Bottom-right
            if R < n - 1 and C < m - 1:
                mn = float('inf')
                for i in range(R + 1, n):
                    for j in range(C + 1, m):
                        mn = min(mn, a[i][j])
                total += mn

            ans.append(total)

        return ans