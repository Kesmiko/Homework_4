#Завдання перше
def total_salary(path):

    total = 0

    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            string = line.split(",")
            total = total + float(string[1])
            average = total / len(lines)
        return (total,average)

print(total_salary("Salary.txt"))


#Завдання друге
def get_cats_info(path):
    try: 
        with open(path, "r") as file:
            cat_list = []
            for lines in file:
                str = lines.strip()
                str = str.split(",")
                keys = ["id", "name", "age"]
                dict_ = dict(zip(keys,str))
                cat_list.append(dict_)
    except:
        return f"Файл {path} не знайдено"
    return cat_list       

print(get_cats_info("Cats.txt"))


#Завдання четверте
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Контакт [{name}] вже є. Можна замінити за допомогою 'change'"
    else:
        contacts[name] = phone
        return f"Контакт [{name}] [{phone}] доданий."

def change_contact(args, contacts):
    name, phone = args
    if contacts.get(name) == None:
        return f"Немає в телефоннній книжці. Можна додати за допомогою 'add'"
    else:
        contacts[name] = phone
        return f"Контакт [{name}] [{phone}] змінено."
        
        
def show_phone(args, contacts):
    name = args[0]
    if contacts.get(name) == None:
        return "Немає в телефоннній книжці"
    else:
        return f"Номер телефону '{name}' : '{contacts.get(name)}'"

def show_all(contacts):
    return contacts
    
def main():
    contacts = {'John':"123", 'Jane':"234", 'Steve':"555"}
    print("Welcome to the assistant bot!")
    commands = ["hello", "add", "change", "phone", "all", "close", "exit"]
    while True:
        user_input = input(f"Enter a command ({commands}): \n>>> ")
        command, *args = parse_input(user_input)

        if command in [commands [5], commands [6]]:
            print("Good bye!")
            break

        elif command == commands [0]:
            print("How can I help you?")
        
        elif command == commands [1]:
            if len(args) == 2:
                print(add_contact(args, contacts))
            else:
                print ("Спробуйте так ('add [name] [phone_numder]')")
        
        elif command == commands [2]:
            if len(args) == 2:
                print(change_contact(args, contacts))
            else:
                print ("Спробуйте так ('change [name] [phone_numder]')")  
                
        
        elif command == commands [3]:
            if len(args) == 1:
                print(show_phone(args, contacts))
            else:
                print ("Спробуйте так ('phone [name]')")
            

        elif command == commands [4]:
            print(show_all(contacts))
            
                    
        else:
            print("Невірна команда")

if __name__ == "__main__":
    main()