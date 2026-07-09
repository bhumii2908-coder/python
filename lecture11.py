# variable lenght arguments
# positional and keywords arguments

# def print_numbers(*lily):
#     for number in lily:
#         print(number)
        
# print_numbers(1,2,3,4,5,6,7,8,9,"lily")

# positional arguments
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1,2,3,4,5,6,7,8,9,"lily")  

# keywords arguments
def print_dealits(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
print_dealits(name="lily",age="32",address="indore")        


def print_dealits(*args,**kwargs):
    for valu in args:
        print(f" positonal arument {valu}")
        
    for key,value in kwargs.items():
         print(f"{key}:{value}")    
        
print_dealits(1,2,3,4,5,6,7,8,9,"lily",name="lily",age="32",address="indore")  
# return statments
def multiply(a,b):
    return a*b,a
   
multiply(2,3)

