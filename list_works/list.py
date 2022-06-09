

# lst=[10,11,11,12,13,14,14,14]
# reslist=[]
#
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]==lst[j]:
#             reslist.append(lst[i])
# print(reslist)

lst=[2,3,4,6]

sum=8

# reslist=[]
# count=1
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j]==sum:
#             reslist.append(lst[i])
#             reslist.append(lst[j])
#         count+=1
# print(reslist)
# print(count)
# print(len(lst))
# print(lst.sort(reverse=True))


# low=0
# upp=len(lst)-1
#
# while(low<upp):
#     total=lst[low]+lst[upp]
#     if total==sum:
#         print(f"Pairs {lst[low]}, {lst[upp]}")
#         break
#     elif total<sum:
#         low+=1
#     elif total>sum:
#         upp+=1

lst=[10,12,13,14,15,16]
lst.sort()
element=18
flag=0
low=0
upp=len(lst)-1
while low<=upp:
    mid=(low+upp)//2
    if element==lst[mid]:
        flag=1
        break
    elif element>lst[mid]:
        low=mid+1
    elif element<lst[mid]:
        upp=mid-1
print(f"Element Found" if flag>0 else "Element not found")





