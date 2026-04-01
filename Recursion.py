### Recursion in Python 

# def show(n):
#     if(n==0):
#         return
#     print(n,end=" ")
#     show(n-1)
# show(5)



# def fact(n):
#     if(n==0):
#         return 1
#     return n*fact(n-1)
# print(fact(5))



# def fibo(n):
#     if(n==0 or n==1):
#         return n
#     return fibo(n-1)+fibo(n-2)

# print(fibo(6))



# def isprime(n):
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#     return True
# n=int(input("Enter your number: "))
# if(isprime(n)):
#     print("prime")
# else:
#     print("Not Prime")



### sum of all natural number
def cal(n):
    if(n==0):
        return 0
    return cal(n-1)+n

print(cal(5))


### print all elements in a list

def print_list(list,idx):

    if(idx==len(list)):
        return
    print(list[idx],end=" ")
    print_list(list,idx+1)

fruits=["mango","lichi","apple","banana"]
print_list(fruits,0)


