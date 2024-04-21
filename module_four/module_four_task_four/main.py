
from functions import *

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    
    while True:

        command = input("Enter a command: ").strip().lower()
        command, *args = parse_input(command)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command in ["hello", "hi"]:
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        # elif command == "change":
        #     print()

        elif command == "chk":
            print(phone_username(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()