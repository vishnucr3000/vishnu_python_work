lst1 = [10, 12, 13, 15, 16, 18]
lst2 = [9, 11, 12, 16, 17, 18, 10]

lst1.sort()
lst2.sort()

p1 = 0
p2 = 0

while p1 < len(lst1) and p2 < len(lst2):
    if lst1[p1] == lst2[p2]:
        print(f"Found Common Element {lst1[p1]}")
        p1 += 1
        p2 += 1
    elif lst1[p1] > lst2[p2]:
        p2 += 1
    elif lst1[p1] < lst2[p2]:
        p1 += 1
