class ATM:
    def __init__(self):
        self.__atm_pin = 1234
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def check_balance(self):
        print(f"Account balance is : {self.__balance}")

    def withdraw(self, atm, amount):
        if atm == self.__atm_pin:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient Funds")
        else:
            print("Invalid PIN")


surya = ATM()
surya.check_balance()
surya.deposit(500)
surya.check_balance()
surya.withdraw(1234, 100)
surya.check_balance()


