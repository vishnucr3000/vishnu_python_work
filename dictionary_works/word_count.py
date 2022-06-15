
text="hai hello hai hello hai"
words=text.split(" ")
w_count={}

for w in words:
    if w in w_count:
        w_count[w]+=1
    else:
        w_count[w]=1
print(w_count)





