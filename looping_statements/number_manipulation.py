

# q1 : input 2 and get output 24  (2+22)
#      input 3 and get output 369 (3+33+333)
#      input 4 and get output 4936 (4+44+444+4444)


num=4
i=1
res=0

while i<=num:
    res=(res*10)+(i*num)
    i+=1
print(res)