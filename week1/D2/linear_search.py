
x=[1,2,3,4,5,10,20,30]


search=int(input("Which number you want to find? \n Enter here: "))
def linear_search(list,num):
    for i in range(len(list)):
        if list[i]==num:
            return i
    return -1
if linear_search(x,search)==-1:
    import winsound
    winsound.Beep(1000,1000)
    print(f"{search} is not found in list")
else:
    print(f"{search} is located at index:",linear_search(x,search))