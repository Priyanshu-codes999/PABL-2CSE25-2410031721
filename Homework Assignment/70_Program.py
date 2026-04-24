class Solution:
    def countUniqueVowelStrings(self, s):
        vowels = "aeiou"
        freq = {}

        # Count occurrences of vowels present in string
        for ch in s:
            if ch in vowels:
                freq[ch] = freq.get(ch, 0) + 1

        # Number of distinct vowels present
        k = len(freq)

        if k == 0:
            return 0

        # factorial(k)
        fact = 1
        for i in range(2, k + 1):
            fact *= i

        # Multiply by choices of occurrences
        ways = 1
        for count in freq.values():
            ways *= count

        return ways * fact