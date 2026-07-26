# default parameters .;0p;         

def num_sum(a=1,b=1):
     print(a*b)
     return a*b
    
(num_sum()) 
    
def num_sum(a=1,b=3):
    print(a*b)
    return a*b
    
num_sum()

#PRACTICE QUESTION
# WAP to print of length of a list(list is the parameter)
                                       
citize=["delhi","malkapur","indore","mumbai","pune","banglore"]
# name=["talya","aporva","jackon","moon","lily"]

def print_len(list):
    print(len(list))
  
print_len(citize)
  
print_len(name)
  
  
# WAF to print th e element of a list in asingle line(list is the parameter)
  
name=["talya","aporva","jackon","moon","lily"]


def print_list(list):
    for item in list:
        print(item ,end=" ")
    
print_list(name)

# WAF TO FIND FACTORIAL OF N.N(N IS THE PARAMETERS)
 
# n=5
# fact =1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

def sys_fact(n):
    fact =1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)

sys_fact(6)

# WAF TO COVERT USD AND INR

def converter(usd_val):
    inr_val=usd_val*93
    print(usd_val,"usd=",inr_val,"inr")

converter(10)


# HOMEWORK QUESWTION

n=(int(input("enter num")))
if(n 2),
    print("odd")
else:
     print("even")

























































































