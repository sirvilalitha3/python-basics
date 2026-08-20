#list comprehensions make your code shorter and more readable compared to using loops.
# Traditional way
squares = []
for i in range(5):
    squares.append(i**2)

# Using list comprehension
squares = [i**2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

#set comprehension
unique = {x for x in "banana"}
print(unique)  # {'b', 'a', 'n'} #removes duplicated

#dict
numbers = {i: i**2 for i in range(5)}
print(numbers)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

even_squares = [i**2 for i in range(10) if i % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
