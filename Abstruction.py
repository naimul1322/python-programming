# Static Methods in Python 

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.cutch=True
        self.acc=True
        print("car started...")

car1=Car()
car1.start()