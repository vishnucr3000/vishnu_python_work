import functools
import operator
import inspect




mylist=["A","B","C","D","E","A"]

newlist=["test1","test2"]

intlist=[1,2,3,4]

# print(inspect.)

res=map(lambda a:a+a,intlist)
print(list(res))


print(mylist[::-1])

print(list(enumerate(mylist,2)))

mylist.append((5,6))

mylist.append(newlist)

mylist.insert(0,"vishnu")

mylist.insert(3,"praseena")

mylist.extend(newlist)

mylist.remove("praseena")

print(mylist.count("A"))

print(mylist.copy())

def testfun(a,b):
    return a+b


print(functools.reduce(lambda a,b:a+b,intlist))

print()