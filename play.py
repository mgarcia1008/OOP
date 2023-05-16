'''class BankAccount:
    # class attributes
    bank_name = "First National Dojo"
    # new class attribute - a list of all the accounts!
    all_accounts = []
    
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum

checking = BankAccount(.10, 500)
checking.change_bank_name('Bank of America')
print(checking.change_bank_name)'''


'''int_to_float = float(35)
print(int_to_float)
float_to_int = int(44.2)
print(float_to_int)
in_to_complex = complex(35)
print(in_to_complex)

import random
print(random.randint(2,5))'''

# Practice Challenge: Correct the errors!
first_name = "Alana"
last_name = "Da Silva"
age = 36
profession = "Software Developer"
years_experience = 5

greeting = (f"Hello my name is {first_name} {last_name}")

print(greeting) 
# Desired output: Hello my name is Alana Da Silva

print(f"I am {age} years old") 
# Desired output: I am 36 years old

print("I work as a {}.".format(profession))
# Desired output: I work as a Software Developer.

exp_string = ("I have worked in the field for {} years.".format(years_experience))
print(exp_string)
# Desired output: I have worked in the field for 5 years.

print(f"I started in the field when I was {age - years_experience} years old.")
# Desired output: I started in the field when I was 31 years old.

my_string = "This is my string"
upper_string = my_string.upper()
print(upper_string)
