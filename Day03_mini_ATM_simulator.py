print("WELCOME TO MINI ATM")
name = input("Enter your name: ")
print(f"Hello, {name}!")
bank=input("Enter your bank name: ")
print(f"Welcome to {bank} bank.")
bank_balance = 5000
print(f"Your starting balance is: Rs.{bank_balance}")
print("ATM Menu:")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
choice = input("Enter your choice (1/2/3): ")

if choice == '1':

    print(f"Your current balance is: Rs.{bank_balance}")

elif choice == '2':
    deposit_amount = float(input("Enter the amount to deposit: Rs."))

    if deposit_amount <= 0:
        print("Invalid amount. Please enter a positive value.")
    else:
        bank_balance += deposit_amount
        print(f"Amount deposited successfully. Your new balance is: Rs.{bank_balance}")


elif choice == '3':
    withdraw_amount = float(input("Enter the amount to withdraw: Rs."))
    if withdraw_amount <= 0:
        print("Invalid amount. Please enter a positive value.")
    elif withdraw_amount > bank_balance:
        print("Insufficient funds.")
    else:
       bank_balance -= withdraw_amount
       print(f"Amount withdrawn successfully. Your new balance is: Rs.{bank_balance}")
    
else:
    print("Invalid choice. Please select a valid option from the menu.")

    
          