def remove_smallest(numbers: list):
    numbers.remove(min(numbers))
    
    # smallest = numbers[0]
    # for i in numbers:
    #     if i < smallest:
    #         smallest = i
    # numbers.remove(smallest)

numbers = [2, 4, 6, 1, 3, 5]
remove_smallest(numbers)
print(numbers)

