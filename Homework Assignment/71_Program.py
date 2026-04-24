from collections import Counter

class Solution:
    def countEvenLetters(self, s):
        freq = Counter(s)
        count = 0

        for val in freq.values():
            if val % 2 == 0:
                count += 1

        return count