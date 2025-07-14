import os

def saveNewEntry():
    global age_sum
    while True:
        id = input("Please enter your ID: ")
        if id.isdigit():
            if int(id) not in users:
                id = int(id)
                break
            print(f"\nError: ID already exists: {id}\nPlease enter a different ID.\n")
            continue    
        print("Invalid ID. Please enter a numeric ID.")
    name = input("Please enter your name: ")
    while True:
        age = input("Please enter your age: ")
        if age.isdigit():
            if int(age) > 0 and int(age) < 130:
                age = int(age)
                age_sum += age
                users[id] = {'name': name, 'age': age}
                users_index[len(users_index)] = id
                print(f"Entry saved:\nID: {id}, Name: {name}, Age: {age}")
                break
        print("Invalid age. Please enter a valid age.")
    

def searchById():
    id = input("Enter the ID to search: ")
    result = users.get(id, None)
    if result != None:
        print(f"ID: {id}\nName: {result['name']}\nAge: {result['age']}")
    else:
        print(f"ID {id} not found in the list.")

def printAgeAvg():
    if users:
        print(f"Average age is: {age_sum / len(users):.2f}")
    else:
        print("No entries in list!")

def printAllNames():
    if users:
        for index, value in enumerate(users.items()):
            print(f"{index}. {value[1]['name']}")
    else:
        print("No entries in list!")

def printAllIds():
    if users:
        for index, value in enumerate(users.items()):
            print(f"{index}. {value[0]}")
    else:
        print("No entries in list!")

def printAllEntries():
    if users:
        for index, value in enumerate(users.items()):
            print(f"{index}. {value[0]}\n   Name: {value[1]['name']}\n   Age: {value[1]['age']}")
    else:
        print("No entries in list!")

def printEntryByIndex():
    if users:
        while True:
            search_index = input(f"Enter the index of the entry to print (0 to {len(users) - 1}): ")
            if search_index.isdigit():
                search_index = int(search_index)
                if search_index >= 0 and search_index < len(users):
                    index_id = users_index.get(search_index, None)
                    if index_id != None:
                        user = users.get(index_id, None)
                        print(f"ID: {index_id}\nName: {user['name']}\nAge: {user['age']}")
                    else:
                        print(f"ID {index_id} not found in the list.")
                    break
            print(f"Invalid index. Please enter a number between 0 and {len(users) - 1}.")
    else:
        print("No entries in list!")

def show_menu():
    exit_program = False
    while not exit_program:
        print("1. Save a new entry")
        print("2. Search by ID")
        print("3. Print ages average")
        print("4. Print all names")
        print("5. Print all ID's")
        print("6. Print all entries")
        print("7. Print entry by index")
        print("8. Exit")
        choice = input("Please enter your choice (1-8): ")
        
        if choice == '1':
            saveNewEntry()
        elif choice == '2':
            searchById()
        elif choice == '3':
            printAgeAvg()
        elif choice == '4':
            printAllNames()
        elif choice == '5':
            printAllIds()
        elif choice == '6':
            printAllEntries()
        elif choice == '7':
            printEntryByIndex()
        elif choice == '8':
            while True:
                exit_input = input("Are you sure (y/n)? ")
                if exit_input =="y":
                    exit_program = True
                    print("Exiting the program. Goodbye!\n")
                    break
                if exit_input == "n":
                    os.system ('cls')
                    print("Returning to the main menu.\n")
                    break    
                else:
                    continue  
            continue  
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")

        os.system ('pause')
        os.system ('cls')

def main():
    show_menu()

if __name__ == '__main__':
    users = {1234: {"name": "Shimon", "age": 30},
            5678: {"name": "Avi", "age": 25},
            9012: {"name": "Marko", "age": 35}}
    users_index = {0: 1234, 1: 5678, 2: 9012}
    age_sum = sum(user['age'] for user in users.values()) 
    
    # users = {}
    # users_index = {}
    # age_sum = 0

    main()