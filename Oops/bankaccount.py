class BankAccount:
    customer = 0
    def __init__(self, accNum, accBalance, accType, dateOpend):
        self.accNumber = accNum
        self.accBalance = accBalance
        self.accType = accType
        self.dateOpened = dateOpend
        BankAccount.customer += 1

    def open(self):
        print("Account is opened !!!")

    def close(self):
        print("Account is closed !!!")

    def deposit(self):
        print("Amount is deposited !!!")

    def withdrawl(self):
        print("Amount is withdrawn !!!")

    def ministatement(self):
        print("Showing account balance:")
        print(self.accBalance)
        return (self.accBalance)

Laxmi = BankAccount("SBI000", 35000, "Savings", "15/02/2015")
Hemu = BankAccount("SBI123", 25000, "Savings", "15/02/2012")
Dinesh = BankAccount("SBI456", 15000, "Savings", "15/02/2010")
Prakash= BankAccount("SBI789", 5000, "Savings", "15/02/2008")
Hemu.open()
print("Total Number of CUstomers in Bank",BankAccount.customer)
print("Prakash", Prakash.ministatement())
#del(Prakash.accBalance)
#print("Prakash", Prakash.ministatement())
