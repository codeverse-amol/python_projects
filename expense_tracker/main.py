# 3. Expense Tracker (Basic)

# Create a program where the user can:

# Add an expense (amount + category)
# View all expenses
# View total amount spent
# Store data in a list of dictionaries.







import json

from datetime import date

lst = []        # list of dictionaries
category_totals = {}


# -------------------------
# Load expenses at startup
# -------------------------
def load_expenses():
    global lst

    try:
        with open("expenses.json", "r") as f:
            lst = json.load(f)

        print("Loaded expenses from file.\n")
        print(lst)

    except FileNotFoundError:
        print("No existing file found. Starting fresh.\n")


# -------------------------
# Save expenses
# -------------------------

def save_expenses():
    # convert date object → string
    temp = []
    for exp in lst:
        temp.append({
            "category": exp["category"],
            "amount": exp["amount"],
            "date": exp["date"]
        })

    with open("expenses.json", "w") as f:
        json.dump(temp, f, indent=4)

    print("💾 Saved to expenses.json\n")



# -------------------------
# Main Expense Tracker Logic
# -------------------------

def expense_tracker(n):
    try:

        match n:

            # -------------------------
            # 1. Add Expense
            # -------------------------
            case 1:

                while True:

                    category = input("Enter the category: ").strip()
                    amount = int(input("Enter the amount: "))
 
                    if not category:
                        raise ValueError("Category cannot be empty.")
                    
                    if amount > 0:
                        lst.append({"category": category, "amount": amount, "date": date.today().isoformat()})
                   
                    elif amount < 0:
                        raise ValueError("Amount cannot be negative.")
                    else:
                        print("Invalid input!")
                    
                    ask = input("Do you add more expenses? (y/n) ").lower()

                    if ask != "y":
                        break

            # -------------------------
            # 2. Show Total per Category
            # -------------------------
            case 2:
                try:
                    category_totals.clear()

                    for expense in lst:
                        cat = expense["category"]
                        amt = expense["amount"]

                        if cat in category_totals:
                            category_totals[cat] += amt
                        else:
                            category_totals[cat] = amt
                    
                    print(f"{'No':<5}{'Category':<15}{'Total Amount':<15}")
                    print("-" * 35)
                    for index, (cat, amt) in enumerate(category_totals.items(), start=1):
                        print(f"{index:<5}{cat:<15}{amt:<15}")
                    print("-" * 35)


                except ValueError:
                    print("Invalid input!")
                except TypeError:
                    print("Wrong inputs!!")
            # -------------------------
            # 3. Show Total Expense
            # -------------------------
            case 3:

                try:

                    print(f"{'No':<5}{'Category':<15}{'Amount':<10}{'Date'}")
                    print("-" * 40)
                    for i, expense in enumerate(lst, start=1):
                        print(f"{i:<5}{expense['category']:<15}{expense['amount']:<10}{expense['date']}")   
                    print("-" * 40) #-------------------------------------------------  

                    total = 0
                    total = sum(e["amount"] for e in lst)
                    print(f"Total: {total}")

                except ValueError:
                    print("Invalid input!")

                except TypeError:
                    print("Wrong inputs!!")


            # -------------------------
            # 4. Delete Expense
            # -------------------------
            case 4:

                # show items with numbers
                for i, (key, value) in enumerate(category_totals.items(), start=1):
                    print(f"{i}. {key} : {value}")
                # take input
                index = int(input("Enter index to delete the expense:"))
                # find actual key
                key_to_delete = list(category_totals.keys())[index - 1]
                # delete it
                lst.pop(index-1)

                del category_totals[key_to_delete]
                # print updated expenses
                print("Updated expenses: ", category_totals)
                print(lst)


            # -------------------------
            # 5. Update Expense
            # -------------------------
            case 5:
                print("All Expenses:")

                # Show all expenses with indexes
                for i, expense in enumerate(lst, start=1):
                    print(f"{i}. {expense}")

                # Step 1: Ask which dictionary (expense) to update
                index = int(input("\nEnter index of the expense you want to update: "))

                if index < 0 or index > len(lst):
                    print("Invalid index")
                else:
                    d = lst[index-1]     # this is the dictionary to update

                    # Step 2: Ask which field to update
                    print("\nWhat do you want to update?")
                    print("1. category")
                    print("2. amount")
                    print("3. date")

                    choice = input("Enter choice: ")

                    key_map = {
                        "1": "category",
                        "2": "amount",
                        "3": "date"
                    }

                    if choice in key_map:
                        key = key_map[choice]

                        if key == "amount":
                            new_value = int(input(f"Enter new value for '{key}': "))

                        elif key == "date":
                            new_value_raw = input(f"Enter new value for '{key}': ")
                            
                            try:
                                new_value = date.fromisoformat(new_value_raw)
                            except Exception:
                                print("Invalid date format. Use YYYY-MM-DD.")
                        else:     
                            new_value = input(f"Enter new value for '{key}': ")

                        d[key] = new_value   # updates the SAME object inside list

                        print("\nUpdated Successfully")
                        print("Updated expense:", d)
                        print("Updated list:", lst)
                    else:
                        print("Invalid choice.\n")

            # -------------------------
            # 6. Search by category
            # ------------------------
            case 6:

                try:

                    choice = input("enter category: ")
                    matches = [item for item in lst if item["category"] == choice]

                    if matches:
                        for i, item in enumerate(matches, start=1):
                            print(f"{i}. {item["category"]} : {item["amount"]} on {item["date"]}")

                    else:
                        raise KeyError(f"'{choice}' not found in expenses.")

                except ValueError:
                    print("Invalid category!!")
                
                except KeyError as e:
                    print("Error: ", e)


            # -------------------------
            # 7. Filter by date
            # -------------------------
            case 7:

                d = input("Enter a date (YYYY-MM-DD): ")
                    
                result = [item for item in lst if item["date"] == d]
                    
                if result:
                    print(f"Expenses found on {d} are: ")
                    for i, item in enumerate(result, start=1):
                        print(f"{i}. {item["category"]} : {item["amount"]}")
                else:
                    print(f"No expenses found on {d}")              

                


            # -------------------------
            # 8. Save All Expenses
            # -------------------------
            case 8:
                save_expenses()

            # -------------------------
            # 9. Load from File
            # -------------------------
            case 9:
                load_expenses()



            case _:
                print("Invalid choice.\n")


    except ValueError as e:
        print("Error:", e)



# -------------------------
# Program Start
# -------------------------

load_expenses()
print("=================================")
print("----- Expense Tracker-----")
print("=================================")
while True:
    try:
        print("\n<= Main Menu =>\n")
        print("1. Add Expense")
        print("2. Show total per category")
        print("3. Show total expenses")
        print("4. Delete expense")
        print("5. Update expense")
        print("6. Search by category")
        print("7. Filter by date")
        print("8. Save expenses")
        print("9. Load expenses")
        print("=================================")

        n = int(input("Enter choice: "))
        print()
        expense_tracker(n)
        print("-" * 40) #-------------------------------------------------  
    except:
        print("Invalid inputs, try again!!")