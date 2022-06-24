# Inheritance Overriding

class Car:
    def run(self):
        print("car runnung")


class Sedan():
    def start(self):
        print("seda started")


class My_Car(Car,Sedan):
    def key_inserted(self):
        print("key insterted")
    # Over riding method from car class
    def run(self):
        print("child driving")
    # Over riding method from Sedan class
    def start(self):
        print("child started car")

my = My_Car()
my.key_inserted()
my.start()
my.run()

