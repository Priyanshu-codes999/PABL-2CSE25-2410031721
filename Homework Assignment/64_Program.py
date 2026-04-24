class Solution:
    def sortByLength(self, arr):
        # Python sort is stable, so same-length strings keep original order
        return sorted(arr, key=len)