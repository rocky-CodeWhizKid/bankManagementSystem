class Bank:
    def __init__(self):
        self.accounts = []
        self.bank_balance = 0
        self.loan_feature = True


    def create_account(self, name, initial_deposit):
        account = Account(name, initial_deposit)
        self.accounts.append(account)
        self.bank_balance += initial_deposit
        print(f"Account created for {name} with an initial deposit balance of {initial_deposit}.")


    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
            self.bank_balance += amount
            print(f"Deposited {amount} to account number {account_number}.")
        else:
            print("Account not found!")


    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            if account.balance >= amount:
                account.withdraw(amount)
                self.bank_balance -= amount
                print(f"Withdrew {amount} from account {account_number}.")
            else:
                print("Insufficient funds!")
        else:
            print("Account not found!")


    def transfer(self, sender_account_number, receiver_account_number, amount):
        sender_account = self.find_account(sender_account_number)
        receiver_account = self.find_account(receiver_account_number)
        if sender_account and receiver_account:
            if sender_account.balance >= amount:
                sender_account.withdraw(amount)
                receiver_account.deposit(amount)
                print(f"Transferred {amount} from account {sender_account_number} to account {receiver_account_number}.")
            else:
                print("Insufficient funds!")
        else:
            print("Account not found!")


    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(f"Account balance for {account_number}: {account.balance}")
        else:
            print("Sorry! Account is not found.")


    def check_transaction_details(self, account_number):
        account = self.find_account(account_number)
        if account:
            account.transaction_history()
        else:
            print("Account not found.")


    def loan(self, account_number):
        if self.loan_feature:
            account = self.find_account(account_number)
            if account:
                loan_amount = account.balance * 2
                account.deposit(loan_amount)
                self.bank_balance += loan_amount
                print(f"Loan of {loan_amount} credited to account {account_number}.")
            else:
                print("Account not found.")
        else:
            print("Loan feature is currently inactived")


    def toggle_loan_feature(self):
        self.loan_feature = not self.loan_feature
        if self.loan_feature:
            print("Loan feature avtivated.")
        else:
            print("Loan feature inactived")


    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None



class Account:
    account_counter = 0

    def __init__(self, name, initial_deposit):
        self.account_number = Account.account_counter
        self.name = name
        self.balance = initial_deposit
        self.transactions = []
        Account.account_counter += 1

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}")

    def transaction_history(self):
        print(f"Here is your transaction history  {self.account_number}:")
        for transaction in self.transactions:



class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, initial_deposit):
        self.bank.create_account(name, initial_deposit)

    def check_balance(self):
        print(f"Total bank balance: {self.bank.bank_balance}")

    def loan(self):
        total_loan = 0
        for account in self.bank.accounts:
            total_loan += account.balance
        print(f"Total loan amount: {total_loan}")



bank = Bank()
admin = Admin(bank)


admin.create_account("Rocky", 350)
admin.create_account("Zimmi", 5000)


bank.deposit(0, 850)
bank.deposit(1, 350)

bank.withdraw(0, 300)
bank.withdraw(1, 3000)


admin.check_balance()


