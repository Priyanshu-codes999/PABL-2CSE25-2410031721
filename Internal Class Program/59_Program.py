class Solution:
    def minSwaps(self, s1, s2):
        n = len(s1)

        # Total number of 1s across both strings must be even
        if (s1.count('1') + s2.count('1')) % 2 != 0:
            return -1

        x = 0  # count of mismatches: (1,0)
        y = 0  # count of mismatches: (0,1)

        for i in range(n):
            if s1[i] != s2[i]:
                if s1[i] == '1':
                    x += 1
                else:
                    y += 1

        # If parity differs, impossible
        if x % 2 != y % 2:
            return -1

        # Pairs of same mismatch fixed in one swap
        ans = (x // 2) + (y // 2)

        # One (1,0) and one (0,1) left -> need 2 swaps
        if x % 2 == 1:
            ans += 2

        return ans