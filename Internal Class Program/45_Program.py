class Solution:
    def sumQuery(self, n, m, a, q, query):
        # Step 1: Build Prefix Sum Matrix
        pre = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                pre[i][j] = a[i][j]

                if i > 0:
                    pre[i][j] += pre[i - 1][j]

                if j > 0:
                    pre[i][j] += pre[i][j - 1]

                if i > 0 and j > 0:
                    pre[i][j] -= pre[i - 1][j - 1]

        # Step 2: Answer Queries
        ans = []

        for k in range(q):
            r1, c1, r2, c2 = query[k]

            total = pre[r2][c2]

            if r1 > 0:
                total -= pre[r1 - 1][c2]

            if c1 > 0:
                total -= pre[r2][c1 - 1]

            if r1 > 0 and c1 > 0:
                total += pre[r1 - 1][c1 - 1]

            ans.append(total)

        return ans