# number=[1,2,3,4,5,6,6,6,7,8,9,0,0]
# print(set(number))

# # counting uniqur words and text
# text="in tnis tutorial we are discussing about sets"
# words=text.split()
# # convert list of words to set to get unique words
# unique_words=set(words)
# print(unique_words)
# print(len(unique_words))

# data structures assigments
# sets
# creating and accessing sets
# value={1,2,3,4,5,6,7,8,9,10}
# print(value)
# print(type(value))

# ADDING AND REMOVING ELEMENTS
# value={1,2,3,4,5,6,7,8,9,10}
# value.add(11)
# value.remove(1)
# print(value)

# SET OPREATION
# set1={1,2,3,4,5}
# set2={2,4,6,8,10}
# solve=set1.union(set2)
# print(solve)
# solve=set1.intersection(set2)
# print(solve)
# solve=set1.difference(set2)
# print(solve)
# solve=set1.symmetric_difference(set2)
# print(solve)

# SET COMPREHENSIONS
# unique_squares={i*i for i in(1,2,3,4,5,6,7,8,9,10)}
# print(unique_squares)

# FILTRE SETS
# value={1,2,3,4,5,6,7,8,9,10}
# sove={2,4,6,8,10,12,14,16,18}
unique_even={2*i for i in(1,2,3,4,5,6,7,8,9,10)}
print(unique_even)

# set method
# value={1,2,2,2,3,4,4,4,5,6,6,6,7,7,8,9}
# value.remove(2)
# value.remove(4)
# value.remove(6)
# value.remove(7)
# print(value)

# subset and superset
# set1={1,2,3,4,5}
# set2={3,4,5,-1,-2}
# value=set2.issubset(set1)
# value=set1.issuperset(set2)
# print(value)
# solve=set1.issuperset(set2)
# # print(solve)

# frozenset
# solve={11,22,33,4,55}
# frozenset(solve)
# print(frozenset(solve))

# set and list conversion
# assig=list({1,2,3,4,5})
# assig.append(6)
# print(assig)
# assig=set([1,2,3,4,5,6])
# print(assig)

# iterating over set

# removing element for set
# solve={1,2,3,4,5,6,7,8,9}
# solve.clear()
# print(solve)

# set symmetric difference update 
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# set1.symmetric_difference_update(set2)
# print(set1)

# set membership testing
# setting={1,2,3,4,5,6,7,8,9}
# print(3 in setting)
# print(10 in setting)

# set and tuples
online={(1,2),("helloworld"),(3.22,44.5),(True,False)}
print(online)
