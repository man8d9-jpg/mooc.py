while True:
    Pbook = {}
    options = input("command(1 search, 2 add, 3 quit): ")

    if options == 3:
        print("quitting...")
        break
    
    elif options == 2:
        name = input("name: ")
        number = input("number: ")

        Pbook['Nombre'] = name
        Pbook['Numero'] = number

        print("ok!")
    
    elif options == 1:
        Name = input("name: ")
        
        for key, value in Pbook.items():
            if key == Name:
                print(value)

            else:
                print("no number")

        

