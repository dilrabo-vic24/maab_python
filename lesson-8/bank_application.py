import json
import os

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} deposited. New balance: {self.balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"{amount} withdrawn. New balance: {self.balance}"
        return "Insufficient funds or invalid amount"

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        if initial_deposit < 0:
            return "Initial deposit must be positive"
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return f"Account created successfully! Account Number: {account_number}"
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return f"Account Number: {account.account_number}\nName: {account.name}\nBalance: {account.balance}"
        return "Account not found"
    
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            message = account.deposit(amount)
            self.save_to_file()
            return message
        return "Account not found"
    
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            message = account.withdraw(amount)
            self.save_to_file()
            return message
        return "Account not found"
    
    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            json.dump({acc_num: vars(acc) for acc_num, acc in self.accounts.items()}, file)
    
    def load_from_file(self):
        if os.path.exists("accounts.txt"):
            with open("accounts.txt", "r") as file:
                data = json.load(file)
                self.accounts = {int(acc_num): Account(**details) for acc_num, details in data.items()}

bank = Bank()

while True:
    print("\n=== BANK SYSTEM ===")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")
    choice = input("Select an option: ")
    
    if choice == "1":
        name = input("Enter your name: ")
        initial_deposit = float(input("Enter initial deposit: "))
        print(bank.create_account(name, initial_deposit))
    elif choice == "2":
        acc_num = int(input("Enter account number: "))
        print(bank.view_account(acc_num))
    elif choice == "3":
        acc_num = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        print(bank.deposit(acc_num, amount))
    elif choice == "4":
        acc_num = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        print(bank.withdraw(acc_num, amount))
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
