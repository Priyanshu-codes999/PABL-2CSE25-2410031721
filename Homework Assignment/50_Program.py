class Solution:
    def prevGreater(self, arr):
        stack = []
        ans = []

        for x in arr:
            # Remove elements <= current
            while stack and stack[-1] <= x:
                stack.pop()

            # Top of stack is previous greater
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(-1)

            stack.append(x)

        return ans