def min_jumps(arr):
    n=len(arr)
    if n<=1:
        return 0
    if arr[0]==0:
        return -1
    maxreach=arr[0]
    steps=arr[0]
    jumps=1
    for i in range(1,n):
        if i==n-1:
            return jumps
        maxreach=max(maxreach,i+arr[i])
        steps-=1
        if steps==0:
            jumps+=1
            if i>=maxreach:
                return -1
            steps=maxreach-i
    return -1
arr=[1,4,3,2,6,7]
print(min_jumps(arr))