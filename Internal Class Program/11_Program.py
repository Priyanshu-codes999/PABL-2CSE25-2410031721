import heapq
def kth_smallest_minheap(arr, k):
    heapq.heapify(arr)
    for _ in range(k-1):
        heapq.heappop(arr)
    return heapq.heappop(arr)
arr =[10,5,4,3,48,6,2,33,53,10]
k=4