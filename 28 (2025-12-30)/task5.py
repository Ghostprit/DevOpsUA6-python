class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount
        return f"The balance of '${self.balance}' has been deposited."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"The amount of '${amount}' has been withdrawn."

    def showBalance(self):
        return f"You have '${self.balance}'."


acc1 = BankAccount(1000, "Peter")
acc2 = BankAccount(2000, "Bob")

print(acc1.showBalance())
print(acc2.showBalance())
print()
print(acc1.deposit(100))
print(acc2.deposit(100))
print()
print(acc1.withdraw(10000))
print(acc2.withdraw(2000))
print()
print(acc1.showBalance())
print(acc2.showBalance())