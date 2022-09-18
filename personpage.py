class Person:
    def __init__(self):
        self.name = ""
        self.father = ""
        self.mobile = ""
        self.address = " "

    def readperson(self):
        self.name = input("Enter Your Name :")
        self.father = input("Enter Father Name :")
        self.mobile = input("Enter Your Mobile Number :")
        self.address = input("Enter Your Address :")

    def __str__(self):
        return "Name = {0},   Father Name = {1},  Mobile No. = {2},   Address = {3}".format(self.name, self.father,
                                                                                            self.mobile,
                                                                                          self.address)
myper = Person()
myper.readperson()

