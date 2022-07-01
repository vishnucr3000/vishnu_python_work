

f=open("abc.txt","r",newline="\n")
# f.write("text")
#
# lst=["python","java","php","javascript"]
#
# for lan in lst:
#     # lan=lan+"\n"
#     f.write(lan)

lst=[line for line in f]
print(lst)