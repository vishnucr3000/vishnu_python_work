# person={"ram":55,
#         "manu":74,
#         "maya":28,
#         "binu":44}
#
# print(min(person.items(),key=lambda p:p[1]))
#
# print(sorted(person,key= lambda per:per[1],reverse=True))


# results = [
#     {"district":"tvm","win": 98, "A+": 45000},
#     {"district":"ktm","win": 95, "A+": 44000},
#     {"district":"apy","win": 97, "A+": 47000},
#     {"district":"idk","win": 90 ,"A+": 38000},
#     {"district":"ekm","win": 99, "A+": 56000},
#     {"district":"pta","win": 99, "A+": 58000},
#     {"district":"tsr","win": 98, "A+": 57000},
#     {"district":"kzd","win": 99, "A+": 58000},
#     {"district":"pkd","win" :95, "A+": 50000},
#     {"district":"mpm","win": 90,"A+": 4500},
#
# ]
#
#
# print([[res["A+"] for res in results]])


weather = [
    {"district": "tvm", "temp": 30},
    {"district": "ktm", "temp": 28},
    {"district": "apy", "temp": 27},
    {"district": "idk", "temp": 18},
    {"district": "ekm", "temp": 31},
    {"district": "pta", "temp": 21},
    {"district": "tsr", "temp": 24},
    {"district": "kzd", "temp": 29},
    {"district": "pkd", "temp": 34},
    {"district": "mpm", "temp": 31},
    {"district": "tvm", "temp": 31},
    {"district": "ktm", "temp": 29},
    {"district": "apy", "temp": 26},
    {"district": "idk", "temp": 20},
    {"district": "ekm", "temp": 30},
    {"district": "pta", "temp": 22},
    {"district": "tsr", "temp": 27},
    {"district": "kzd", "temp": 28},
    {"district": "pkd", "temp": 30},
    {"district": "mpm", "temp": 29},

]

out={}

for data in weather:
    dist_name=data["district"]
    cur_temp=data["temp"]
    if dist_name in out:
        old_temp=out[dist_name]
        if cur_temp>old_temp:
            out[dist_name]=cur_temp

    else:
        out[dist_name]=cur_temp

print(out)





# sort out based on temparature

sorted_weather=sorted(out.items(),key=lambda item:item[1])
print (sorted_weather)

# find max tem district

max_temp=max(weather,key=lambda tmp:tmp["temp"])
print(max_temp)
# find min tem district

min_temp=min(weather,key=lambda tmp:tmp["temp"])
print(min_temp)

print(dir(dict))

# dictionary methods
