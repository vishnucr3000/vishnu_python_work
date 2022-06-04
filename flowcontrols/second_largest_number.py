
num1=200
num2=500
num3=100

largest=0
smallest=0

# Find Largest No

if num1>num2 and num1>num3:
    largest=num1
elif num2>num1 and num2>num3:
    largest=num2
elif num3>num1 and num3>num2:
    largest=num3


# Find Smallest Number
if num1<num2 and num1<num3:
    smallest=num1
elif num2<num1 and num2<num3:
    smallest=num2
elif num3<num1 and num3<num2:
    smallest=num3

res=(num1+num2+num3)-(largest+smallest)
print(f"{res} is the second largest number")







