# temperature converting
# def convert_temperature(temp,unit):
#     """this function converts temersture between celsius and fahrenheit"""
#     if unit=='C':
#         return temp * 9/5 + 32         #celsius to fahrenheit
#     elif unit=="F":
#         return(temp-32)*5/9             #fahrenheit to celsius
#     else:
#         return None
        
# print(convert_temperature(24,"C"))
# print(convert_temperature(45,"F"))
# print(convert_temperature("r","g"))


# password streght checker
def strong_password(password):
    if len(password)<8:
        return False
    if not any (char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$^&*_+' for char in password):
        return False
    return True    
    
print(strong_password("animE@c3b"))
print(strong_password("12345"))
print(strong_password("c3bA0&534^88"))


# calculate the total cost of item in a shooping cart
def calculate_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+= item['price']* item['quanity']
        
    return total_cost
        
#example cart data
cart=[
    {'name':'Apple','price':0.5,'quanity':5},
    {'name':'banana','price':0.6,'quanity':7},
    {'name':'Orange','price':0.8,'quanity':9}
    ]

# calling the function
print(calculate_total_cost(cart))
# print(total_cost)