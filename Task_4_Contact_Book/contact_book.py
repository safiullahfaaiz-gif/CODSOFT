class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append(Contact(name, phone, email, address))
        print("\nContact added successfully!\n")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts available.\n")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, keyword):
        found = [c for c in self.contacts if keyword.lower() in c.name.lower() or keyword in c.phone]
        if found:
            print("\nSearch Results:")
            for contact in found:
                print(contact, "\n")
        else:
            print("\nNo contact found.\n")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("\nEnter new details (leave blank to keep current):")
                new_phone = input(f"Phone ({contact.phone}): ") or contact.phone
                new_email = input(f"Email ({contact.email}): ") or contact.email
                new_address = input(f"Address ({contact.address}): ") or contact.address

                contact.phone, contact.email, contact.address = new_phone, new_email, new_address
                print("\nContact updated successfully!\n")
                return
        print("\nContact not found.\n")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("\nContact deleted successfully!\n")
                return
        print("\nContact not found.\n")


def menu():
    book = ContactBook()
    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            book.add_contact(name, phone, email, address)

        elif choice == "2":
            book.view_contacts()

        elif choice == "3":
            keyword = input("Enter name or phone to search: ")
            book.search_contact(keyword)

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            book.update_contact(name)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            book.delete_contact(name)

        elif choice == "6":
            print("\nExiting Contact Book. Goodbye!\n")
            break

        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    menu()
