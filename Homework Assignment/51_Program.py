class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        next_smaller = [n] * n
        stack = []

        # Find next index on right having smaller value
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                next_smaller[i] = stack[-1]

            stack.append(i)

        # Count valid subarrays starting at each index
        ans = 0
        for i in range(n):
            ans += next_smaller[i] - i

        return ans