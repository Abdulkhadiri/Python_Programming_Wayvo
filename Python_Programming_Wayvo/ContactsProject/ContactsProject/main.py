import json

CONTACTS_FILE = "Contacts.json"
#Load contacts from the JSON file.
def load_contacts():

    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

#Save contacts to the JSON file.
def save_contacts(contacts):

    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

#Create a new contact
def create_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

#Read and display all contacts.

def read_contacts():

    contacts = load_contacts()
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")

#Update a contact's details.

def update_contact():

    name = input("Enter the name of the contact to update: ")
    contacts = load_contacts()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input("Enter new phone (leave blank to keep current): ") or contact["phone"]
            contact["email"] = input("Enter new email (leave blank to keep current): ") or contact["email"]
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    """Delete a contact by name."""
    name = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()
    filtered_contacts = [contact for contact in contacts if contact["name"].lower() != name.lower()]
    if len(contacts) == len(filtered_contacts):
        print("Contact not found.")
    else:
        save_contacts(filtered_contacts)
        print("Contact deleted successfully!")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_contact()
        elif choice == "2":
            read_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


main()