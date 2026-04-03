# practice problem 

class Account:
    def __init__(self,balace,account_no):
        self.balace=balace
        self.account_no=account_no
    
    def debit(self,amount):
        self.balace-=amount
    def credit(self,amount):
        self.balace+=amount
    def print_balace(self):
        print(self.account_no,": Current balace = ",self.balace)


c1=Account(1000,12345)
c1.debit(400)
c1.credit(900)
c1.print_balace()
