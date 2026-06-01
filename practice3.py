# creating and Accessing tuple
positive_tuple=(1,2,3,4,5,6,7,8,9,10)
print(positive_tuple)

# accessing tuple element
number=(1,2,3,4,5,6,7,8,9,0)
first,*middle,last=number
print(first)
print(middle)
print(last)

# tuple slicing
tup=(1,2,3,4,5,6,7,8,9,0)
print(tup[0:3])
print(tup[-3:])
print(tup[2:5])

# nested tuple
tup=((1,2,3),
    ("a","b","c"),
    (True,False))
print(tup[0][2])
print(tup[1][2])
print(tup[2][1])

# tuple concantion
number=(1,2,3)
mixed=(4,5,6)
concatenate_tuple=number+mixed
print(concatenate_tuple)

# tuple method
# tup=(1,2,2,3,4,5,5,6,7,8,8,8,9,0,0,0)
print(tup.count(2))
print(tup.count(5))
print(tup.count(8))
print(tup.count(0))
print(tup.index(2))
print(tup.index(5))
print(tup.index(8))
print(tup.index(0))

# unpacking tuple
# element
number=1,2,3,4,5
a,b,c,d,e=number
print(a)
print(b)
print(c)
print(d)
print(e)

# tuple conversion
lst=[1,2,3,4,5]
value=tuple(lst)
print(value)

# tuple of tuples
tup=((1,2,3),(4,5,6),(7,8,9))
print(tup)

# tuple and list
tup=(1,2,3,4,5)
value=list(tup)
value.append(6)
solve=tuple(value)
print(solve)

# tuple and string
tup=("world","earth","fish","star")
result=" ".join(tup)
print(tup)

# nested tuple itration
tup=((1,2,3),("hello","world","earth"),(True,False))
for sub in tup:
    for item in sub:
        print(item,end=" ")
    print()   
    
# 12,14,15
        


