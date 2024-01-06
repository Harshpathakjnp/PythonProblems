def ones(n):
    if n == 0:
        return ""
    elif n == 1:
        return "One"
    elif n == 2:
        return "Two"
    elif n == 3:
        return "Three"
    elif n == 4:
        return "Four"
    elif n == 5:
        return "Five"
    elif n == 6:
        return "Six"
    elif n == 7:
        return "Seven"
    elif n == 8:
        return "Eight"
    elif n == 9:
        return "Nine"


def tens(n):
    if n < 10:
        return ones(n)
    a = n // 10
    b = n % 10
    if n == 10:
        return "Ten"
    elif n == 11:
        return "Eleven"
    elif n == 12:
        return "Twelve"
    elif n == 13:
        return "Thirteen"
    elif n == 14:
        return "Fourteen"
    elif n == 15:
        return "Fifteen"
    elif n == 16:
        return "Sixteen"
    elif n == 17:
        return "Seventeen"
    elif n == 18:
        return "Eighteen "
    elif n == 19:
        return "Nineteen "
    elif a == 2:
        return "Twenty " + ones(b)
    elif a == 3:
        return "Thirty " + ones(b)
    elif a == 4:
        return "Forty " + ones(b)
    elif a == 5:
        return "Fifty " + ones(b)
    elif a == 6:
        return "Sixty " + ones(b)
    elif a == 7:
        return "Seventy " + ones(b)
    elif a == 8:
        return "Eighty " + ones(b)
    elif a == 9:
        return "Ninety " + ones(b)


def hundreds(n):
    if n < 100:
        return tens(n)
    a = n // 100
    b = n % 100
    return ones(a) + " Hundred " + tens(b)


def thousands(n):
    if n < 1000:
        return hundreds(n)
    a = n // 1000
    b = n % 1000
    if a > 9:
        return tens(a) + " Thousand " + hundreds(b)
    return ones(a) + " Thousand " + hundreds(b)


def lakhs(n):
    if n < 100000:
        return thousands(n)
    a = n // 100000
    b = n % 100000
    if a > 9:
        return tens(a) + " Lakh " + thousands(b)
    return ones(a) + " Lakh " + thousands(b)


n = 123456
print(lakhs(n))
