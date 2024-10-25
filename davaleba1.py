class BankAccount:
    def __init__(self, account_holder, balance=0, category="Standard"):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute
        self.__category = category  # Private attribute for account category
        self.__withdrawal_limit = self.__set_withdrawal_limit()  # Private method to set withdrawal limit based on category

    def __set_withdrawal_limit(self):
        """Private method to set withdrawal limits based on account category"""
        if self.__category == "Standard":
            return 500
        elif self.__category == "Premium":
            return 1000
        elif self.__category == "Gold":
            return 5000
        else:
            return 300  # Default limit for undefined categories
        
    def get_withdrawal_limit_int(self):
        if self.__category == "Standard":
            return 500
        elif self.__category == "Premium":
            return 1000
        elif self.__category == "Gold":
            return 5000
        else:
            return 300  # Default limit for undefined categories

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} in {self.account_holder}'s account. New balance: {self.__balance}")
        else:
            print(f"{self.account_holder} entered Deposit amount must be positive!")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if 0 < amount <= self.__balance and amount <= self.__withdrawal_limit:
            self.__balance -= amount
            print(f"Withdrew {amount} from {self.account_holder}'s account. New balance: {self.__balance}")
        elif amount > self.__withdrawal_limit:
            print(f"{self.account_holder} you cannot withdraw more than your limit of {self.__withdrawal_limit}!")
        else:
            print(f"{self.account_holder} you have Insufficient balance or you entered invalid amount!")

    def get_balance(self):
        """Check the account balance"""
        return f"The current balance is: {self.__balance}"
    
    def get_balance_int(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.account_holder

    def get_account_info(self):
        """Get account details including category and limits"""
        return f"Account holder: {self.account_holder}, Category: {self.__category}, Withdrawal limit: {self.__withdrawal_limit}"


# Inherited Account Classes
class StandardAccount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance, category="Standard")


class PremiumAccount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance, category="Premium")

    def __set_withdrawal_limit(self):
        """Override to set a higher withdrawal limit for Premium"""
        return 1000  # Custom limit for premium accounts


class GoldAccount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance, category="Gold")

    def __set_withdrawal_limit(self):
        """Override to set an even higher withdrawal limit for Gold"""
        return 5000  # Custom limit for gold accounts


# Card Class
class Card:
    def __init__(self, card_holder, card_type, account):
        self.card_holder = card_holder
        self.card_type = card_type
        self.account = account

    def get_card_info(self):
        """Get information about the card and associated account"""
        return f"Card Holder: {self.card_holder}, Card Type: {self.card_type}, Account Info: {self.account.get_account_info()}"
    
def transfer(sender, reciever, amount):
        if 0 < amount <= sender.get_balance_int() and amount <= sender.get_withdrawal_limit_int():
            sender.withdraw(amount)
            reciever.deposit(amount)
        elif amount > sender.get_withdrawal_limit_int():
            print(f"{sender.get_account_holder()} you Cannot transfer more than your limit of {sender.get_withdrawal_limit_int()}!")
        elif amount <= 0:
            print(f"{sender.get_account_holder()} Transfer amount should be positive!")


# Example usage
elly = StandardAccount("Elly", 1000)
bob = PremiumAccount("Bob", 3000)

transfer(elly, bob, 300)




# # Creating cards for each account
# standard_card = Card("Alice", "Debit", standard_account)
# premium_card = Card("Bob", "Credit", premium_account)


# # Test withdrawals and limits
# standard_account.withdraw(600)  # Exceeds limit
# premium_account.withdraw(700)  # Within limit


# # Check account details
# print(standard_account.get_account_info())
# print(premium_account.get_account_info())


# # Get card details
# print(standard_card.get_card_info())
# print(premium_card.get_card_info())
