# age=int(input("Enter your age: "))

# if(age>=18):
#     print("voter")
# else:
#     print("N/A")

a=int(input())
b=int(input())
c=int(input())
if(a<b):
    if(c<a):
        print(c,a,b)
    else:
        if(c<b):
            print(a,c,b)
        else:
            print(a,b,c)
else:
    if(c<b):
        print(c,b,a)
    else:
        if(c<a):
            print(b,c,a)
        else:
            print(b,a,c)