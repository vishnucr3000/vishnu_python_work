# Multi Level Inheritance

class Car:
    def run(self):
        print("car runnung")

class Sedan(Car):
    def start(self):
        print("seda started")

class My_Car(Sedan):
    def key_inserted(self):
        print("key insterted")

my=My_Car()
my.key_inserted()
my.start()
my.run()


