def factorial(n):
    result = [1]
    for x in range(2, n + 1):
        carry =0
        for i in range(len(result)):
           prod=result[i] * x + carry
           result[i] = prod % 10
           carry = prod // 10
        while carry > 0:
            result.append(carry % 10)
            carry //= 10
    return result[::-1]
n=5
print("Factorial of", n, "is:", ''.join(map(str, factorial(n))))
           