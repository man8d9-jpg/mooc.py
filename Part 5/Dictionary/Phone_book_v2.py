Pbook = {}
while True:
    options = (input("command(1 search, 2 add, 3 quit): "))

    if options == "3":
        print("quitting...")
        break
        
    elif options == "2":
        name = input("name: ")
        number = (input("number: "))           

        if name not in Pbook:
            Pbook[name] = [] 

        Pbook[name].append(number)
        print("ok!")
    
    elif options == "1":
        Name = input("name: ")
    
        if Name in Pbook:
            for i in Pbook[Name]:
                print(i)      
    
        else:
            print("no number")
     


