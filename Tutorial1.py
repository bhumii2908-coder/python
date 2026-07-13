str1="This is a string"
print(str1)
str2="Notebook"
print(str2)
str3="""This is string"""
print(str3)

# "this isa python's tutorial
# 'this is pythin"stutorial'
str1="this is a sting \n we are creating in python."
print(str1)
str2="this is a drama.\t and we watching the drama"
print(str2)

# BASIC OPERATIONS
#CONCATENATION
str1="luxury"
str2="life"
finalstr= (str1+" "+str2)
print(finalstr)

str4="disney"
str5="land"
print(str4 + str5)

# length of str
str6="python online complier"
len6=len(str6)
print(len6)
print(str6)

str7="programiz"
len7=len(str7)
print(len7)

# INDEXING
str="friends"
print(str[3])

str="selfcare"
print(str[5])

#SLICING
str="success"
print(str[1:5])

str="travel"
print(str[2:len(str)])

# slicing negative index
str="space"
print(str[-5:-2])
 
 
# STRING FUNCTIONS
# str.endswith("er")
str="I am studing pythonfrom apnacollage"
print(str.endswith("age"))

str="Stop copy pasting code"
print(str.endswith("ode"))

#st.capitalize
str="bali is beautiful place"
str=str.capitalize()
print(str)

str="i like to traveling wrold "
str=str.capitalize()
print(str)

# str.replace (old,new)
str="python is a coding language"
print(str.replace("python", "java"))

str="you can use online complier"
print(str.replace("on","off"))

#str.find(word)
str="programiz a python is a online comiler it's platform using for coding"
print(str.find("online"))

str="python is very easy language"
print(str.find("is"))

# str.count("am")
str="i am from studing python form online compiler"
print(str.find("form"))

str="build the coding confide3nce then you become a coding master"
print(str.find("i"))

# practice queation
# WAP to input user's first name &print its length'
name=input("enter your name:")
print("length of your name is",len(name))

name=input("enter your name:")
print("length of your name is",len(name))

# WAP to find the occurence of $ in a sting
str ="i like the $ it is use for america i wish one day my bank accound number is $999.99999, in america $ is use for currrency"
print(str.count("$"))

# CONDITIONAL STATEMENT
# if-elif- else(syntax)
age=21
if (age >=18):
    print("can vote")
    print("can drive")  
    
marks=77
if (marks >=75):
    print("you are eligible for goverment schoolership")
  
#   elif  
light="green"
if (light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
    
passport="valid" 
if(passport =="invalid"):
    print("now you are not going india")
elif(passport =="invalid"):
    print("you are not going")
elif(passport =="valid"):    
    print("now you are going europe")
    
num=5
if(num>2):
    print("greater than 2")
if(num<3):
    print("less than 3")
    
# else
book="notes"
if(book =="exam"):
  print("examination")  
elif(book =="lib"):
    print("library")
elif(book =="subjects"):
    print("english,hindi maths")
else:    
    print("books notes are not availble")
 
#  tab called indentation   
age =14
if(age>=18):
    print("can vote")
else:
    print("cannot vote")
    
marks=int(input("enter student marks:"))
if (marks >=90 ):
    print("grade =A")
elif(marks >=80 and marks < 90):    
    print("grade=B")
elif(marks >=70 and marks<80):   
    print("grade=C")
else: 
    grade="D"
    print("the student grade -->",grade)
    
# nesting

age=14
if(age>=18):
        if(age >=80):
             print("cannot drive")
        else:
            print("can drive")
else:
        print("cannot drive")
    

# practice
# WAP to check if a number entered by the user is odd or even

 num = int(input("enter number:"))

rem= num % 2
if(rem == 0):
    print("even")
else:
    print("odd")

# WAP to find the greatest of 3 numbers entered by the user
    
a=int(input("enter first number:"))  
b=int(input("enter second number:"))  
c=int(input("enter thrid number:"))
  
if (a>=b and a>=c):
      print("first number is largest",a)
elif (b>=c):
      print("second number is lagest",b)
else:   
      print("third number is lagest",c)
      
#  WAP to check if a number is a multipul of 7 or not 
     
x=int(input ("enter number:"))
if (x % 7== 0):
      print("multiple of 7")
else:      
     print("not a multiple") 
     
  #  WAP to check if a number is a multipul of 9 or not 
        
x=int(input ("enter number:"))
if (x % 9== 0):
      print("multiple of 9")
else:      
     print("not a multiple") 
        
#  WAP to check whether a number is positive or negative 
   
num=int(input("enter number:")) 
rem = num % 2
if(rem == 0):
    print("positive")  
else:
    print("negative")
      
# check whether a number is greater than 10 or not      
      
a = int(input("enter a number"))
if(a>10):
    print("number greater than",a)
else:    
    print("number not greater than")  
    
#  check whether a number is zero not  
 
a = int(input("enter a number"))
if(a==0):
    print("number zero",a)
else:    
    print("number not zero")  
 
# campare two number and print greater number

a=int(input("enter first number:"))
b=int(input("enter second number:"))
if(a>b):
    print("greater  number",a)
else:
    print("greater  number",b)

#  check whether a student is pass or fail(pass marks 33
 
a=int(input("enter marks"))
if(a>=33):
    print("student is pass",a)
else:
    print("student is fail")
 
# check whether a person is child,teenager andadult based on age 
a=int(input("enter first age"))     
b=int(input("enter second age"))    
c=int(input("enter third age"))
if(a>=5):
    print("person is child")
elif(b>=11):
    print("person is teenager")
else:
    print("person is adult")
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      











    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    










































