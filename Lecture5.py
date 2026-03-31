# Loops in Python 

# cnt=1
# while cnt<=100:
#     print("hello",cnt)
#     cnt+=1


# i=1
# while i<=100:
#     print(i)
#     i+=1

# n=int(input("Enter your number: "))
# i=1
# while(i<=10):
#     print(n,"X",i ,"= ",n*i )
#     i+=1

#Qs4

# nums=[1,4,9,16,25,36,49,64,81,100]

# idx=0
# while idx<=len(nums)-1:
#     print(nums[idx])
#     idx+=1

nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter serach number: "))
idx=0
ans=-1
while (idx<len(nums)):
    if(nums[idx]==x):
        ans=idx
        break
    idx+=1

print(ans)

