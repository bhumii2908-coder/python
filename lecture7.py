# list
value=[]
print(type(value))

names=["lily,savapnil,akshara,madhuri",1,2,3,4,5]
print(names)

mixed=["hello",1234,33.450,True] 
print(mixed)
print(type(mixed))

#  accesing list elsements
school=["class","teacher","students","board","exam","canteen"]
print(school[0])
print(school[1])
print(school[2])
print(school[3])
print(school[-2])
print(school[-1])

# this is use for you want to print all list 

print(school[1:])
# it not add the last element it and after the last element

print(school[0:-2])

# modifying the list elements

school=["class","teacher","students","board","exam","canteen"]
school[1]="facltiy"
print(school)
school[3]="vision borad"
print(school)

# listmethod
fruits=["apple","banana","spobreey","kiwi","cherry","gauva"]

# append use for you want to add item in end
fruits.append("watermelon")
print(fruits)
# insert use for you want to add item in middle,start
fruits.insert(1,"orange")
print(fruits)
fruits.insert(0,"cherry")
print(fruits)

# remove is use for remove the items
fruits.remove("cherry")
print(fruits)

# remove and the return the last items
popped_fruits=fruits.pop()
print(popped_fruits)
print(fruits)

# fruits=["apply","banana","cherry","watermelon","oreang","pappaya"]
# value=fruits.index("cherry")
# print(value)

# one more thing
# fruits.insert(4,"banana")
# print(fruits)
# print(fruits.count("banana"))

# sorts the list in asending
# fruits.sort()
# print(fruits)

# revers the list
# fruits.reverse()
# print(fruits)

# remove all the items in list
# fruits.clear()
# print(fruits)

# slicing list
# number=[1,2,3,4,5,6,7,8,9,10]
# print(number[2:6])
# print(number[:5])
# print(number[6:])
# print(number[::2])  #jumpstepsize
# print(number[::3])
# print(number[::-1])
# print(number[::-2])       #jump step size   

#  itreating over list
fruits=["apply","banana","cherry","watermelon","oreang","pappaya"]
for fruit in fruits:
     print(fruit)

# numbers=[1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
#     print(number)


# movies=["murder","flower of the evil","bloodhound","rich man","the king"]
# for movie in movies:
#     print(movie)
# for index,movie in enumerate(movies):
    # print(index,movie)


# numbers=[1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
#     print(number)
    
# itreating with index 
# for index,number in enumerate(numbers):

# list comprehension
# basic syantax[expression for item in iterable]
# with conditionl logic [expression for item in iterable if condition]
# basic list comphrension
# sqaure=[num**2 for num in range(10)]
# print(sqaure)

# list comprehension with condition
# even numbers
lst=[]
for n in range(10):
    if n%2==0:
        lst.append(n)
print(lst)       

# odd numbers
value=[]
for i in range(10):
    if i%2!=0:
        value.append(i)
print(value)  

# nested list comprehension
# expression for item1 in iterable1 for item2 iterable2
lst1=[1,2,3,4,5]
lst2=["a","b","c","d","e"]
mix=[[i,j]for i in lst1 for j in lst2]
print(mix)









    
    
    
    
    
    
    
    
   
    
    



























































