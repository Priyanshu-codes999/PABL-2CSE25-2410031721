class Solution:
    def find132pattern(self, arr):
        n = len(arr)
        if n < 3:
            return False

        stack = []
        third = float('-inf')   # possible arr[k]

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            
            # If arr[i] < third, pattern found
            if arr[i] < third:
                return True

            # Maintain decreasing stack
            while stack and arr[i] > stack[-1]:
                third = stack.pop()

            stack.append(arr[i])

        return False