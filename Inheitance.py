# Inheritance in Python 

class Car:
    @staticmethod
    def start():
        print("car statred..")
    
    @staticmethod
    def stop():
        print("car stopped...")


class Toyotocar(Car):
    def __init__(self,name):
        self.name=name


car1=Toyotocar("fortuner")
car2=Toyotocar("helio")

car1.start()
        