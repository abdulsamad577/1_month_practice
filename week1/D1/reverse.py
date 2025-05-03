num=input("Enter a number:")
try: 
     num=int(num)
except:
     import winsound
     winsound.Beep(1000,1000)
     print("Yor Entered a Incorrect Number")
     exit()

num=str(num)
rev=num[::-1]
new_num=int(rev)
print(f'Reverse Number is: {new_num}')