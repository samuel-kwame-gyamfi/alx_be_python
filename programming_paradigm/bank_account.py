# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the BankAccount with an account balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account balance.

        Returns:
            bool: True if the withdrawal is successful, False otherwise.
        """
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current balance: ${self.__account_balance:.2f}")

