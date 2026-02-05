arr =[1,4,3,5,8,6]
minimum =maximum = arr[0]
for num in arr:
    if num < minimum:
        minimum =num
        if num > maximum:
            maximum=num
            print([minimum,maximum])