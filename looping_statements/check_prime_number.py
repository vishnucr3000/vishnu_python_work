
num=8
flag=0
for i in range(2,7):
    if num%i==0:
        flag=1
        break
if flag==0:
    print("Prime Number")
else:
    print("not prime")
