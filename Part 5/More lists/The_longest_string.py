def longest(strings: list):
    lengthiest = (strings[0])
    for i in range(len(strings) - 1):
        if len(strings[i]) > len(lengthiest):
            lengthiest = strings[i]
    return lengthiest

strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
print(longest(strings))