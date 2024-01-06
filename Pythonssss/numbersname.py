def numberprint(b):
    if b >= 20 and b < 30:
        print("twenty", end=' ')
        numberprint(b % 20)
    elif b >= 30 and b < 40:
        print("thirty", end=' ')
        numberprint(b % 30)
    elif b >= 40 and b < 50:
        print("forty", end=' ')
        numberprint(b % 40)
    elif b >= 50 and b < 60:
        print("fifty", end=' ')
        numberprint(b % 50)
    elif b >= 60 and b < 70:
        print("sixty", end=' ')
        numberprint(b % 60)
    elif b >= 70 and b < 80:
        print("seventy", end=' ')
        numberprint(b % 70)
    elif b >= 80 and b < 90:
        print("eighty", end=' ')
        numberprint(b % 80)
    elif b >= 90 and b < 100:
        print("ninety", end=' ')
        numberprint(b % 90)
    elif b == 10:
        print("ten", end=' ')
    elif b == 11:
        print("eleven", end=' ')
    elif b == 12:
        print("twelve", end=' ')
    elif b == 13:
        print("thirteen", end=' ')
    elif b == 14:
        print("fourteen", end=' ')
    elif b == 15:
        print("fifteen", end=' ')
    elif b == 16:
        print("sixteen", end=' ')
    elif b == 17:
        print("seventeen", end=' ')
    elif b == 18:
        print("eighteen", end=' ')
    elif b == 19:
        print("nineteen", end=' ')
    elif b == 1:
        print("one", end=' ')
    elif b == 2:
        print("two", end=' ')
    elif b == 3:
        print("three", end=' ')
    elif b == 4:
        print("four", end=' ')
    elif b == 5:
        print("five", end=' ')
    elif b == 6:
        print("six", end=' ')
    elif b == 7:
        print("seven", end=' ')
    elif b == 8:
        print("eight", end=' ')
    elif b == 9:
        print("nine", end=' ')
