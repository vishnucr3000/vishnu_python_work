

def add(*args):
    return sum(args)
print(add(10,20,30))


def max_func(*mx):
    return max(mx)
print(max_func(10,20,30))


def min_fun(*mn):
    return min(mn)
print(min_fun(10,20,30))


def get_details(**kwargs):
    print(kwargs)

get_details(name="Vishnu",age=30,gender="male",mobile="9495621778")

dic={"n1":10,"n2":20,"n3":30}

print(sum(v for k,v in dic.items()))

print(sum(dic.values()))


