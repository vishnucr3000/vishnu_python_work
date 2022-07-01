
passed_students=open("students.txt")
failed_students=open("failed.txt")
new_file=open("newfile.txt","w")

pstudent=set(passed_students)-set(failed_students)

for stud in pstudent:
    new_file.write(stud)






