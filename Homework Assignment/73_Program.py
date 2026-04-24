class Solution:
    def shortestSubstring(self, s1, s2):
        need = set(s1)          # required vowels
        freq = {}
        formed = 0
        required = len(need)

        left = 0
        ans = float('inf')

        for right in range(len(s2)):
            ch = s2[right]

            if ch in need:
                freq[ch] = freq.get(ch, 0) + 1
                if freq[ch] == 1:
                    formed += 1

            # Shrink window while valid
            while formed == required:
                ans = min(ans, right - left + 1)

                remove = s2[left]
                if remove in need:
                    freq[remove] -= 1
                    if freq[remove] == 0:
                        formed -= 1

                left += 1

        return ans if ans != float('inf') else -1