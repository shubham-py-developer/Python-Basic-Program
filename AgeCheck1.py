#Ask a user for age & check if they are a child, teenager, or adult.
a=float(input("enter your age here:"))#here child is age group 0-14,teenager14-18,adult 19-above
if a<=14:
    print(f"you are a child beacause your age is {a}!")
elif a<=18:
    print(f"you are a teenagerbeacause your age is {a}!")
else:
    print("you are an adult beacause your age is {a}!")    
