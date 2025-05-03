print("Welcome to Multiplication Table Generator")
print("=======================")
x=int(input("\a\a\aNumber: "))
for i in range(1,10+1):
    print(f'{x} x {i} = {i*x}')

import winsound

# Beep at 1000 Hz for 500 milliseconds
winsound.Beep(1000, 1000)
