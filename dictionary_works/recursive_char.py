# word count
# text = "hai hello hai hello"
# newtext = text.split(" ")
# t_count = {}
# for word in newtext:
#     if word in t_count:
#         t_count[word] += 1
#     else:
#         t_count[word] = 1
# print(t_count)
#
# # first recursive char
#
# pattern = "ABACCDACC"
# char_dict = {}
#
# for char in pattern:
#     if char in char_dict:
#         print(f"first rec char is {char}")
#         break
#     else:
#         char_dict[char] = 1
#
# # second recursive char
# s_dict = {}
# s_list = []
# for s_char in pattern:
#     if s_char in s_dict:
#         s_list.append(s_char)
#     else:
#         s_dict[s_char] = 1
# print(s_list[1])
#
# # most recursive char
# mrc_dict={}
# mrc_set=set()
# for mrc in pattern:
#     if mrc in mrc_dict:
#         mrc_set.add(mrc)
#     else:
#         mrc_dict[mrc]=1
# mrc_list=list(mrc_set)
# print(mrc_list[-1])
#
#
# # NEW
#
# my_dict={"C":3,"B":2,"A":3}
#
# print(sorted(my_dict.keys()))


