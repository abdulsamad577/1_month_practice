num=input("Enter a number:")
try: 
     num=int(num)
except:
     import winsound
     winsound.Beep(1000,1000)
     print("Yor Entered a Incorrect Number")
     exit()
fact=1
for i in range(1,num+1):
     fact=fact*i
print(f"Factorial of {num} is {fact}")