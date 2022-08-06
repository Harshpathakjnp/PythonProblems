def push(stack, data):
    stack.insert(0, data)


def pop(stack):
    return stack.pop(0)


#
def empty(stack):
    return len(stack) == 0





st = []
st2 = []
data = "1234567"
n = len(data)
for i in range(n):
    ch = data[i]
    (push(st, ch))

for i in range(n):
    ch = pop(st[i])

    push(st2,ch)
# print(st)
while not empty(st):
    print(pop(st))
    print(pop(st2))
