#  Print patter
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

# num=5
# i=0
# for i in range(1,num):
#     for j in range(1,num+1):
#         print(f"{j}",end=" ")
#     print()

# Print Pattern
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

# num = 4
#
# for i in range(1, num + 1):
#     for j in range(1, num):
#         print(f"{i}", end="")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4

# num=4
#
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(f"{j}",end=" ")
#     print()

# 1
# 22
# 333
# 4444

# num=4
#
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(f"{i}",end=" ")
#     print()


#
#  #
#  #  #
#  #  #  #


# num=4
#
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(f"#", end=" ")
#     print()


# # # #
# # #
# #
#

num=4

for i in range(1,num+1):
    for j in range(num+1,i,-1):
        print("#",end="\t")
    print()





