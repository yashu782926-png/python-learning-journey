name=input("Enter your name: ")
expenses=[]
# First expense input
expense_amount=float(input("Enter your expense amount: "))

while expense_amount <= 0:
     print("Please enter a valid expense amount.")
     expense_amount=float(input("Enter your expense amount: "))

expenses.append(expense_amount)
print("Your expense list: ", expenses)
#additional expenses
while True:
    choice=input("Do you want to add more expenses? (yes/no): ")
   
    if choice.lower() == 'yes':
        expense_amount=float(input("Enter your expense amount: "))
       
        while expense_amount <= 0:
           print("Please enter a valid expense amount.")
           expense_amount=float(input("Enter your expense amount: "))

        expenses.append(expense_amount)
        print("Your expense list: ", expenses)

    elif choice.lower() == 'no':
        print("Final expense list: ", expenses)
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
#Expense summary
print("Expense summary for: ", name)
print(expenses)
print("Total expenses: ", sum(expenses))
print("Average expense: ", sum(expenses)/len(expenses))
print("Number of expenses: ", len(expenses))
print("Highest expense: ", max(expenses))
print("Lowest expense: ", min(expenses))