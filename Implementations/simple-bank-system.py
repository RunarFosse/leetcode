class Bank:

    def __init__(self, balance: List[int]):
        self.balance, self.n = balance, len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Only transfer if both accounts are valid for their given operations
        if not (self._isValid(account1, money) and self._isValid(account2)):
            return False
        
        # Withdraw from one account, deposit into the other
        self.withdraw(account1, money)
        self.deposit(account2, money)
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._isValid(account):
            return False
        
        # Deposit money into the account
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._isValid(account, money):
            return False
        
        # Withdraw money from the account
        self.balance[account - 1] -= money
        return True
        
    def _isValid(self, account: int, money: int = 0) -> bool:
        # Check if an action on a given account is valid
        return 0 < account <= self.n and money <= self.balance[account - 1]


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)