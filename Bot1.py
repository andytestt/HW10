from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.get_value()] = record

class Record:
    def __init__(self, name):
        self.name = name
        self.phone = Phone()
    
    def add_phone(self, phone):
        self.phone.add_phone(phone)
    
    def remove_phone(self, phone):
        self.phone.remove_phone(phone)
    
    def edit_phone(self, old_phone, new_phone):
        self.phone.edit_phone(old_phone, new_phone)

class Field:
    def __init__(self):
        self.value = None
    
    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return self.value

class Name(Field):
    def set_value(self, value):
        if not value:
            raise ValueError("Name field cannot be empty.")
        super().set_value(value)

class Phone(Field):
    def __init__(self):
        super().__init__()
        self.value = []
    
    def add_phone(self, phone):
        self.value.append(phone)
    
    def remove_phone(self, phone):
        if phone in self.value:
            self.value.remove(phone)
    
    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.value:
            index = self.value.index(old_phone)
            self.value[index] = new_phone

contacts = AddressBook()

def add_contact(name, phone):
    record = Record(Name())
    record.name.set_value(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return "Contact added successfully."

def change_phone(name, phone):
    if name in contacts.data:
        record = contacts.data[name]
        record.add_phone(phone)
        return "Phone number updated successfully."
    else:
        raise KeyError

def get_phone(name):
    if name in contacts.data:
        record = contacts.data[name]
        return record.phone.get_value()
    else:
        raise KeyError

def show_all_contacts():
    if len(contacts.data) == 0:
        return "No contacts found."
    else:
        output = ""
        for name, record in contacts.data.items():
            phone_numbers = ", ".join(record.phone.get_value())
            output += f"{name}: {phone_numbers}\n"
        return output.strip()

def main():
    print("How can I help you?")

    while True:
        command = input("> ").lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            try:
                _, name, phone = command.split(" ")
                print(add_contact(name, phone))
            except ValueError:
                print("Invalid input. Please enter name and phone number separated by a space.")
        elif command.startswith("change"):
            try:
                _, name, phone = command.split(" ")
                print(change_phone(name, phone))
            except ValueError:
                print("Invalid input. Please enter name and phone number separated by a space.")
            except KeyError:
                print("Contact not found.")
        elif command.startswith("phone"):
            try:
                _, name = command.split(" ")
                print(get_phone(name))
            except ValueError:
                print("Invalid input. Please enter a name.")
            except KeyError:
                print("Contact not found.")
        elif command == "show all":
            print(show_all_contacts())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
