class Bank:
    def __init__(self, initial_amount = 0.00):
        self.bal = initial_amount

    def transaction_log(self, transaction_string):
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction_string} \t\t\tbal: {self.bal}\n")

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount and amount <= self.bal:
            self.bal = self.bal - amount
            self.transaction_log(f"Withdrew {amount}")
        else:
            print("You do not have enough money in your account.")

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.bal = self.bal + amount
            self.transaction_log(f"Deposited {amount}")


account = Bank(1000)
while True:
    try:
        action = input("\n1. For Withdraw \n2. For Deposit \n3. To Show Balance \n Enter: ")
    except KeyboardInterrupt:
        print("\n\n Bye Bye !!! \n I'm Leaving the ATM\n")
        break

    if action in ["1", "2", "3"]:
        if action == "1":
            amount = input("Enter the amount you want to withdraw: ")
            account.withdraw(amount)
        elif action == "2":
            amount = input("Enter the amount you want to deposit: ")
            account.deposit(amount)
        elif action == "3":
            print("Your balance is", account.bal)
        
        if action == "1" or action == "2":
            print("Your new balance is", account.bal)
    else:
        print("Invalid input. Please try again.")
