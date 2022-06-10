lst = [
    [10, 11],
    [13, 45],
    [51, 15],
    [60, 16]
]

# for sub_lst in lst:
#     for num in sub_lst:
#         if num>16:
#             print(max(sub_lst))


# flat_lst = []
# for s_list in lst:
#     for no in s_list:
#         flat_lst.append(no)
# print(max(flat_lst))


flat_lst=[num for slist in lst for num in slist]

print(f"The largest number is {max(flat_lst)}")

print(f"{[num for num in flat_lst if num>16]}")

print(f"{[num for num in flat_lst if num%2!=0]}")

print(f"{sum([num for num in flat_lst if num%2==0]) }")

print(f"Mapped List {[num+1 if num>25 else num-1 for num in flat_lst]}")