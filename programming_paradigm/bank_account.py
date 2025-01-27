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


# Example usage with tests:
if __name__ == "__main__":
    # Create a bank account with an initial balance of $100
    account = BankAccount(100)

    # 1. Test display_balance method
    print("Test 1: Display initial balance (Expected: $100.00)")
    account.display_balance()
    print()

    # 2. Test deposit method
    print("Test 2: Deposit $50 (Expected: Current balance: $150.00)")
    account.deposit(50)
    account.display_balance()
    print()

    # 3. Test withdraw method (successful withdrawal)
    print("Test 3: Withdraw $30 (Expected: Withdrawal successful. Current balance: $120.00)")
    if account.withdraw(30):
        print("Withdrawal successful.")
    else:
        print("Withdrawal failed.")
    account.display_balance()
    print()

    # 4. Test withdraw method (withdraw more than balance)
    print("Test 4: Attempt to withdraw $200 (Expected: Withdrawal failed. Insufficient funds.)")
    if account.withdraw(200):
        print("Withdrawal successful.")
    else:
        print("Withdrawal failed.")
    account.display_balance()
    print()

    # 5. Test display_balance again
    print("Test 5: Display balance (Expected: $120.00)")
    account.display_balance()