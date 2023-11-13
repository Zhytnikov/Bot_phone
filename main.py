# Декоратор для обробки помилок 
def if_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Contact not found"
    return inner

# Функція для обробки команд користувача
@if_error
def parser(command):
    if command == "hello":
        return hello()
    
    elif command.startswith("add"):
        _, name, phone = command.split()
        return add_contact(name, phone)

    elif command.startswith("change"):
        _, name, phone = command.split()
        return change_phone(name, phone)

    elif command.startswith("phone"):
        _, name = command.split()
        return get_phone(name)

    elif command == "show all":
        return show_all()

    else:
        return "Invalid command. Please try again."

def hello():
    return "How can I help you?"

def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} added"

def change_phone(name, phone):
    contacts[name] = phone
    return f"Phone number for {name} changed"

def get_phone(name):
    return f"Phone number for {name}: {contacts.get(name, 'Contact not found')}"

def show_all():
    return show_all_contacts(contacts)


def main():
    while True:
        command = input("Enter command: ").lower()

        if command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break

        print(parser(command))

# Функція для виводу всіх контактів
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts"
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

contacts = {}

if __name__ == "__main__":
    main()
