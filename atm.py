balance = 10000

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawn:", amount)
    else:
        print("Insufficient balance")

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)

def check_balance():
    print("Current balance:", balance)

while True:
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)
    elif choice == '2':
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)
    elif choice == '3':
        check_balance()
    elif choice == '4':
        break
    else:
        print("Invalid choice")
