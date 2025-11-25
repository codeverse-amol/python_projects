# 2. Simple Contact Book

# Build a command-line contact book that allows the user to:
    # Add a new contact (name, phone)
    # View all contacts
    # Search a contact by name
    # Delete a contact
    # Use a dictionary to store contacts.



# code:
print("\n#---Command-Line Contact Book---#\n")
contacts = {}

def contact_book(n):
    
    match n:
            # Add a new contact (name, phone)
            case 1:
               while True:
                key = input("Add your name: ")
                value = input("Add your phone: ")
                contacts[key]=value
                choice = input("Add more? (y/n): ")
                print("====================")
                if choice.lower() != "y":
                    break


            # View all contacts
            case 2:
                if len(contacts) == 0:
                    print("No contacts found!")
                else:
                    print(contacts)

            # Search a contact by name
            case 3:
                search = input("Enter contacts name:")
                if search in contacts:
                    print(f"Found '{search}': {contacts[search]}")
                else:
                    print(f"{search} is not in contact book!")
            
            # Delete a contact
            case 4:
                del_key = input("Enter conatct name to delete: ")
                if del_key in contacts:
                    del contacts[del_key]
                    print(f"{del_key} deleted successfully!")
                else:
                    print(f"{del_key} not found in contact book.")


        
   

while True:
    try:
        print()
        n = int(input("Enter your choice: "))
        print("====================")
        if n != 0:
            contact_book(n)
        else:
            print("Quitting..")
            break

    except ValueError:
        print("Invalid input, please enter a number!")



