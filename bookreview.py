class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.noofpages = ""
        self.publisher = ""

    def readDetails(self):
        self.title = input("Enter Title :\n")
        self.author = input("Enter Author :\n")
        self.noofpages = int(input("Enter No.of Pages :\n"))
        self.publisher = input("Enter Publisher Name :\n")

    def __str__(self):
        return "Book Name = {0},   Author = {1},  No.of Pages = {2},   Publisher = {3}".format(self.title, self.author,
                                                                                               self.noofpages,
                                                                                               self.publisher)


li = []
while 1:
    print("0 - Exit\n1 - Add Detail\n2 - Search Book by Name\n3 - Search Book by Author\n4 - search Book by Publisher\n")
    t = int(input("Enter Your Choice :"))

    if t == 0:
        break
    elif t == 1:
        mybook = Book()
        mybook.readDetails()
        li.append(mybook)
    elif t == 2:
        k = input("enter book name to open :")
        for book in li:
            if book.title == k:
                print(book)
    elif t == 3:
        k = input("enter Author name to open :")
        for book in li:
            if book.author == k:
                print(book)

    elif t == 4:
        k = input("enter Publisher name to open :")
        for book in li:
            if book.publisher == k:
                print(book)
