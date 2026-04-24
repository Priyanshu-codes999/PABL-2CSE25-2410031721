class Solution:
    def sortByLength(self, arr):
        arr.sort(key=len)   # stable sort keeps same-length order
        return arr