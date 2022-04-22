# Example 1, without type conversions
a = input("Type a number"); 
b = a + 2
print(b)

# Traceback (most recent call last):
# File "main.py", line 2, in <module>
#   b = [What you typed] + 2
# TypeError: can only concatenate str (not "int") to str


# Example 1, with type conversions
a = input("Type a number"); 
b = str(a) + 2
print(b)
