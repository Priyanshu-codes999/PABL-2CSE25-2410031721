def subArrSum(arr,k):
    n=len(arr)
    min_length=float('inf')
    current_sum=0
    start=0
    for end in range(n):
        current_sum+=arr[end]
        while current_sum>=k:
            min_length=min(min_length,end-start+1)
            current_sum-=arr[start]   #or current_sum=current_sum-arr[start]
            start+=1  #or start=start+1
            if min_length==float('inf'):
                return 0
    return min_length
arr=[1,4,45,6,0,19]
k=51
print(f"output: {subArrSum(arr,k)}")