class Bank:
    def __init__(self):
        self.user=None
        self.users = {}
        self.loan_feature_enabled = True
        self.admin = None
        self.total_bank_balance = 0
        self.total_loan = 0

    def create_account_for_user(self, username, initial_balance=0):
        if username not in self.users:
            user = User(self, username, initial_balance)
            self.users[username] = user
            self.total_bank_balance += initial_balance
            user.transaction_history.append(initial_balance)
            print(f'Welcome to created Account in this Bank. Account name is: {username}')
        else:
            print(f'Account name {username} already exists in this bank')

    def create_admin_account(self, admin_name):
        if not self.admin:
            self.admin = Admin(self, admin_name)
            print(f'Account created for admin: {admin_name}')
        else:
            print(f'Admin account is already exists in this bank')


class User(Bank):
    def __init__(self, bank, username, balance=0) -> None:
        self.bank = bank
        self.username = username
        self.balance = balance
        self.user_loan_amount = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.bank.total_bank_balance += amount
        self.transaction_history.append(f'Deposit {amount}')


    def withdraw(self, amount):
        if amount > self.balance:
            print(f'You are not eligible for withdraw, The bank is Bankrupt')
        else:
            self.balance -= amount
            self.bank.total_bank_balance -= amount
            self.transaction_history.append(f'Withdraw amount is:{amount}')


    def take_loan(self):
        if self.user_loan_amount == 0 and self.bank.loan_feature_enabled:
            loan_amount = 2 * self.balance
            self.user_loan_amount += loan_amount
            self.bank.total_bank_balance -= loan_amount
            self.bank.total_loan += loan_amount
            self.transaction_history.append(f'Take a loan: {self.user_loan_amount}')
        else:
            print(f'You are not eligible for a loan')

    def transfer_money(self, amount, receive_username):
        if amount <= 0:
            print("Invalid transfer amount, You don't have enough money")
           
        if receive_username in self.bank.users:
            receive = self.bank.users[receive_username]

            if amount <= self.balance:
                self.balance -= amount
                receive.balance += amount
                self.transaction_history.append(f'transfer {amount} to {receive_username}')
                receive.transaction_history.append(f'Receive {amount} from {self.username}')
                print(f'Transfer successful of this account : {amount} to {receive_username}')
            else:
                print("You are not eligable for transfer money")
        else:
            print(f"receiver account {receive_username} does not exist.")

    def account_detail_for_user(self):
        print(f'Account details for {self.username} BELO:--')
        print(f'Balance: {self.balance}')
        print(f'Loan Amount: {self.user_loan_amount}')
        print(f'Transaction History: {self.transaction_history}')


class Admin(Bank):
    def __init__(self, bank, admin_name) -> None:
        self.bank = bank
        self.admin_name = admin_name

    def check_total_bank_details(self):
        print(f'Total available balance of the BANK BELO:--')
        print(f'Total bank balance is: {self.bank.total_bank_balance}')
        print(f'Total loan amount is: {self.bank.total_loan}')
        if self.bank.total_loan > self.bank.total_bank_balance:
            self.bank.loan_feature_enabled = False
            print('Loan feature is OFF')
        else:
            print('Loan feature is ON')

    def loan_feature_of_the_bank(self):
        if self.bank.total_bank_balance < self.bank.total_loan:
            self.bank.loan_feature_enabled = False
            print('Loan feature is OFF, you cannot take a loan')
        else:
            self.bank.loan_feature_enabled = True
            print('Loan feature is ON, Please wait:-')


bank = Bank()
bank.create_account_for_user('Rakib', 1000)
bank.create_account_for_user('Rehan', 500)
bank.create_account_for_user('Sohan', 4000)
bank.create_admin_account('MD.Hassan')
bank.users['Rehan'].take_loan()
bank.users['Rakib'].transfer_money(200, 'Bob')
bank.users['Rehan'].withdraw(1000)
bank.users['Sohan'].account_detail_for_user()
bank.users['Rehan'].account_detail_for_user()
bank.users['Rakib'].account_detail_for_user()
bank.admin.check_total_bank_details()
