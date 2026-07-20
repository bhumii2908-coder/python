# Lambda fuctions in python
#  syntax=lambda agrumnet:expression

# for example
addition=lambda a,b,c:a+b+c

print(addition(2,5,8))
print(type(addition))


even=lambda num:num%2==0
print(even(24))
print(even(33))

# map()-applies afunction to all items in a list
number=[1,2,3,4,5,6]
# def square(number):
#     return number**2

# print(square(2))   

# using map function
print(list(map(lambda n:n**2,number)))