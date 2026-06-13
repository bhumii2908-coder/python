# DICTIONRIES
# unorderd collection of items they store data in a key value pairs
# creating a empty dictionries
empty_dict=dict()
print(empty_dict)
print(type(empty_dict))

# creating a dictionries
student={"name":"lily","age":32,"marks":65}
print(student)
print(type(student))
# single key is always used
student={"name":"lily","age":32,"name":65}
print(student)

# accessing dictionary elements
student={"name":"lily","age":32,"marks":65,"grade":'A',"class":6}
print(student['marks'])
print(student['grade'])
print(student['name'])
print(student['age'])

# accessing uswing get()method
student={"name":"mark","class":6,"grade":'A',"age":11,"mark":67}
print(student.get('class'))
print(student.get('grade'))
print(student.get('age'))
print(student.get('last_name'))

# modifying dicitonary elements
# dicitonary are mutable so you can add update or delete elements
student={"name":"mark","class":6,"grade":'A',"age":11,"mark":67}
student["class"]=7
student["name"]='lily'
student["age"]=12
print(student)
student["address"]='indore'
print(student)

# delete key and value pair
# student={"name":"lily","grade":'A',"class":7,"address":'indore'}
# del student['name']
# print(student)

# dictionary methods
# get all the key
# keys=student.keys()
# print(keys)
# # get all the values
# values=student.values()
# print(values)
# # get all key value pairs
# items=student.items()
# print(items)

# shallow copy
# student={"name":"lily","grade":'A',"class":7,"address":'indore'}
# student_copy=student
# print(student)
# print(student_copy)

#shallow method is use to copy the variables but we arre updated elemnts but it not effect  
# student_copy=student.copy()
# print(student_copy)
# student["name"]="mark"
# student["address"]="delhi"
# print(student)

# itreating over dictionaries
# you can use loops itreating over dictionatries,key,values or items
# iterating over keys
# student={"name":"lily","grade":'A',"class":7,"address":'indore'}
# # iterating over keys
# for keys in student.keys():
#     print(keys)
    
# # itreating over values
# for values in student.values():
#     print(values)
    
# # iytreating over items/key value
# for key,value in student.items():
#     print(f"{key}:{value}")
    
# nested disctionaries
students={
    "points":{"name":"lily","grade":'A',"class":7},
     "option":{"address":'indore',"age":15,"marks":87} 
}  
print(students) 

# access nested dictionaries elements
print(students["points"]["grade"])
print(students["points"]["name"])
print(students["option"]["age"])
print(students["option"]["marks"])

# iterating over nested dictionaries
# students={
#     "points":{"name":"lily","grade":'A',"class":7},
#      "option":{"address":'indore',"age":15,"marks":87} 
# }  
# print(students) 

# for points,option in students.items():
#     print(f"{points}:{option}")
#     for key,value in option.items():
#         print(f"{key}:{value}")
        
# dictonary comphrehension
# squares={i:i**2 for i in range(10)}
# print(squares)

# # condition dictionary comprehension
# even={i:i**2 for i in range(10) if i%2==0}
# print(even)

# odd={n:n*2 for n in range(10) if n%3==0}
# print(odd)

# practical exam
# use a dictionary to count he frequency of elements in list
# numbers=[1,1,1,1,2,2,3,3,4,4,4,5,5,6,6]
# frequency={}
# for number in numbers:
#     if number in frequency:
#         frequency[number]+=1
#     else:
#         frequency[number]=1
# print(frequency)

# merge2 dictionries  into one
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
mixed={**dict1,**dict2}
print(mixed)











