

class Car:
    Brand:str
    Type:str
    Price:float

    def __init__(self,**kwargs):
        self.brand=kwargs.get("Brand")
        self.type=kwargs.get("Type")
        self.price=kwargs.get("Price")

    def __str__(self):
        return self.Brand


BMW=Car(Brand="BMW",Type="Sedan",Price="1 Cr")

print(BMW)