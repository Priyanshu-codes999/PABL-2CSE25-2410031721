class Solution:
    def largestString(self, s, k):
        keep = len(s) - k
        stack = []

        for ch in s:
            while stack and k > 0 and stack[-1] < ch:
                stack.pop()
                k -= 1

            stack.append(ch)

        # If deletions still remain, remove from end
        while k > 0:
            stack.pop()
            k -= 1

        return "".join(stack[:keep])