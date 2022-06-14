# print(dir(set))
#
# lst=[1,2,3,4,5,6,6,7,7,8,8,9,9]
# st=set(lst)
# print(st)
# st.add(20)
# print(st)
# st.remove(20)
# print(st)
# st.pop()
# print(st)
#
# st1 = {1, 2, 3, 4, 5, 6}
# st2 = {10, 11, 12, 13, 14}
# st3={100,200,300,400,500}
#
# st1.add(10)
# print(st1)
#
# union_set = st1.union(st2)
# print(union_set)
#
# inter_set = st1.intersection(st2)
# print(inter_set)
#
# diff_set = st1.difference(st2)
# print(diff_set)
#
# st1.update(st3)
# print(st1)


students=["ram","ravi","hari","tom","nikhil","jain","jhon"]
passed_sudents=["ram","ravi","hari","tom"]
failed_students=set(students).__sub__(set(passed_sudents))
print(list[failed_students])


