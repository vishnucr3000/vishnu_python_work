

num=[9,39,8,78]
lst1=[]
lst2=[]
result=[]

for n in range(0,len(num)):
    if num[n]<10:
        lst1.append(num[n])
    else:
        lst2.append(num[n])
result.append(sorted(lst1,reverse=True))
result.append(sorted(lst2,reverse=True))

print(result)


