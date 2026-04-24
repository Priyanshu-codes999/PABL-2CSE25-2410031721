class Solution:
    def combinationSum(self, n, k):
        ans = []

        def backtrack(start, remain, path):
            # Valid combination found
            if len(path) == k:
                if remain == 0:
                    ans.append(path[:])
                return

            for num in range(start, 10):
                if num > remain:
                    break

                path.append(num)
                backtrack(num + 1, remain - num, path)
                path.pop()

        backtrack(1, n, [])
        return ans