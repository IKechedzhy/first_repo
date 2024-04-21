def parse_input(command):
    cmd, *args = command.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# def change_username_phone():


def phone_username(name, contacts):
    for name in contacts:
        if name in contacts:
            return contacts[name]
        else:
            return f"{name} not found"
    
def show_all(contacts):
    contacts_str = ""
    for key, value in contacts.items():
        contacts_str += f"{key}: {value}\n"
    return contacts_str


