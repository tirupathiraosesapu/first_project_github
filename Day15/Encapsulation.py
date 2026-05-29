class Institute:
    def __init__(self, address):
        self.name = "TechU Innovations Pvt Ltd"
        self.address = address
        self._mobile = 1234567890
        self.__bank_account = 987653234567
        self.__atm_pin = 1234
        self.__balance = 1000

    def show_bank_account(self):
        return self.__bank_account

    def balance_change(self, amount):
        self.__balance += amount

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount


i1 = Institute("Hyderabad")
# print(i1.name)
# print(i1.address)
# print(i1._mobile)
# print(i1.__bank_account)
# print(i1.__atm_pin)

i1.name = "Python Full Stack"
i1.address = "Vijayawada"
# i1._mobile = 9876543210
# print(i1.name)
# print(i1.address)
# print(i1._mobile)

# print(i1.show_bank_account())

print(i1.check_balance())
i1.deposit(500)
print(i1.check_balance())
