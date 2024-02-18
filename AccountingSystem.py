# also create a dictionary to store the account names and balances
accounts = {}

# create a function to create a new account
def create_account(account_name, initial_balance):
    accounts[account_name] = initial_balance

# create a function to record a transaction
def record_transaction(debit_account, credit_account, amount):
    if debit_account not in accounts or credit_account not in accounts:
        print("Error: No account found.")
        return
    
# create a function to view the account balances
def view_balances():
    for account, balance in accounts.items():
        print("{account}: {balance}")

# test 
create_account("Cash", 1000)
create_account("Inventory", 500)
record_transaction("Cash", "Inventory", 200)
view_balances()

