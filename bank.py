#Simple Banking System
"""
Project Idea: Develop a basic banking system that allows users to create accounts,
deposit, withdraw, and check balances. Each user account can be an object.
Why It’s Great for Beginners: This project introduces you to the idea of encapsulation,
where you hide the internal details of an object and expose only the necessary methods.
"""

class Account:
    def __init__(self, name):
        self.user = name
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"{amount} deposited.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn.")

    def check(self):
        print(f"You have {self.balance} left.")



def main():

    accounts = {}

    while True:
        print("\n--- BANKING SYSTEM ---")
        print("1. Create an account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter new account name: ")

            if name in accounts:
                print("Account already exists. Please choose another one.")
            else:
                accounts[name] = Account(name)

        elif choice == 2:
            name = input("Enter account name: ")
            amount = int(input("Enter amount to deposit: "))
            accounts[name].deposit(amount)

        elif choice == 3:
            name = input("Enter account name: ")
            amount = int(input("Enter amount to deposit: "))
            accounts[name].withdraw(amount)

        elif choice == 4:
            name = input("Enter account name: ")
            accounts[name].check()

        elif choice == 5:
            print("Thank you for your time. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()








