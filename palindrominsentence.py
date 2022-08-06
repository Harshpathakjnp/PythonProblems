def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    print(str)
    return True






inp = input()
x = inp.split(" ")
for i in range(len(x)):
    ans = isPalindrome(x[i])