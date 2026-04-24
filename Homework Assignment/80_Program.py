def compute_z(s):
    n = len(s)
    z = [0] * n
    l = r = 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z


def z_search(text, pattern):
    concat = pattern + "$" + text
    z = compute_z(concat)
    m = len(pattern)

    for i in range(len(z)):
        if z[i] == m:
            print("Pattern found at index:", i - m - 1)


# Example
text = "ababcababc"
pattern = "ababc"
z_search(text, pattern)
