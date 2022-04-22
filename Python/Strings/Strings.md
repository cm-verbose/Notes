# Strings 
Strings represent some text values in our program usually written with single quotes (`''`) or double quotes (`""`). But you have to use the same quotes in a pair in order to write the strings. So strings like **`"Hello'` don't work** in Python. If you want to use quotes inside of your strings, be careful of what the **string's quotes** are and what quotes you are trying to use. Here are examples of quotes you want to avoid : 

```py
'John's wallet'
"As he said, "Hello world""
```

Instead, use the right quotes in this situation : 
```py
"John's wallet"
'As he said, "Hello world"'
```

## Multiline Strings
These are strings that can span multiple lines and also register line breaks within the string. They are declared with three quotes (either `''' '''` or `""" """`). Here is an example on their behavior : 
```py
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
```
With these multiline Strings, we can also use both quotes inside the same string : 
```py
quotes = ''' you can either use " or ' '''
print(quotes) # you can either use " or '
```

## Characters
In Python, you can get certain characters from a string using brackets using a number. Let's see how this can be used : 

### Getting single characters

We can get a character within any position of the string : 
```py
text = "Python is fun"
print(text[0]) # P
print(text[1]) # y
# Notice that 0 is the first letter, 1 is the second and so on... 
```

We can also get a character starting from the end of the string :
```py
text = "Python is fun"
print(text[-1]) # n
print(text[-2]) # u
# Notice that here, we start at -1 which is the last character, all the way to the end
```

### Getting multiple characters

We can get a multiple characters with the `:` :
```py
text = "I love ducks"
print(text[2:6]) # love
print(text[7:12]) # ducks
# With this colon inside the brackets, we tell the interpreter to start at some index and return everything until a certain point
# For example in the second print, we get the character at the 7th index,
# "d" and return everything until the index  of the letter "s", or 12
```

We can also ignore the numbers inside the colons : 
```py
text = "I fix bugs"
print(text[:6]) # "I fix" 
print(text[2:]) # "fix bugs"
print(text[:]) # "I fix bugs"

# If you ignore the first number, it will start at the start of the string, or index 0, and end at your index
# If you ignore the second number, it will start at your index and end at the end of the string 
# If you ignore both numbers, it will return the entire string
```

Negative numbers are also allowed : 

```py
text = "I ate apple"
print(text[-2:]) # "le"
print(text[:-5]) # "I ate"
print(text[-5:-2]) # "app"
```

## Formated Strings
Formated Strings are strings that can have variables in them, usually to ease reading by avoiding concatenation. We declare formatted strings by using the string syntax, but preceding it with the letter `f`. For example : 

```py
name = "John"
age = 12 
msg = f"{name} is {age} years old"
print(msg) # John is 12 years old
```

This can also apply to mutli-line Strings :
```py
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
```

## String methods 
String methods are functions that you can apply on your strings to manipulate them.

### `len()`
This method gives you the number of characters in a string (space included) : 
```py
msg = "Hello World !"
print(len(msg)) # 13
```

### `upper()`
This method creates a new string and returns every letter in a string in uppercase :
```py
msg = "Hello World !"
print(msg.upper()) # HELLO WORLD !
print(msg) # Hello World !
```

### `lower()`
This method creates a new string and returns every letter in a string in lowercase : 
```py
msg = "Hello World !"
print(msg.lower()) # hello world !
print(msg) # Hello World !
```

### `find()`
This method finds the first apparition of a character (case sensitive) or string and returns the index at which it starts : 
```py
msg = "Hello World !"
print(msg.find("H")) # 0 
print(msg.find("h")) # -1 (here the string does not have a lowercase h, so it returns -1)
print(msg.find("World")) # 6
```

### `replace()`
This method finds the value inside it's parameter (the value you have given the function) in order to replace it with another string, case sensitive :
```py
msg = "Hello World !"
print(msg.replace("Hello", "Goodbye")) # Goodbye World !
print(msg.replace("W", "J") # Hello Jorld !
print(msg.replace("E", "a") # Hello World (there isn't a capital E here)
```

### `in`
This is not a method, but a keyword that can see if a certain value is in the string. If it is, it returns `True` or else `False`, so it is a bolean expression : 
```py
msg = "Hello World !"
print("Hello" in msg) # True
print("Ducks" in msg) # False
```
