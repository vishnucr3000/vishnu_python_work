# Super Method
# Overiding parent class with access of parent class properties

# Example one
class Parent:
    def properties(self):
        self.props = {"mobile": "Samsung", "Bike": "Bullet"}
        return self.props


class Child(Parent):
    def properties(self):
        props = super().properties()
        props["Car"] = "BMW"
        return props


ch = Child()

print(ch.properties())


# Example Two

class Editor:
    def functionalites(self):
        self.fun = ["create new file", "execute file", "save file"]
        return self.fun


class Pycharm(Editor):
    def functionalites(self):
        fun = super().functionalites()
        fun.append(("version control", "debug"))
        return fun


py = Pycharm()
print(py.functionalites())
