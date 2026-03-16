# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
# def hello_func():
#   print("hello world!")
#   name = input("What is your name? ")
#   print("Nice to meet you,", name)

# function that takes parameters
# def hello_func(greeting):
#   print("hello world!")
#   name = input("What is your name? ")
#   print(greeting, name)

# hello_func("How are you doing?")
# hello_func("Hey what's up")

# function that returns a value
# def cube(x):
#   return x*x*x

# result = cube(3)
# print(result)

# function with default value for an parameter
# def hello_func(greeting="What's up", name=None):
#   print("hello world!")
#   if name == None:
#     name = input("What is your name? ")
#   print(greeting, name)

# hello_func()
# hello_func(name="Sarita", greeting="What's up")

# # function with variable number of parameters
# def multi_add(start, *args):
#   result = start
#   for x in args:
#     result = result + x
#   return result

# print(multi_add(10, 4, 5, 10, 4, 10))

import re
def remove_non_alphanumeric_re(text):
    return re.sub(r'[^a-zA-Z0-9]', '', text)



test_word = "Madam, I'm Adam."
print(remove_non_alphanumeric_re(str.casefold(test_word)))
print(remove_non_alphanumeric_re(str.casefold(test_word[::-1])))