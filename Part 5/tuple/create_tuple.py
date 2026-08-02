def create_tuple(x:int, y:int, z:int):
    values = (min(x,y,z), max(x,y,z), x+y+z)
    return values

print(create_tuple(3,-1,7))


