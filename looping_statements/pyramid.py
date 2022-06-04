

num=5


for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,2*i+1):
        print("*",end="")
    print()

num=8

for row in range(1,num+1):
    for col in range(1,num*2):
        if row==num or row+col==num+1 or col-row==num-1:
            print("*",end="")
        else:
            print(end=" ")
    print()
