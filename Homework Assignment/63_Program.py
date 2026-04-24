from collections import Counter

class Solution:
    def sortByFreq(self, s):
        freq = Counter(s)

        # Sort by frequency ascending, then lexicographically
        chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))

        ans = []

        for ch, count in chars:
            ans.append(ch * count)

        return "".join(ans)