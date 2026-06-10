# emplt tuple
# lst=list()
# print(type(lst))
# tpl=tuple()
# print(type(tpl))

# you can create tuple to list and list to tuple
# value=tuple([1,2,3,4,5,6,7,8,9])
# print(value)

# section=list[(1,2,3,4,5,6,7,8,9)]
# print(section)

# mixed_tuple=(1,2,3,4,5,"hello","world","chatgpt",3.44,4.222,True,False)
# print(mixed_tuple)

# ACCESING TUPLE ELEMENT
# you can print index element 
# number=(1,2,3,4,5,6,7,8,9,10)
# print(number[0])
# print(number[5])
# print(number[-2])
# print(number[-1])

# slicing element it like a list
# number=(1,2,3,4,5,6,7,8,9,10)
# print(number[0:5])
# print(number[::])
# print(number[:-1])
# print(number[0:])
# print(number[0:7])
# if i use[::-1]so is get the rivers of all the element
# print(number[::-1])

# tuple operations
# all the method called
# concatenation_tuple
number=(1,2,3,4,5,6,7,8,9,10)
mixed_tuple=(1,2,3,4,5,"hello","world","chatgpt",3.44,4.222,True,False)
value=number+mixed_tuple
print(value)

# number=(1,2,3,4,5,6)
# mixed=(1,2,3,"hello","world",22.45,56.7,True,False)
# value=number+mixed
# print(value)

# one more think do you always remember
# mixed=(1,2,3,"hello","world",22.45,56.7,True,False)
# value=mixed*3
# print(value)

# number=(1,2,3,4,5,6)
# number*3
# print(number*3)

# immutable nature of tuples 
# tuple are immutable meaning their element cannot be changed once assignet

# tuple method
number=(1,2,3,4,5,6,7,8,9)
# count use for counting a element
print(number.count(1))
# index is use for return value of the index
print(number.index(3))

# packing and unpacking tuple
# packing
packed=1,"heelo world",3.44
print(packed)

# unpacked_tuple
a,b,c=packed
print(a)
print(b)
print(c)

# one more think
number=(1,2,3,4,5,6,7,8,9)
first,*middle,last=number
print(first)
print(middle)
print(last)

# nested tuple
# nested list
lst=[1,2,3,8,9,0],[4,5,6,7],[1,"hello world",3.24,"t"]
print(lst[0][0:][::-1])  #you can use index and slicing

# nested tuple
# access the element inside a tuple
tup=((1,2,3),(4,5,6),("a","b","c"))
print(tup[0][::-1])
print(tup[1][2])
print(tup[2][1])

# iterting over nested tuple
for sub in tup:
    for item in sub:
        print(item,end=" ")
    print()    

































