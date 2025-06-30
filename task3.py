contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Contact for {name} added.\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\n--- Contact List ---")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("--------------------------")

def search_contact():
    search_name = input("Enter name to search: ")
    if search_name in contacts:
        info = contacts[search_name]
        print(f"\nFound contact for {search_name}:")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"Address: {info['address']}\n")
    else:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter the name to update: ")
    if name in contacts:
        print("Leave blank to keep current value.")
        phone = input(f"New phone (current: {contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"New email (current: {contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"New address (current: {contacts[name]['address']}): ") or contacts[name]['address']
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print(f"{name}'s contact updated.\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted.\n")
    else:
        print("Contact not found.\n")

def contact_book():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

contact_book()