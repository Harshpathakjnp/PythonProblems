import classcurrency
class BankAccount:
    def __int__(self):
        self.name = ""
        self.age = ""
        self.bal = classcurrency.Currency(0,0)
        self.account = ""

    def readDetails(self):
        self.name = input("Enter the Name of Account Holder :")
        self.age = int(input("Account Holder Age :"))
        c=classcurrency.Currency(0,0)
        c.readDetail()
        self.bal = c
        self.account = int(input("Enter Account Number :"))

    def __str__(self):
        return "Account Holder = {0},   Account Holder Age = {1}  ,   Balance = {2} , Account No.   =  {3}".format(
            self.name, self.age, self.bal, self.account)

    def deposit(self):
        k = int(input("Enter Account No. to Search :"))
        for detail in li:
            if detail.account == k:
                m = int(input("Enter Amount to Deposit :"))
                if m <= 0:
                    print("You Can't Deposit This Money")
                    continue
                detail.bal += m

    def withdraw(self):
        k = int(input("Enter Account No. to Search :"))
        for detail in li:
            if detail.account == k:
                m = int(input("Enter Amount to Withdraw :"))
                if m >= 0:
                    print("You Can't Withdraw This Money")
                    continue
                detail.bal -= m


li = []
while 1:
    print(
        "0 - Exit\n1 - Open New Account\n2 - Search Account Details by Account NUmber \n3 - Credit Your Account \n4 - Debit Your Account\n5 - View All Account Holders Details ")
    choice = int(input("Enter Your Choice : "))
    if choice == 0:
        print("Thankyou for Choosing Our Bank .. Good Bye ! have a nice day ..")
        break
    elif choice == 1:
        mydetail: BankAccount = BankAccount()
        mydetail.readDetails()
        li.append(mydetail)
    elif choice == 2:
        k = int(input("Enter Account No. to Search :"))
        for detail in li:
            if detail.account == k:
                print(detail)
    elif choice == 3:
        mydetail.deposit()
    elif choice == 4:
        mydetail.withdraw()
    elif choice == 5:
        for i in range(len(li)):
            print(li[i])
