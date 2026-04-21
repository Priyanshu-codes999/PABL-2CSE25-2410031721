def isPalindrome(num):
    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    return original == rev


def allPalindrome(arr):
    for num in arr:
        if not isPalindrome(num):
            return False
    return True


# Test Cases
print(allPalindrome([111, 222, 333, 444, 555]))   # True
print(allPalindrome([121, 131, 20]))              # False