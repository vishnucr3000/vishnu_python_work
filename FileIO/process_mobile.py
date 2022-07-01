
fread=open("mobiles.txt")
lst_mob=[]

for line in fread:
    mobile=line.rstrip("\n").split(",")
    lst_mob.append(mobile)

largestprice=max(lst_mob,key=lambda k:int(k[2]))
fifthgen=[]

for mob in lst_mob:
    if mob[-2]=="5g":
        fifthgen.append(mob)

print(largestprice)
print(fifthgen)

