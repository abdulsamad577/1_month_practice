num=input("Enter a number:")
try: 
     num=int(num)
except:
     import winsound
     winsound.Beep(1000,1000)
     print("Yor Entered a Incorrect Number")
     exit()
if num<=1:
    print("Please Enter more than 1 number")
    import winsound
    winsound.Beep(1000,1000)
else:
    for i in range(2,num):
        if num%i==0:
            print("Its not a prime!")
            break
    else:
            print("Its a prime!")
