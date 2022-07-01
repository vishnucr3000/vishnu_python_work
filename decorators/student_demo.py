class Student:
    student_name: str
    student_roll_no: int
    student_roll: str

    def post(self, **kwargs):
        self.student_name = kwargs.get("student_name")
        self.student_roll_no = kwargs.get("student_roll_no")
        self.student_roll = kwargs.get("student_roll")

    def __str__(self):
        return self.student_name


student = Student()
student.post(student_name="Vishnu", student_roll_no="1234", student_roll="Admin")


class Course:
    course_name: str
    course_user: Student

    def post(self, **kwargs):
        user = kwargs.get("course_user")
        if user.student_roll == "Admin":
            self.course_name = kwargs.get("course_name")
            print("Course Added")
        else:
            print("User has no privilage")


course = Course()
course.post(course_name="django", course_user=student)


class Batch:
    batch_name: str
    batch_user: Student
    batch_course: Course

    def post(self, **kwargs):
        user = kwargs.get("batch_user")
        if user.student_roll == "Admin":
            self.batch_name = kwargs.get("batch_name")
            self.batch_course = kwargs.get("batch_course")
            print("Batch Added")
        else:
            print("Access Denied")


batch = Batch()
batch.post(batch_name="May", batch_user=student, batch_course=course)
