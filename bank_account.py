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

            

checking = BankAccount(.10, 500)
savings = BankAccount(.05, 1000)

checking.deposit(100).deposit(200).deposit(500).withdraw(500).yield_interest().display_account_info()
savings.deposit(200).deposit(1000).withdraw(200).withdraw(300).withdraw(500).withdraw(600).yield_interest().display_account_info()

