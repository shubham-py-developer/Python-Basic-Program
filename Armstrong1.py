#write a program to find Armstrong number
num=int(input("enter the number:"))
orig=num
power=len(str(num))
i=0
while num>0:
    digit=num%10
    i+=digit**power
    num=num//10# or num//=10
if i==orig:
    print("armstrong no.")
else:   
    print("not an armstrong  no:")
    
    #using fn, Armstrong Number identification
def Is_Armstrong(num):
    temp=num
    power=len(str(num))
    i=0
    while temp>0:
        digit=temp%10
        i+=digit**power
        temp//=10
    if i==num:
        return True
    else:
        return False
num1=int(input("enter a number:"))
if Is_Armstrong(num1):
    print(f"{num1} is an Armstrong no.")
else:
    print(f"{num1} is not an Armstrong no.")
    
    #using fn, Armstrong Number identification
def Is_Armstrong(num):
    temp=num
    power=len(str(num))
    i=0
    while temp>0:
        digit=temp%10
        i+=digit**power
        temp//=10
    if i==num:
        print(f"{num1} is an Armstrong no.")
    else:
        print(f"{num1} is not an Armstrong no.")
num1=int(input("enter a number:"))
Is_Armstrong(num1)
num2=int(input("enter a number:"))
Is_Armstrong(num2)