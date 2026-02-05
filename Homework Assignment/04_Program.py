a=[1,2,3,2,1]
b=[3,2,2,3,3,2]
union=[]
for element in a:
    if element not in union:
        union.append(element)
for element in b:
    if element not in union:
         union.append(element)
print(sorted(union))