def invert(dictionary: dict):
    reversed = {value : key for key, value in dictionary.items()}
    dictionary.clear()
    dictionary.update(reversed)

s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s) 


#OR


def invert(dictionary: dict):
    reversed = {}

    for key, value in dictionary.items():
        reversed[value] = key
    
    dictionary.clear()

    for key, value in reversed.items():
        dictionary[key] = value
    
s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)