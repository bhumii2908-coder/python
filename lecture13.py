# THE MAP FUNCTION IN PYTHON

# FOR EXAMPLE
def square(x):
    return x*x
    
print(square(4))
print(square(6))


numbers=[1,2,3,4,5,6,7,8,9]
print(list(map(square,numbers)))

# LAMBDA FUNCTION WITH MAP
numbers=[1,2,3,4,5,6,7,8,9]
print(list(map(lambda x:x**3,numbers)))

# MAP MULTIPLE ITERABLES

number1=[1,2,3]
number2=[4,5,6]

table=list(map(lambda a,b:a+b,number1,number2))
print(table)


# MAP()TO CONVERT A LIST OF STRING TO INTERGERS
# USE MAP TO CONVERT STRING TO INTEGERS
str_numbers=['1','2','3','4','5','6','7']
int_numbers=list(map(int,str_numbers))

print(int_numbers)



words=['apple','banana','cherry']
upper_word=list(map(str.upper,words))
print(upper_word)

def get_name(person):
    return person['name']

people=[
    {'name':'lily','age':32},
    {'name':'jack','age':33}
]
value=list(map(get_name,people))
print(value)