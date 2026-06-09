# loop
# for loop

range(10)
for a in range(10):
    print(a)

range(4,10)       #(start,stop)
for n in range(4,10):
    print(n)
    
for x in range(2,21,2):     #(start,stop,step)
    print(x)

# STRING
str="ashawqariya rai"
for n in str:
    print(n)

## while loop
# the whike loop continues to execute as long as the condition is true
count=0
while count<10:
    print(count)
    count=count+1
    
    
value=0
while value%2==0:
    print(value)
    value=value+1

## loop controll statment 
# break:- the break statment exits the loop permaturely

for m in range(10):
    if(m==8):
        break
    print(m)

for n in range(20):
    if n==10:
        break
    print(n)

##continue
# the continue statement skips the current iteration contunues with the next

for a in range(20):
    if a%2==0:
        continue
    print(a)


##pass
##the pass statement is a null opertion; it does nothing
for x in range(10):
    if(x==5):
        pass
    print(x)


##nested loopss
##a loop inside a loop

for n in range(4):
    for m in range(5):
        print(f"n:{n}and m:{m}")


# first 10 natrual numbers sum
# while loop
n=10
sum=0
count=1
while count<=n:
    sum=sum+count
    count=count+1
print(sum)   

# for loop'
num=10
sum=0
for num in range(11):
    sum=sum+num
print(sum)  

# prime number 

for num in range(1,101):
    if num >1:
        for i in range(2,num):
            if num%i==0:
                break
            else:
                print(num)


# rite a program that prints all the numbers from 1 to 10 using a for loop.

n=10
for n in range(11):
    print(n)
    
#  rite a program that prints all the numbers from 1 to 10 using a for loop.    
    
num=1
while num=10:
    num=num+1
print(num)    

    
    
    
    
    
    
    
    
    
    
    
    
