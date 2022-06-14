mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]

]

# q1 total number of out_of_stock mobiles

# out_of_stock=[stock for stock in mobiles if stock[6]==0]
# print(out_of_stock)

# q2 total stock

# print(sum(t_stock[6] for t_stock in mobiles))


# q3 pritn mobiles available in range 20k to 30k

# print([price if price[4]>20000 and price[4]<30000 else 0 for price in mobiles])

# q4 print all 5g phone

# print([stock for stock in mobiles if stock[2]=="5g"])

# q5 print samsung mobiles

# print([sam for sam in mobiles if sam[5]=="samsung"])
# q6 print costly mobile

costly_prod = max(mobiles, key=lambda m: m[4])
print(costly_prod)

# q7 prin low cost mobiles

# low_cost = min(mobiles, key=lambda m: m[4])
# print(low_cost)

# q8 print all mobiles having stock >10

# print([stock for stock in mobiles if stock[6]>10])

# q9 count of mobiles having dispaly amoled

# lst=[num[0] for num in mobiles if num[3]=="AMOLED"]
# print(len(lst))

# q10 sort mobiles based on price oredr by desc

sort_mobile=sorted(mobiles,reverse=True, key=lambda m:m[4])
print(sort_mobile)

# print(sorted([mob[] for mob in mobiles]))

# q11 sort mobiles based on avl stock oredr by desc

sort_by_stock=sorted(mobiles, reverse=True, key=lambda m:m[-1])
print(sort_by_stock)

# q12 is there any mobile available at rs 10000 ?

# mob_ten=[mob[4]==10000 for mob in mobiles]
# print(f"Available" if True in mob_ten else "Not Available")

# q12 list all mobiles having same price
