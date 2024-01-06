from numbersname import numberprint
n = 1234
if n >= 1000000:
    b = n // 1000000
    n = n % 1000000
    numberprint(b)
    print("million", end=' ')
if n >= 100000:
    b = n // 100000
    n = n % 100000
    numberprint(b)
    print("lakh", end=' ')
if n >= 1000:
    b = n // 1000
    n = n % 1000
    numberprint(b)
    print("thousand", end=' ')
if n >= 100:
    b = n // 100
    n = n % 100
    numberprint(b)
    print("hundred", end=' ')
if n > 20:
    numberprint(n)
if n < 20:
    numberprint(n)
if n == 0:
    print('Zero')