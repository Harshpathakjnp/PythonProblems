def push(stack, data):
    stack.insert(0, data)


def pop(stack):
    return stack.pop(0)


def empty(stack):
    return len(stack) == 0


count = 0
count2 = 0
st = []
data = "a*(b+c)+d*(f-g)"
n = len(data)
for i in range(n):
    ch = data[i]
    if ch == "(":
        push(st, i)
        count = count + 1
    if ch == ")":
        count2 = count2 + 1

# print(st)

if count == count2:
    print("Sahi hai")
else:
    print("Galat hai")
