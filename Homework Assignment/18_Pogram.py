def is_subset(a, b):
    freq = {}

    # Count frequency of elements in a
    for x in a:
        freq[x] = freq.get(x, 0) + 1

    # Check elements of b
    for x in b:
        if freq.get(x, 0) == 0:
            return False
        freq[x] -= 1

    return True


# Test cases
print(is_subset([11,7,1,13,21,3,7,3],[11,3,7,1,7]))  # True
print(is_subset([1,2,3,4,4,5,6],[1,2,4]))            # True
print(is_subset([10,5,2,23,19],[19,5,3]))            # False
