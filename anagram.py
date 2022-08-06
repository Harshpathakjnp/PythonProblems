w = input()
w2 = input()
flag = 1
for i in w2:
    if i not in w:
        print("Not Anagram ")
        flag=0
        break
if flag == 1:
    print("Anagram")

