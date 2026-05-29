class ATM:
    def __init__(self):
        self.__pin = 1234
        self.__balance = 0
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, pin, amount):
        if pin == self.__pin:
            if amount <= self.__balance:
                self.__balance-=amount
                print(f"Amount {amount} is withdrawn successfully")
            else:
                print(f"Insufficient Funds.")
        else:
            print(f"Please enter correct pin")
    
    def checkBalance(self):
        print(f"Your balance is : {self.__balance}")

person1 = ATM()
# person1.deposit(500)
# person1.checkBalance()
# person1.withdraw(1234, 300)
# person1.checkBalance()

while True:
    print("-----------------------------\n1. Check balance\n2. Deposite\n3. Withdraw\n4. Exit")
    input_value = input("Please Enter your option : ")
    print("-----------------------------")
    if input_value == "1":
        person1.checkBalance()
    elif input_value == "2":
        deposit_amount = int(input("Enter your deposite amount : "))
        person1.deposit(deposit_amount)
        person1.checkBalance()
    elif input_value == "3":
        atm_pin = int(input("Enter your ATM Pin : "))
        withdraw_amount = int(input("Enter your withdraw amount : "))
        person1.withdraw(atm_pin, withdraw_amount)
        person1.checkBalance()
    elif input_value == "4":
        break