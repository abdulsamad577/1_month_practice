def sort_list(list):
    return sorted(list),sorted(list,reverse=True)
numlist=[1,6,2,9,3,6,2,4,10]
ascend,reverse=sort_list(numlist)
print (ascend)
print(reverse)