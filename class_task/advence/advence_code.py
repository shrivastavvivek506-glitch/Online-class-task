import json
import os
from datetime import datetime


class BankAccount:
    FILE_NAME = "bank_data.json"

    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance
        self.__transactions = []

    # Deposit money
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.__balance += amount
        self.__add_transaction("Deposit", amount)

        print(f"₹{amount} deposited successfully!")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if amount > self.__balance:
            raise ValueError("Insufficient balance!")

        self.__balance -= amount
        self.__add_transaction("Withdrawal", amount)

        print(f"₹{amount} withdrawn successfully!")

    # Check balance
    def check_balance(self):
        print(f"Current Balance: ₹{self.__balance:.2f}")

    # Private transaction method
    def __add_transaction(self, transaction_type, amount):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }

        self.__transactions.append(transaction)

    # Transaction history
    def show_transactions(self):
        if not self.__transactions:
            print("No transactions available.")
            return

        print("\n--- Transaction History ---")

        for transaction in self.__transactions:
            print(
                f"{transaction['date']} | "
                f"{transaction['type']} | "
                f"₹{transaction['amount']}"
            )

    # Getter for private balance
    @property
    def balance(self):
        return self.__balance

    # Save account data
    def save_data(self):
        data = {
            "account_holder": self.account_holder,
            "account_number": self.account_number,
            "balance": self.__balance,
            "transactions": self.__transactions
        }

        with open(self.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        print("Account data saved successfully!")

    # Load account data
    @classmethod
    def load_data(cls):
        if os.path.exists(cls.FILE_NAME):
            with open(cls.FILE_NAME, "r") as file:
                data = json.load(file)

            account = cls(
                data["account_holder"],
                data["account_number"],
                data["balance"]
            )

            account.__transactions = data["transactions"]

            return account

        return None


# Main program
def main():

    account = BankAccount.load_data()

    if account is None:
        print("Create New Bank Account")

        name = input("Enter account holder name: ")
        account_number = input("Enter account number: ")

        account = BankAccount(name, account_number)

    while True:

        print("\n========== BANK MANAGEMENT SYSTEM ==========")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Save Account")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

            elif choice == "3":
                account.check_balance()

            elif choice == "4":
                account.show_transactions()

            elif choice == "5":
                account.save_data()

            elif choice == "6":
                account.save_data()
                print("Thank you for using our banking system!")
                break

            else:
                print("Invalid choice! Try again.")

        except ValueError as error:
            print("Error:", error)

        except Exception as error:
            print("Unexpected Error:", error)


if __name__ == "__main__":
    main()