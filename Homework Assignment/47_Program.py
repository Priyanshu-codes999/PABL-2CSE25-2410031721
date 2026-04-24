import heapq

class Solution:
    def minOperations(self, arr):
        # Max heap using negative values
        max_heap = [-x for x in arr]
        heapq.heapify(max_heap)

        total = sum(arr)
        target = total / 2.0
        current = total
        operations = 0

        while current > target:
            largest = -heapq.heappop(max_heap)

            half = largest / 2.0
            current -= half

            heapq.heappush(max_heap, -half)
            operations += 1

        return operations