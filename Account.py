class Account:

    def __init__(self):
        self._customer = None
        self._balance = 0
        self._interest_rate = 0.05

    def get_customer(self):
        return self._customer

    def set_customer(self, customer):
        self._customer = customer

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance

    def get_interest_rate(self):
        return self._interest_rate

    def set_interest_rate(self, rate):
        self._interest_rate = rate

    def add_interest(self):
        self._balance += self._balance * self._interest_rate

    def add_funds(self, amount):
        self._balance += amount

    def close_account(self):
        self._customer = None
        self._balance = 0
