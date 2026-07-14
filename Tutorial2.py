# LIST
marks1=54.2
marks2=66.3
marks3=33.32
marks4=53.81
marks5=88.1

marks=[54.2,66.3,33.32,53.81,88.156]
print(marks)
print(type(marks))
print(marks[0])
print(marks[3])
print(len(marks))

student=["arjun",95.4,18,"delhi"]
print(student[0])
student[0]="karan"
print(student)

marks=[85,66,43,85,77,86]
print(marks[1:5])
print(marks[:4])
print(marks[0:])
print(marks[-3:-1])
print(marks[-5:-2])

# LIST METHOD
#list.append()
list=[32,43,"lily","karan",77.4,"tilya"]
list.append("selena")
print(list)

list=[44.6,"zayn","gigi","kristen","nickloce",43,75,87.54]
list.append("songyoungi")
print(list)

#list.sort() asecnding
list=[555,76,99,654,89,2]
print(list.append(44))
print(list.sort())
print(list)

list=["karan"," pooja","priya","tina","meera"]
print(list.append("sarir"))
print(list.sort())
print(list)

# descending
list=[234,65,88,943,432,65,79,80]
print(list.append(43))
print(list.sort(reverse=True))
print(list)

list=["zayn","gigi","kristen","nickloce","songyoungi"]
print(list.append("lily"))
print(list.sort(reverse=True))
print(list)

# list.reverse
list=[10,37,42,12,15,6]
list.reverse()
print(list)

list=["maths","science","computer","comunication","artical"]
list.reverse()
print(list)

# list.insert
list=[3,4,6,7,8,9,5,]
list.insert(3,90)
print(list)

list=["arjun","anjali","dev","sameer"]
list.insert(1,"sara")
print(list)

# tuples in python
tup=(4,6,8,7,9,3)
print(type(tup))
print(tup[0])
print(tup[1])
print(tup[2])

tup=()
print(tup)
print(type(tup))

tup=(1,)
print(tup)
print(type(tup))

tup=(1,2,3,4,5)
print(tup[1:3])

# TUPLE METHODE
# tup.index
tup=(2,4,5,6,3,7,8,9)
print(tup.index(7))

# tup.count
tup=(2,3,5,6,8,9,1,3,1)
print(tup.count(1))

# practice questions
# WAP to ask the user to enter name of their 3 favorite movies & store them in a list
abc=[]
a=(input("enter first movie,"))
b=(input("enter second movie,"))
c=(input("enter third movie,"))

abc.append(a)
abc.append(b)
abc.append(c)

print(a,b,c)

# WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS (HINT USE COPY(METHOD))

list1=[1,2,2,1]
list2=[1,2,3,4]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("palindorome")
else:
    print("not polindorme")

list2=["m","a","a","m","p"]
-
copy_list2=list2.copy()
copy_list2.reverse()

if(copy_list2==list2):
    
    print("polindorme")
else:
    print("NOT polindorme")
    
#  WAP to count the number of students with the "A"grade in the following tuple
# ["C","D","D","A","A","B","B","A"]

grade=("C","D","D","A","A","B","B","A")
print (grade.count("A"))

# STORE THE ABOVE VALUE IN A LIST & SORT THEM FROM "A"TO "D"
grade=["C","D","D","A","A","B","B","A"]
grade.sort()
print(grade)

#DICTIONARY
info={
  "name":"pythontutorial",
  "class":3,
    "lecture":4,
    "studentname":"lily",
    "age":19,
    "rollno": 423.290,
    "enrollment":True,
    23.66 :5466
    
#     }
print(type(info))
# print(info)
print(info["name"])
print(info["rollno"])
info["studentname"] ="nick" #overwrite
info["coding"]="programiz"
info["enrollment"]="False"
print(info)

null_dict={}
null_dict["name"]="mack",
null_dict["groupname"]="got7"
print(null_dict)

# nested dictinaries
student ={
    "name" : "jackson wang",  
    "place" :{
        "india":2,
        "america":4,
        "korean":8,
        "china":5,
        "dubai":3
        }
    }
print(len(student))    
print(student["name"])
print(student["place"]["korean"])

# DIVTIONARY METHODS
# mydict.key()
 
   # DIVTIONARY METHODS
# mydict.key()
 
data={
    "name":"pythontutorial",
    "class":3,
    "platform":"programiz",
    "enrollment":22345776
}
print(len(data))
print(data.keys())

#mtDict.values()
collage={
    "name":"skilldeveloper",
    "couser":{
        "B.tech":972,
        "BBA":985,
        "MCA":332,
        "BCA":221,
        "B.com":994,
        "MBA":654
        }
}
print(list(collage.values()))

# myDict.items
platform={
    "programiz":"python",
    "W3school":"java",
    "frondend":"react",
    "backend":"javasript",
    "lecture":6,
    "tutorial":23
}
pairs=(list(platform.items()))
# print(list(platform.items()))
print(pairs[0])
print(pairs[3])

# myDict.get("key")
collage={
    "name":"skilldeveloper",
    "couser":{
        "B.tech":972,
        "BBA":985,
        "MCA":332,
        "BCA":221,
        "B.com":994,
        "MBA":654
        }
}
print(collage.get("name2")) #no Error--->none
print(collage["name2"]) #ERROR
    
# you can use:-
# print("BEFORE")
# print(collage["name"])
# print("AFTER")

# myDict.update(newDict)

collage={
    "name":"skilldeveloper",
    "couser":{
        "B.tech":972,
        "BBA":985,
        "MCA":332,
        "BCA":221,
        "B.com":994,
        "MBA":654
        }
}

# collage.update({"semester":8})
# print(collage)

new_dict={"city":"indore"}
collage.update(new_dict)
print(collage)

# you can add multiple key and values& you can change the value also
new_dict={"semester":8,"city":"indore","time":5,"name":"datadeveloper"}
collage.update(new_dict)
print(collage)

# SET IN PYTHON  ( ELEMENT UNIQUE AND IMMUTABLE)
#set is mutable but it element are not 

collection ={1,2,2,2,2,3,4,"hello","world","hello","hello","hello","hello"}
print(type(collection))
print(collection)
# set ignore duplicate value 

collection={} #empty dictionary {}this is use for dictionary
print(type(collection))

collection=set() # set() empty set it is use for set
print(type(collection))

# SET METHOD
#  set.add()
collection=set("a")
collection.add(43)
collection.add(678)
collection.add(789)
collection.add(55)
collection.add("hello")
collection.add("world")
collection.add(2.99)
print(collection)

# set.remove
info=set()
info.add("address")
info.add("name")
info.add("number")
info.add(23456789)
info.add(32)
info.add("programiz")
info.add("2.77")
info.remove("name")
info.remove(23456789)
print(info)
print(len(info))

# set clear()
collection=set()
collection.add(789)
collection.add(55)
collection.add("hello")
collection.add("world")
collection.add(2.99)

collection.clear()
print(len(collection))

# set.pop

student={"name","address","number","enrollment","python"}

student.pop()
print(student.pop())
print(student.pop())
print(student.pop())

# SET UNION(SET2)
# COMBINE BOTH SET VALUES AND RETURN NEW VALUE

set1={1,3,2,4,5,6,7,8}
set2={1,1,2,3,3,4,5,6}

print(set1.union(set2))   #{1,2,3,4,5,6,7,8}

# SET INTERSECTION(SET2)
# COMBINE COMMON VALUES AND RETURN NEW

set1={1,3,2,4,5,6,7,8}
set2={1,1,2,3,3,4,5,6}

print(set1.intersection(set2))


































































































































































































































































































































































































































































