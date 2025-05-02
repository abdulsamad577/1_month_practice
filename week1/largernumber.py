print("Check a greater number")
print("--------------")
x1=int(input("Enter 1st Number:"))
x2=int(input("Enter 2nd Number:"))
x3=int(input("Enter 3rd Number:"))
print("You Entered:")
print(x1,x2,x3)
a=x1
if x2>a:
    a=x2
elif x3>a:
    a=x3
print(f"Maximum Number is: {a}")
