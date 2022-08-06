li = [1, 2, 3, 4, 5,-1,-2,0]
length = len(li)
poscount =0
negcount=0
for i in li:
    if i>0:
        poscount+=1
    elif i<0:
        negcount+=1
print(f"Positive No. are {poscount} and Negative No. are {negcount}")

