from collections import Counter

class Solution:
    def winner(self, arr):
        freq = Counter(arr)

        max_votes = max(freq.values())
        name = min(candidate for candidate, votes in freq.items() if votes == max_votes)

        return [name, str(max_votes)]