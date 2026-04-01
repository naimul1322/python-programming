# Functions & Recursion in Python

# def sum(a,b):
#     return a+b
# print(sum(3,4))



# cities=["Dhaka","Ctg","Rajshahi","Bogra","Pabna","Khulna"]

# def print_len(list):
#     for item in list:
#         print(item,end=" ")

# print_len(cities)
# print()

# def fact(n):
#     sum=1
#     for i in range(1,n+1,1):
#         sum=sum*i
#     return sum
# n=int(input("Enter your Number: "))
# print(fact(n))

### USD money covert into the Bangladesh money
# def convert(usd):
#     bd=usd*122.64 
#     print("Today Bangladesh currency rate",bd)

# n=float(input("Enter your USD Dollars: "))
# convert(n)

def evenodd(n):
    if(n%2==0):
        print("Even")
    else:
        print("ODD")
n=int(input("Enter your number: "))
evenodd(n)

