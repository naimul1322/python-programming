# OOPS Part 2 in Python 


# class Student:
#     def __init__(self,name):
#         self.name=name

# s1=Student("naimul")
# del s1
# print(s1.name)

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

a1=Account("1234","@852369")
a1.reset_pass()
        
