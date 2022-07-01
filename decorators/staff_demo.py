class Employee:
    emp_id: int
    emp_name: str
    emp_role: str

    def __init__(self, **kwargs):
        self.emp_id = kwargs.get("emp_id")
        self.emp_name = kwargs.get("emp_name")
        self.emp_role = kwargs.get("emp_role")

    def __str__(self):
        return self.emp_name


emp = Employee(emp_id=1234, emp_name="Vishnu", emp_role="HR")


class Department:
    dep_name: str
    dep_user: str

    def __init__(self, **kwargs):

        user = kwargs.get("dep_user")

        u_role = user.emp_role
        if u_role == "Admin":
            self.dep_name = kwargs.get("dep_name")
            self.dep_user = kwargs.get("dep_user")
        else:
            print("Admin previlage required")

    def __str__(self):
        return self.dep_name


new_dep = Department(dep_name="IT", dep_user=emp)

print(emp)
print(new_dep)
