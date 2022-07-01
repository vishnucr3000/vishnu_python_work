class Course:
    course_name :str
    course_status : bool

    def post(self, **kwargs):
        self.course_name = kwargs.get("course_name")
        self.course_status = kwargs.get("status")
        # print("Course Added")

    def __str__(self):
        return self.course_name




class Batch:
    batch_name: str
    batch_course: Course
    batch_code: int
    batch_date: str

    def post(self, **kwargs):
        self.batch_name = kwargs.get("batch_name")
        self.batch_course = kwargs.get("course")
        self.batch_code = kwargs.get("batch_code")
        self.batch_date = kwargs.get("batch_date")
        # print("Batch Added")

    def __str__(self):
        return self.batch_code




class Student:
    student_name:str
    gender:str
    rollno:int
    student_batch:Batch

    def post(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.gender=kwargs.get("gender")
        self.rollno=kwargs.get("rollno")
        self.student_batch=kwargs.get("student_batch")

    def __str__(self):
        return self.student_name


django = Course()
django.post(course_name="django", status=True)
bigdata = Course()
bigdata.post(course_name="big Data", status=True)

djangobatch = Batch()
djangobatch.post(batch_name="May", batch_code="2022D", batch_date="01-05-2022", course=django)
# print(djangobatch)

bigdatabatch = Batch()
bigdatabatch.post(batch_name="May", batch_code="2022B", batch_date="05-05-2022", course=bigdata)
# print(bigdatabatch)

vishnu=Student()
vishnu.post(student_name="Vishnu",gender="Male",rollno="1244",student_batch=djangobatch)
# print(vishnu)

athira=Student()
athira.post(student_name="Athira",gender="Female",rollno="1234",student_batch=djangobatch)

print(athira.student_batch.batch_course.course_name)


# num=[9,39,8,78]


# masterstring=

# checkstring=



