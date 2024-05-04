def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid input format."

    return inner

@input_error
def parse_input(command):
    cmd, *args = command.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_username_phone(args, contacts):
    name, phone = args
    if name  in contacts:
        contacts[name] = phone
    return "Contact updated"

@input_error       
def show_phone(name, contacts):
    for name in contacts:
        if name in contacts:
            return contacts[name]
        else:
            return f"{name} not found"

@input_error
def show_all(contacts):
    contacts_str = ""
    for key, value in contacts.items():
        contacts_str += f"{key}: {value}\n"
    return contacts_str


