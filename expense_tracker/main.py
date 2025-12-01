# 3. Expense Tracker (Basic)

# Create a program where the user can:

# Add an expense (amount + category)
# View all expenses
# View total amount spent
# Store data in a list of dictionaries.

# ✅ Task-1: Add validation

# If amount is negative → show error
# If category is empty → show error


# ✅ Task-2: Show total for each category

# Example output:

# food: 350
# travel: 120
# shopping: 500

from datetime import date

lst = []
category_totals = {}

def expense_tracker(n):
    try:

        match n:
            case 1:

                while True:

                    category = input("Enter the category: ")
                    amount = int(input("Enter the amount: "))

                    if category == "":
                        raise ValueError("Category is empty.")
                    
                    if amount > 0:
                        lst.append({"category": category, "amount": amount, "date": date.today()})
                    elif amount < 0:
                        raise ValueError("Amount cannot be negative.")
                    else:
                        print("Invalid input!")

            case 2:

                print("total of each category")

                

                for expense in lst:
                    cat = expense["category"]
                    amt = expense["amount"]

                    if cat in category_totals:
                        category_totals[cat] += amt
                    else:
                        category_totals[cat] = amt
                
                for cat, amt in category_totals.items():
                    print(cat,":",amt)

            case 3:

                print("total expenses till now.")

                total = sum(e["amount"] for e in lst)
                print(total)


            case 4:

                print("delete the expense:")
                # show items with numbers
                for i, (key, value) in enumerate(category_totals.items(), start=1):
                    print(f"{i}. {key} : {value}")
                # take input
                index = int(input("Enter index to delete the expense:"))
                # find actual key
                key_to_delete = list(category_totals.keys())[index - 1]
                # delete it
                del category_totals[key_to_delete]
                # print updated expenses
                print("Updated expenses: ", category_totals)

            case 5:
                print(lst)
                print("Which element you want update: \n1. category\n2. amount\n3. date")
                choice = input("Enter your choice: ")
                update_ex = input("Enter the value: ")

                if choice == "category":
                    category_totals["category"] = [update_ex]
                    print(f"{choice} updated successfully!")

                if choice == "amount":
                    category_totals["amount"] = [update_ex]
                    print(f"{choice} updated successfully!")

                if choice == "date":
                    category_totals["date"] = [update_ex]
                    print(f"{choice} updated successfully!")

                    





    except ValueError as e:
        print("Error:", e)





while True:

    n = int(input("Enter the choice: "))
    expense_tracker(n)