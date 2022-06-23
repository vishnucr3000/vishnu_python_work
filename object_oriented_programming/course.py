# cource id, course name, course fee

class course:
    course_id:int
    course_name=str
    course_fee=float
    def __init__(self,*args):
        self.course_id=args[0]
        self.course_name=args[1]
        self.course_fee=args[2]
    def print_course(self):
        print(self.course_id,self.course_name,self.course_fee)

cls=course(123,'python',500)

cls.print_course()


