address_book = {}

while True:
    action = input("Choose an action - (1) Add, (2) Lookup, (3) View Dictionary, (4) Quit: ") #actions
    
    if action == '1': #dito mag input ng name at number
        name = input("Enter Name: ")
        num = int(input("Enter Number: "))
        address_book[name] = num
        print(f"Added {name} : {num}")
    elif action == '2': #maghahanap ng pangalan
        lookup = input("Lookup Name: ")
        if lookup in address_book:
            print(f"{lookup}: {address_book[lookup]}")
        else:
            print("Who tf is ts gng?")
    elif action == '3': #Display ng mga dictionary
        print("Address Book:")
        for name, number in address_book.items():
            print(f"{name}: {number}")
    elif action == '4': #exit
        print("Adios")
        break
    else:
        print("1-4 na nga yung option basa basa naman po") 