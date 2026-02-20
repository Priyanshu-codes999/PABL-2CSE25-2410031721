def is_pal(num):
    rev = 0
    temp = num
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    return rev == num

def all_palindrome(arr):
    for num in arr:
        if not is_pal(num):
            return False
    return True

print(all_palindrome([111, 222, 333, 444, 555]))  
print(all_palindrome([121, 131, 20]))             
