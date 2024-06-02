class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

account = BankAccount("123456789", "Franek Fajny", 1000, "2024-06-01")

account.deposit(500)

account.withdraw(200)

account.check_balance()
