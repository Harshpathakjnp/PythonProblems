def push(stack, data):
    stack.insert(0, data)


def pop(stack):
    return stack.pop(0)


#
def empty(stack):
    return len(stack) == 0


st = []
data = {"a*(a+b)+(b*c)*c"}
n = len(data)

for i in range(n):
    ch = data[i]
    if ch == "(":
        push(st, i)
    if ch == ")":
        out = pop(st)
        part = data[out:i + 1]
        print(part)
# print(st)
while not empty(st):
    print(pop(st))
