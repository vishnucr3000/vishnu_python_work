

# cars=["BMW","Benz","Ferrari","Ducati","Honda","Maruthi"]
#
# for car in cars:
#     print(car)
#
# for i in range (0,len(cars)):
#     print(cars[i])

numbers=[12,13,14,15,16,17,18]

# for num in numbers:
#     if num%2==0:
#         print(num)
#


# for num in numbers:
#     if num<15:
#         print(num-1)
#     elif num>15:
#         print(num+1)
#     else:
#         print(num)

# count=0
# for num in numbers:
#     if num>=14 and num<=18:
#         count+=1
# print(count)

number=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]

pcount=0
ncount=0
zcount=0
for num in number:
    if num<0:
        ncount+=1
    elif num>0:
        pcount+=1
    else:
        zcount+=1
print(f"postive count is {pcount}, Negetive Count is {ncount}, zero count is {zcount}")

print(f" positve 0{len([n for n in number if n>0])}")


# print(sum(number))



