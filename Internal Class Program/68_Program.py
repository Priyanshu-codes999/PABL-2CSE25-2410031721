class Solution:
    def isPermutationSubstring(self, txt, pat):
        n = len(txt)
        m = len(pat)

        if m > n:
            return False

        need = [0] * 26
        window = [0] * 26

        # Frequency of pattern
        for ch in pat:
            need[ord(ch) - ord('a')] += 1

        # First window
        for i in range(m):
            window[ord(txt[i]) - ord('a')] += 1

        if window == need:
            return True

        # Sliding window
        for i in range(m, n):
            window[ord(txt[i]) - ord('a')] += 1
            window[ord(txt[i - m]) - ord('a')] -= 1

            if window == need:
                return True

        return False