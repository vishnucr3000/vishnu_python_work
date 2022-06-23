# Exercise 1: Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

num={}
ind=0
#Approach one
# for i in keys:
#     num[i]=values[ind]
#     ind+=1

#Approach Two

# num=dict(zip(keys,values))
# print(num)

#Approch Three

# for i in range(len(keys)):
#     num.update({keys[i]:values[i]})
# print(num)

# Exercise 2: Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

res_dict={}

# Approach one
# res_dict.update(dict1)
# res_dict.update(dict2)
#
# print(res_dict)

# Approach 2

# res_dict={**dict1,**dict2}
# print(res_dict)

# Approach 3

# dict1.update(dict2.copy())
# print(dict1)

# Exercise 3: Print the value of key ‘history’ from the below dict

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
#
# print(sampleDict["class"]["student"]["marks"]["history"])

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
#
# res_dic=res_dict.fromkeys(employees,defaults)
# print(res_dic)

# Exercise 5: Create a dictionary by extracting the keys from a given dictionary


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

# Approach one
new_dict={k:sample_dict[k] for k in keys}
print(new_dict)

# Approach two
tdict={}
for k in keys:
    tdict[k]=sample_dict.get(k)
print(tdict)



# Exercise 6: Delete a list of keys from a dictionary

sample = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

# Approach one using for loop

# for k in keys:
#     sample.pop(k)
# print(sample)

# approach two using dictionary comprehension

sample={k:sample[k] for k in sample.keys()-keys}
print(sample)

# Exercise 7: Check if a value exists in a dictionary

s_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in s_dict.values():
    print("value is present in dict")


# Exercise 8: Rename key of a dictionary


# sa_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# sa_dict["location"]=sample_dict.pop("city")
# print(sa_dict)

# Exercise 9: Get the key of a minimum value from the following dictionary

samp_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(samp_dict,key=samp_dict.get))

# Exercise 10: Change value of a key in a nested dictionary

sampl_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

for k,v in sampl_dict['emp3']:
    print(k,v)



