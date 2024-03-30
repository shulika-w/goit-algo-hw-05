def input_error(func): # Створення декоратору для обробки помилок
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command."
        except KeyError:
            return "Enter the key for the command."
        except IndexError:
            return "Incorrect index."
        
    return inner

@input_error # Обгортання функції декоратором
def parse_input(user_input): # Створення функції, яка приймає рядок вводу користувача як аргумент
    cmd, *args = user_input.split() # Розбиття рядку на дві складові, перше слово зберігається у змінній cmd, решта - в списку args
    cmd = cmd.strip().lower() # Видалення пробілів навколо команди і перетворення її на нижній регістр
    return cmd, *args # Повернення обробленого рядка в змінній cmd і списку args

@input_error # Обгортання функції декоратором
def add_contact(args, contacts): # Створення функції додавання контакту
    name, phone = args # Приймання двох змінних як аргументів
    contacts[name] = phone # Запис значення phone до ключа name у словнику
    return "Contact added." 

@input_error # Обгортання функції декоратором
def change_contact(args, contacts): # Створення функції зміни значення для існуючої пари ключ-значення
    name, phone = args # Приймання двох змінних як аргументів
    contacts[name] = phone # Запис нового значення phone до ключа name у словнику
    return "Contact updated."

@input_error # Обгортання функції декоратором
def show_phone(args, contacts): # Створення функції виведення на екран значення за викликом ключа
    name = args[0]
    return contacts[name] 

@input_error # Обгортання функції декоратором
def show_all(args, contacts): # Створення функції виведення на екран всіх доданих пар ключ-значення
    return contacts

def main(): # Створення функції, яка управляє основним циклом обробки команд
    contacts = {} # Створення порожнього словника
    print("Welcome to the assistant bot!") # Виклик привітання при запуску
    while True: # Вхід в нескінченнний цикл
        user_input = input("Enter a command: ") # Очікування на введення від користувача
        command, *args = parse_input(user_input) # Виклик функції

        if command in ["close", "exit"]: 
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            if len(contacts.items()) == 0:
                print("Contact list is empty")
            for name, phone in contacts.items():
                print(name + ":" + ' ' + phone)
        else:
            print("Invalid command.") # Варіації команд і виклик відповідних функцій

if __name__ == "__main__": 
    main()