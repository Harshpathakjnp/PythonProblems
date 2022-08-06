def lastChar(s):
    return s[len(s) - 1]


a = ["cat", "dog", "ball", "apple"]
a.sort(key=lambda x: x[len(x) - 1], reverse=False)  # Sorting by last character and reverse
print(a)
