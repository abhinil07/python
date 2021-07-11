import pandas as pd
import numpy as np
class SavingAccount:
    def __init__(self, rate, balance):
        self.annual_inter_rate = rate
        self.saving_balance = balance

    def MonthlyInterest(self):
        self.interest = (self.annual_inter_rate * self.saving_balance)/(12*100)
        print("Monthly Interest is",str(self.interest))
        self.saving_balance += self.interest
        print("total saving balance is",str(self.saving_balance))

    def Modify_interest_rate(self, new_rate):
        self.annual_inter_rate = new_rate
p1 = SavingAccount(5, 2000)
p2 = SavingAccount(5, 3000)
print(f"New balance for p1: {p1.saving_balance}")
print(f"New balance for p2: {p2.saving_balance}")
p1.MonthlyInterest()
p2.MonthlyInterest()
p1.Modify_interest_rate(7)
p2.Modify_interest_rate(7)
p1.MonthlyInterest()
p2.MonthlyInterest()
print(f"New balance for p1: {p1.saving_balance}")
print(f"New balance for p2: {p2.saving_balance}")
