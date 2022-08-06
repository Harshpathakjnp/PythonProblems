# Solve a Quadratic Equation :

a = int(input("Enter a\n"))
b = int(input("Enter b\n"))
c = int(input("Enter c\n"))
if a == 0 and b == 0:
    print("No Equation")
elif a == 0:
    print(-c / b)

else:
    x1 = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    print("x1 = ", x1, "x2 = ", x2)
