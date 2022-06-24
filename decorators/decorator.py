

def dec_fun(fn):
    def wrapper(num1,num2):
        if num1<0:
            num1=1
        elif num2<0:
            num2=1
        return fn(num1,num2)
    return wrapper



@dec_fun
def min_num(num1,num2):
    return min(num1,num2)
@dec_fun
def max_num(num1,num2):
    return max(num1,num2)

print(min_num(-5,5))

print(max_num(2,-5))