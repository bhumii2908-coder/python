# # creating dictionaries
# my_value={}
# print(type(my_value))

# my_value=dict()
# print(my_value)

# student={"name":"jungkook","age":30,"grade":"A","brand":"BTS"}
# print(student)
# print(type(student))

# # accessing dictionary element
# student={"name":"jungkook","age":30,"grade":"A","brand":"BTS"}
# print(student['age'])
# print(student['grade'])
# print(student['brand'])

# # accessing using get() method
# student={"name":"jungkook","age":30,"grade":"A","brand":"BTS"}
# print(student.get('grade'))
# print(student.get('age'))
# print(student.get('python'))
# print(student.get('python',"programming"))

# # modifying dicitonary element
# student={"name":"jungkook","age":30,"grade":"A","brand":"BTS"}
# student["age"]=28  #update the value and kay
# print(student)
# student["address"]="korea"  #add key and value
# print(student)
# # delete key and value pair
# del student["grade"]
# print(student)

#dictionary methods
# student={"name":"jungkook","age":30,"grade":"A","brand":"BTS"}
# keys=student.keys()   #get all the keys
# print(keys)
# values=student.values()    #get all value
# print(values)
# items=student.items()  #get all key values pairs
# print(items)

# shallow copy
student={"name":"jungkook","age":30,"grade":"A","brand":"BTS"}
# student_copy1=student.copy()
# print(student_copy1)
# print(student)

# student["name"]="namjoo"
# print(student_copy1)
# print(student)

# iterating over dictionaries
# you can use loops to iterate over dictiontries,keys,values.or items
# iterating over keys
for keys in student.keys():
    print(keys)
    
# itreating over values
for value in student.values():
    print(value)
    
# itreating keys value pair
for key,value in student.items():
    print(f"{key}:{value}")
    
# nested dictionaries 
# days{
#    "tea":{"redlebal":"evning","place":"dehli"},
#    "cafe":{"americano":"lunch","place":"new york"}
#    }
# print(days)

# access nested dictionaries elements
# print(day["cafe"]["place"])
# print(day["tea"]["redlebal"])

# itreating over nested dictionaries
# for tea_id,tea_info in days.items():
#     print(f"{tea_id}:{tea_info}")
    
    
    
  
    







