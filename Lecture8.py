# OOPS in Python 

class Student:

    # # defalut constructors 
    # def __init__(self):
    #     print("adding new student in database...")
    #     pass

    # parameterized constructors
    def __init__(self,name,roll):
        self.name=name
        self.Roll=roll

    # Methods
    def weclome(self):
        print("Welcome is student")


s1=Student("karan ",5)
print(s1.name,s1.Roll)
s1.weclome()

s2=Student("Rakib hasan ",6)
print(s2.name,s2.Roll)


# class Car:
#     color="blue"
#     brand="mercedes"

# c1=Car()
# print(c1.color)
# print(c1.brand)