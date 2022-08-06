ip = input("Enter Ip Address :")
x = ip.split(".")
flag = 1
for i in range(len(x)):
    y = int(x[i])
    if y > 255 or y < 0 or len(x) > 4:
        print("Not Valid IP")
        flag = 0
        break
if flag == 1:
    print("Valid ip")
