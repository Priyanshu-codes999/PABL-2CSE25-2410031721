def min_height(arr , k):
    arr.sort()
    n=len(arr)
    diff=arr[-1]-arr[0]
    result=diff
    small=arr[0]+k
    big=arr[-1]-k
    if small>big:
        small,big=big,small
    for i in range(1,n):
        subtract=arr[i]-k
        add=arr[i]+k
        new_min=min(small,subtract)
        new_max=max(big,add)
        result=min(result,new_max-new_min)
    return result
arr=[3,9,12,16,20]
k=3
print(min_height(arr,k))