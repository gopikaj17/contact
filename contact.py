class Contact:
    def __init__(self, full_name, phone, email, location):
        self.full_name, self.phone, self.email, self.location = full_name, phone, email, location

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added!")

    def display_contacts(self):
        print("\n--- Contact List ---")
        for contact in self.contacts:
            print(f"Name: {contact.full_name}, Phone: {contact.phone}")

    def search_contacts(self, keyword):
        matching_contacts = [c for c in self.contacts if keyword.lower() in c.full_name.lower() or keyword in c.phone]
        self._display_results(matching_contacts, "Matching Contacts")

    def update_contact(self, old_name, new_contact_info):
        for contact in self.contacts:
            if contact.full_name.lower() == old_name.lower():
                contact.__dict__.update(new_contact_info.__dict__)
                print("Contact updated!")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c.full_name.lower() != name.lower()]
        self._display_results(self.contacts, "Contact deleted", "Contact not found")

    def _display_results(self, items, success_msg, failure_msg="No items found."):
        print(success_msg if items else failure_msg)

def run_contact_manager():
    contact_manager = ContactManager()

    while True:
        print("\n--- Contact Management ---")
        print("1. Add Contact\n2. Display Contacts\n3. Search Contacts\n4. Update Contact\n5. Delete Contact\n6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            new_contact = Contact(input("Full Name: "), input("Phone: "), input("Email: "), input("Location: "))
            contact_manager.add_contact(new_contact)

        elif choice == '2':
            contact_manager.display_contacts()

        elif choice == '3':
            contact_manager.search_contacts(input("Enter name or phone to search: "))

        elif choice == '4':
            old_name = input("Enter name of contact to update: ")
            new_info = Contact(input("New Full Name: "), input("New Phone: "), input("New Email: "), input("New Location: "))
            contact_manager.update_contact(old_name, new_info)

        elif choice == '5':
            contact_manager.delete_contact(input("Enter name of contact to delete: "))

        elif choice == '6':
            print("Exiting Contact Management.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    run_contact_manager()
