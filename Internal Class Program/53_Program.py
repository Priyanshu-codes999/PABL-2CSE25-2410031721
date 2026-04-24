class Solution:
    def maxPeopleSeen(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        prev_ge = [-1] * n          # nearest index on left with value >= arr[i]
        next_ge = [n] * n           # nearest index on right with value >= arr[i]

        stack = []

        # Previous Greater or Equal
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()

            if stack:
                prev_ge[i] = stack[-1]

            stack.append(i)

        stack = []

        # Next Greater or Equal
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()

            if stack:
                next_ge[i] = stack[-1]

            stack.append(i)

        ans = 1

        for i in range(n):
            left_seen = i - prev_ge[i] - 1
            right_seen = next_ge[i] - i - 1

            total = left_seen + right_seen + 1   # include self
            ans = max(ans, total)

        return ans