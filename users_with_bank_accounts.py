class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if amount > self.balance:
          print("Insufficient funds: Charging a $5 fee")
          self.balance - 5
        else: 
            self.balance -= amount
        return self 

    def display_account_info(self):
        print(f"Inerest rate:{self.int_rate}, Current Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance >= 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount) #using deposit which is calling deposit from line 7
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount) #using withdraw which is calling withdraw from line
        return self 
    
    def display_user_balance(self):
        print(f"Current Balance: {self.account.balance}")
        return self

mindi = User("Mindi Garcia", "mgarcia410@yahoo.com")
peter = User("Peter Smith", "psmith@aol.com")

mindi.make_deposit(500).make_withdrawal(50).display_user_balance()
peter.make_deposit(5000).make_withdrawal(1000).display_user_balance()





