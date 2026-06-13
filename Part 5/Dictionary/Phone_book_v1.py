Pbook = {}
while True:
    options = int(input("command(1 search, 2 add, 3 quit): "))

    if options == 3:
        print("quitting...")
        break
    
    elif options == 2:
        name = input("name: ")
        number = int(input("number: "))

        Pbook[name] = number

        print("ok!")
    
    elif options == 1:
        Name = input("name: ")
        
        if Name in Pbook:
            print(Pbook[Name])

        else:
            print("no number")
        
        
      

