def factorials(n: int):
    fac_dictionary = {}

    for i in range(1, n+1):
        fact = 1
        for j in range(1, i+1):
            fact *= j
        fac_dictionary[i] = fact
    return fac_dictionary

k = factorials(5)
print(k[1])
print(k[3])
print(k[5])