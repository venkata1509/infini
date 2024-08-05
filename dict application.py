# Define the contact list dictionary
contacts = {}


# Function to add a contact
def add_contact(name, phone):
    if name in contacts:
        print(f"Contact {name} already exists.")
    else:
        contacts[name] = phone
        print(f"Contact {name} added.")


# Function to remove a contact
def remove_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} removed.")
    else:
        print(f"Contact {name} does not exist.")


# Function to update a contact's phone number
def update_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        print(f"Contact {name} updated.")
    else:
        print(f"Contact {name} does not exist.")


# Function to view all contacts
def view_contacts():
    if contacts:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts available.")


# Main program loop
while True:
    print("\nContact List Menu:")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Update Contact")
    print("4. View Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        add_contact(name, phone)
    elif choice == '2':
        name = input("Enter contact name to remove: ")
        remove_contact(name)
    elif choice == '3':
        name = input("Enter contact name to update: ")
        phone = input("Enter new contact phone number: ")
        update_contact(name, phone)
    elif choice == '4':
        view_contacts()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
