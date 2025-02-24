products = {"apple": 10, "banana": 15, "mango": 25} #products and prices
print(f"Initial products: {products}")

while True:
    actions = input("Choose an action - (1) Update Price, (2) Lookup, (3) View Dictionary, (4) Quit: ") #actions
    if actions == "1":
        fruit = input("Update which product?: ").lower() #lowercase
        if fruit not in products: #andyan na yung products sa taas
            print("wala nang c2 na red, green nalang (ayaw ko nyan wtf lasang tubig)")
        else:
            try:
                cost = int(input("New price: ")) #new price 
                products[fruit] = cost
                print(f"Updated products: {products}")
            except ValueError:
                print("Di yan maaari")
    elif actions == "2": #lookup products
        fruit = input("Lookup which product?: ").lower()
        if fruit not in products:
            print("wala nang c2 na red, green nalang (ayaw ko nyan wtf lasang tubig)")
        else:
            print(f"{fruit}: {products[fruit]}")
    elif actions == "3": #view products
        print("List of Products and their Prices:")
        for fruit, cost in products.items():
            print(f"{fruit}: {cost}")
    elif actions == "4": #exit
        print("bye")
        break
