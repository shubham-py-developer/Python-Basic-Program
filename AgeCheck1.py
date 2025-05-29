#Ask a user for age & check if they are a child, teenager, or adult.
a=float(input("enter your age here:"))#here child is age group 0-14,teenager14-18,adult 19-above
if a<=14:
    print("you are a child")
elif a<=18:
    print("you are a teenager")
else:
    print("you are an adult")    