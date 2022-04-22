# Using the right quotes
"John's wallet"
'As he said, "Hello world"'

# Multi-line Strings
a = """Hello 

This is a 

multi-line string
"""
print(a) 

# Hello
#
# This is a
#
# multi-line string

# Using both " and ' in the same string
quotes = ''' you can either use " or ' '''
print(quotes) # you can either use " or '


# Get single characters
text = "Python is fun"
print(text[0]) # P
print(text[1]) # y
# Notice that 0 is the first letter, 1 is the second and so on... 

# Get single characters starting from the end of a string
text = "Python is fun"
print(text[-1]) # n
print(text[-2]) # u
# Notice that here, we start at -1 which is the last character, all the way to the end

# Getting mutliple characters
text = "I love ducks"
print(text[2:6]) # love
print(text[7:12]) # ducks
# With this colon inside the brackets, we tell the interpreter to start at some index and return everything until a certain point
# For example in the second print, we get the character at the 7th index,
# "d" and return everything until the index  of the letter "s", or 12

# Ignoring conlon numbers
text = "I fix bugs"
print(text[:6]) # "I fix" 
print(text[2:]) # "fix bugs"
print(text[:]) # "I fix bugs"

# If you ignore the first number, it will start at the start of the string, or index 0, and end at your index
# If you ignore the second number, it will start at your index and end at the end of the string 
# If you ignore both numbers, it will return the entire string

# Using negative numbersw
text = "I ate apple"
print(text[-2:]) # "le"
print(text[:-5]) # "I ate"
print(text[-5:-2]) # "app"

# Formatted Strings
name = "John"
age = 12 
msg = f"{name} is {age} years old"
print(msg) # John is 12 years old

# Multi-line formated strings
name = "Bob"
dept = 4562.25
msg = f"""Hello {name}, 

It seems that you are in a dept of {dept}$
"""
print(msg)
# "Hello Bob, 
#
# It seems that you are in a dept of 4562.25$
# "

# len()
msg = "Hello World !"
print(len(msg)) # 13

# upper()
msg = "Hello World !"
print(msg.upper()) # HELLO WORLD !
print(msg) # Hello World !

# lower()
msg = "Hello World !"
print(msg.lower()) # hello world !
print(msg) # Hello World !

# find()
msg = "Hello World !"
print(msg.find("H")) # 0 
print(msg.find("h")) # -1 (here the string does not have a lowercase h, so it returns -1)
print(msg.find("World")) # 6

# replace()

msg = "Hello World !"
print(msg.replace("Hello", "Goodbye")) # Goodbye World !
print(msg.replace("W", "J") # Hello Jorld !
print(msg.replace("E", "a") # Hello World (there isn't a capital E here)
      
# in
msg = "Hello World !"
print("Hello" in msg) # True
print("Ducks" in msg) # False
