# check If a string is palindrome
# def is_palindrome(s):
#     s=s.lower().replace(" ","")
#     return s==s[::-1]
    
# print(is_palindrome("A man a plan a canal Panama"))
# print(is_palindrome("Hello"))


# Calculate the factorial of a number using recursion
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n* factorial(n-1)
    
# print(factorial(6))
# print(factorial(5))


# A function to read a file and count the frequency of each word
# def count_word_frequency(file_path):
#     word_cont={}
#     with open(file_path,'r') as file:
#         for line in file:
#             words=line.split()
#             for word in words:
#                 word=word.lower().stripo('.,!?::"/')
#                 word_count[word]=word_count.get(word.0)+1
                
#     return word_count   
# filepath="your file name"
# word_frequency=count_word_frequency(filepath)
# print(word_frequency)
                