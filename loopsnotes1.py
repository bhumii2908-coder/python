# BREAK
i=0
while i<=5:
    print(i)
    if(i==3):
        break
    i=i+1
    
print("ends of loop")


name=("meera","tina","anjali","maya","neha","lily","tara","megha","tina","jeera","sonu","monu")    
    
x="tina"
i=0
while i< len(name):
    if(name[i]==x):
        print("FOUND at i",i)
        break
    else:
        print("finding..")
    i=i+1   

print("end the list")


num=(23,34,45,56,67,78,89,45,3,44,55,67,8765,54,32,3)

x=67
i=0
while i<len(num):
    if( num[i]==x):
        print("found at ", x)
        break
    else:
        print("finding...")
    i=i+1

print("end the num")


name=("meera","tina","anjali","maya","neha","lily","tara","megha","tina","jeera","sonu","monu","maya","lily")

x="lily"
i=0
while i<len(name):
    if(name[i]==x):
        print(name[i])
        break
    else:
        print(name[i])
    i=i+1
print("list is closed")

# CONTINUE

i=0
while i<=10:
    if(i==5):
        i=i+1
        continue #skip
    print(i)
    i=i+1

i=0
while i<=10:
    if(i%2==0):
        i=i+1
        continue #skip
    print(i)
    i=i+1

i=0
while i<=10:
    if(i%2==0):
        i=i+1
        continue #skip
    print(i)
    i=i+1

# odd number print
i=0
while i<=10:
    if(i%2==0):
        i=i+1
        continue #skip
    print(i)
    i=i+1

# even number print
i=0
while i<=10:
    if(i%2 != 0):
        i=i+1
        continue #skip
    print(i)
    i=i+1

#  FOR LOOP IN PYTHON          

nums=[1,23,3,4,56,4,33,3,44,5,56,75,7,77,653,3,3,23,66]

for i in nums:
    print(i)
    
    
sub=("maths","chemistry","english","hindi","cloud engineering","opreating system","anroid","backend")  
    
for val in sub:
    print(val)
    
#  YOU CAN USE FOR LOOP IN TUPLES
tup=(1,2,3,4,5,6,7,8,9,10,12,21,23)   
 
for val in tup:
    print(val)
    
    
# YOU CAN PRINT STRING ALSO 
 
str=("programiz is a online compiler")


for char in str:
    if(char=="n"):
        print("n found")
        break
    print(char)

print("end")
    
# PRACTICE QUESTIONS

# print the elements od the following list using a loop
# [1,4,9,16,25,36,49,81,100]

list=[1,4,9,16,25,36,49,81,100]
for i in list:
    print(i)


# QUESTION2
# search for a number x in this tuple using loop[1,4,9,16,25,36,49,81,100]

nums=(1,4,9,16,25,36,49,81,100,25)
x=25

idx=0
for i in nums:
      if (i==x):
        print("number found at idx",idx)
        
      idx=idx+1








































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

























































































































































































