class student:
    s_name: str
    s_roll_no: int
    s_class: str

    def __init__(self, s_name, s_roll_no, s_class):

        #initializing instance variable

        self.s_name = s_name
        self.s_roll_no = s_roll_no
        self.s_class = s_class

    def get_student(self):
        print(f"Student Name is {self.s_name} , Student Roll No is {self.s_roll_no} , Student class is {self.s_class}")


std1 = student("vishnu",1234,"Luminar")

std1.get_student()


# constructor initializing instance variable
# constructor name is always same as java and c++
# constructor name is always __init__


