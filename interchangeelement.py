li = [1, 2, 3, 4, 5]
length = len(li)
t = li[0]
li[0]= li[length-1]
li[length-1] = t
print(li)

