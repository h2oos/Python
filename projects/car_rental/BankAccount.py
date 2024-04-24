class BankAccount:
    def __init__(self, new_name, checking_balance, savings_balance):
        self.new_name = new_name
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
        
    def deposit_checking(self, amount):
        if amount > 0:
            self.checking_balance += amount;
            
    def deposit_savings(self, amount):
        if amount > 0:
            self.savings_balance += amount;
            
    def withdraw_checking(self, amount):
        if amount > 0 and amount < self.checking_balance:
            self.checking_balance -= amount;
            
    def withdraw_savings(self, amount):
        if amount > 0 and amount < self.savings_balance:
            self.savings_balance -= amount;
            
    def transfer_to_savings(self, amount):
        if amount > 0 and amount < self.checking_balance:
            self.checking_balance -= amount;
            self.savings_balance += amount;
            
    def __str__(self):
        return f"Name: {self.new_name} Savings Account Balance: {self.savings_balance} Checking Account Balance: {self.checking_balance}" 

if __name__ == "__main__":
    account = BankAccount("Joe Doe", 32000, 12000);
    
    print("Initial Bank Account Details:")
    print(account)
    
    
    account.transfer_to_savings(10000)
    
    print("Current Bank Account Details:")
    print(account)
