class Solution:
    def countBalanced(self, arr):
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Prefix difference = vowels - consonants
        prefix = 0
        freq = {0: 1}
        ans = 0

        for word in arr:
            v = 0
            c = 0

            for ch in word:
                if ch in vowels:
                    v += 1
                else:
                    c += 1

            prefix += (v - c)

            # Same prefix means balanced subarray
            ans += freq.get(prefix, 0)
            freq[prefix] = freq.get(prefix, 0) + 1

        return ans