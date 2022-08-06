word = input()
x = word.split(" ")
x.reverse()
for i in range(len(x)):
    print(x[i], end=" ")
