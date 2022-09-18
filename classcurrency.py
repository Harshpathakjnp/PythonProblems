class Currency:

    def readDetail(self):
        rs = int(input("Enter amount in Ruppee :"))
        paisa = int(input("Enter amount in Paise :"))
        self.total = rs * 100 + paisa

    def __init__(self, rs, paisa):
        self.total = rs * 100 + paisa

    def pad0(self, n):  # Add leading 0 to numbers less than 10
        if n < 10:
            return "0{0}".format(n)
        return "{0}".format(n)

    def __str__(self):
        r = self.total // 100
        p = self.total % 100
        if r <= 9:
            r = "0" + str(r)
        if p <= 9:
            p = "0" + str(p)
        return "₹ {0}.{1}".format(r, p);

    def __add__(self, other):  # Implements the + operator
        return Currency(0, self.total + other.total)

    def __sub__(self, other):
        return Currency(0, self.total - other.total)

    def __mul__(self, other):
        return Currency(0, (self.total * other.total) // 100)

    def __lt__(self, other):
        return self.total < other.total

    def __gt__(self, other):
        return self.total > other.total

    def __getitem__(self, item):
        if item == 0:
            return "₹ " + self.pad0(self.total // 100)
        if item == 1:
            return self.pad0(self.total % 100)
        raise IndexError("list index out of range")

    def __len__(self):  # This is for a loop through sequence.We have two items rupees and paise
        return 2

    def __iter__(self):
        self.counter = 0
        return self

    def __getitem__(self, item):
        if item == 0:
            return self.pad0(self.total // 100)
        if item == 1:
            return self.pad0(self.total % 100)
        raise IndexError("list index out of range")

    def __next__(self):  # Returns rupees the first time and paise the next time
        n = self.counter
        if self.counter > 1:
            raise StopIteration
        self.counter += 1
        return self[self.counter - 1]


c1 = Currency(3, 10)
c2 = Currency(2, 50)
# print(c1, c2)
# c = c1 + c2
# print(c)
# sub = c1 - c2
# print(sub)
# print(c1 * c2)
# print(c1 < c2)
# print(c1 > c2)
# print(c1[0])
# print(c1[1])
# print(len(c1))
# for i in range(len(c1)):
#     print(c1[i])
# for c in c1:
#     print(c)
