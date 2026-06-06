# data structure assigment
# Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.
# squares={}
# for n in range(1,11):
#     squares[n]=n**2
# print(squares)

# Print the value of the key 5 and the keys of the dictionary created in Assignment 1.
# squares={}
# for n in range(1,11):
#     squares[n]=n**2
# print(squares)
# print(squares[5])
# print(squares.get(5))

# Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.
# squares[11]=121
# print(squares)

# Iterate over the dictionary created in Assignment 1 and print each key-value pair.
# items=squares.items()
# print(items)

# Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. Print the new dictionary.
# cubes={}
# for n in range(1,11):
#     cubes[n]=n**3
# print(cubes)    

cubes={n:n**3 for n in range(1,11)}
print(cubes)

# Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.

 













