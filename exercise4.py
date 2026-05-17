# Консольни бот помічник, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.
def input_error(func): # Декоратор для обробки помилок введення користувачаю
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter a user name "
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts): # Функція для додавання нового контакту до списку контактів.
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts): # Функція для зміни номера телефону існуючого контакту.
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."
    
@input_error
def show_phone(args, contacts): # Функція для відображення номера телефону контакту.
    name = args[0]
    return contacts[name]

@input_error
def show_all(contacts): # Функція для відображення всіх контактів.
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone  in contacts.items())



def main():
    print("Welcome to the assistant bot!")
    contacts = {}
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue
        
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change": # Функція для зміни номера телефону існуючого контакту.
            print(change_contact(args, contacts))
        elif command == "phone": # Функція для відображення номера телефону контакту.
            print(show_phone(args, contacts))
        elif command == "all": # Функція для відображення всіх контактів.
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
