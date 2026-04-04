# solving problem OOPS in python 


class Cricle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (22/7)*self.radius**2
    def perimeter(self):
        return 2*(22/7)*self.radius

    
c1=Cricle(25.6)
print(c1.area())
print(c1.perimeter())
