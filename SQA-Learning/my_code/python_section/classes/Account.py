import random


class Account:
    def __init__(self, user_id, currency='USD'):
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_database()
        print(f'Current balance is: {self.current_balance} {currency}')

    def withdraw(self, amount):
        if self.current_balance - float(amount) < 0:
            print(f"Yo can't made withdraw you the current balance not enough")
        else:
            self.current_balance = self.current_balance - float(amount)
            print(f'New balance after withdraw: {self.current_balance}')

    def deposit(self, amount):
        self.current_balance = self.current_balance + float(amount)
        print(f'New balance after deposit {self.current_balance}')

    def generate_statement(self, start_date, end_date):
        pass

    def __read_balance_from_database(self):
        print(f'Getting balance from db for: {self.user_id}')
        return random.randint(100, 10000)


account1 = Account(987, 'EUR')
account1.deposit(100)
account1.withdraw(150)
