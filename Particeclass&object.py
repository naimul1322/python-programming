# creating student class that takes name & marks of 3 subjects as arguments in constructor 
# then create a method to print the average

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    #methods
    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("average of three subject",sum/3)


s1=Student("Milon",[95,93,85.6])
s1.average()
