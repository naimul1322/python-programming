# File input / output in Python

# f=open("demo.txt","a")
# f.write("I want to learn javascript")
# f.close()


# f=open("sample.txt","w")
# f.write("Hello bangladesh programing is good for human and student i want to learn bangldesh programming")
# f.close()

# f=open("sample.txt","r+")
# f.write("\nabcdgmgodmgm")
# f.close()


# import os
# os.remove("sample.txt")


# f=open("practice.txt","r")
# f.write("Hi everyone/we are learning file input/output/ni using java./nI like programming in java.")
# data=f.read()
# new_data=data.replace("java","python")
# f=open("practice.txt","w")
# f.write("new_data")
# f.close()

# word="learning"
# with open("practice.txt","r") as f:
#     data=f.read()
#     if(data.find(word)!=-1):
#         print("found")
#     else:
#         print("not found")

def check_for_line():
    word="not"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return 
            line_no+=1
    
    return -1
check_for_line()




