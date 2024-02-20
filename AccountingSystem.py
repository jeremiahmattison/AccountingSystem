# also create a dictionary to store the account names and balances
accounts = {}

# create a function to create a new account
def create_account():
    account_name = input("Enter account name: ")
    initial_balance = float(input("Enter initial balance: "))
    accounts[account_name] = initial_balance

# create a function to record a transaction
def record_transaction():
    debit_account = input("Enter existing debit account name: ")
    credit_account = input("Enter existing credit account name: ")
    amount = float(input("Enter transaction amount: "))
    if debit_account not in accounts:
        print("Error: No debit account found.")
        return
    if credit_account not in accounts:
        print("Error: No credit account found")
        return

    accounts[debit_account] -= amount
    accounts[credit_account] += amount
    
# create a function to view the account balances
def view_balances():
    for account, balance in accounts.items():
        print(f"{account}: {balance}")

# test 
def main():
    create_account()
    create_account()
    record_transaction()
    view_balances()

main()

