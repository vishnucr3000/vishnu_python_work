# print first recursive char

pattern="ABACCD"

c_count={}
r_char=[]

# for c in pattern:
#     if c in c_count:
#         print(c_count[c])
#         break
#     else:
#         c_count[c]=c

for c in pattern:
    if c in c_count:
        r_char.append(c)
    else:
        c_count[c]=1
print(r_char[1])

print(c_count)


# wordcount
# first recursive char
# second recursive char
# most recursive char

