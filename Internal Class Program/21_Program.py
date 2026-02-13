def mindiff_chocolates(arr,m):
    n=len(arr)
    if m==0 or n==0:
        return 0
    if m>n:
        return 0
    arr.sort()
    mindiff=float('inf')
    for i in range(n-m+1):
        diff=arr[i+m-1]-arr[i]
        mindiff=min(mindiff,diff)
    return mindiff

#arr=[3,4,1,9,56,7,9,12]
#m=5
#print(f"output: {mindiff_chocolates(arr,m)}")