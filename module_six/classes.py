from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.validate_format(value)
        super().__init__(value)
        

    def validate_format(self):
        if not re.match(r'^\d{10}$', self.value):
            raise ValueError(
                "Invalid phone number format. Please provide a 10-digit number.")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def del_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise ValueError("Phone number not found in record.")

    def update_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            Phone(new_phone)
            self.phones[self.phones.index(old_phone)] = new_phone
        else:
            raise ValueError("Phone number not found in record.")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return self
        return None

    def __str__(self):
        phone_numbers = ', '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phone_numbers}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Record with name '{name}' not found.")

    def find(self, name):
        return self.data.get(name)

    def update(self, name, record):
        if name in self.data:
            self.data[name] = record
        else:
            print(f"Record with name '{name}' not found. Cannot update.")
