
text="There is a program, that is calculate is the that frequency of words."
# print(text.split())
words=text.split()
# print (words)

count={}
for word in words: 
    # print (word)
    count[word]=count.get(word,0)+1
# print(count)

print(max(count,key=count.get))
print(count[max(count,key=count.get)])
