a=2345
b=4325
c=a+b

print(" addition of two number is:", c)

#using function
def calc_Sum(a,b,c):#fn definition
    sum=a+b+c
    print(sum)
    return sum
calc_Sum(5,19,897)#fn call
calc_Sum(15,349,897)
calc_Sum(554,19,897)
calc_Sum(5,1923,897)

#or
def calcu_Sum(d,e):
    return d+e  
sum=calcu_Sum(5,80)
print(sum)
sum=calcu_Sum(90,40)
print(sum)
