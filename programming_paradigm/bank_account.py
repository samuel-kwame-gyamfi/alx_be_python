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

# Example usage:
if __name__ == "__main__":
    # Create a bank account with an initial balance of $100
    account = BankAccount(100)

    # Display the initial balance
    account.display_balance()

    # Deposit $50
    account.deposit(50)
    account.display_balance()

    # Withdraw $30
    if account.withdraw(30):
        print("Withdrawal successful.")
    else:
        print("Withdrawal failed.")
    account.display_balance()

    # Attempt to withdraw $200 (should fail)
    if account.withdraw(200):
        print("Withdrawal successful.")
    else:
        print("Withdrawal failed.")
    account.display_balance()
 