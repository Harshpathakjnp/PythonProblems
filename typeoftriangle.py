a = int(input("Enter length of First Side :"))
b = int(input("Enter length of Second Side :"))
c = int(input("Enter length of Third Side :"))
if a + b >= c and a + c >= b and b + c >= a:
    if a == b and b == c:
        print("Equilateral Triangle :")
    elif a == b or b == c or c == a:
        print("Isoceles Triangle :")
    else:
        print("Scalene Triangle :")
else:
    print("No Triangle :")
