from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))   # sorted letters
        groups[key].append(word)

    return list(groups.values())


# Test Cases
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))