# Type conversion
Type conversion just means to switch a value's **type** by using a **function**, so that it can be used with your program with the same data types. This is why certain blocks of code cannot work, such as this one : 

```py
a = input("Type a number"); 
b = a + 2
print(b)

# Traceback (most recent call last):
# File "main.py", line 2, in <module>
#   b = [What you typed] + 2
# TypeError: can only concatenate str (not "int") to str
```

In order to fix this error, we can use the functions mentionned earlier which are : 
  - **`str()`** : Converts value to a string (text)
  - **`int()`** : Convert value to an integer (number)
  - **`float()`** : Converts value to a float (number with decimals)
  - **`bool()`** : Converts value to a Bolean (True or False)

In this case, we can fix this issue with the **`string()`** function to convert your number to a string: 

```py
a = input("Type a number"); 
b = str(a) + 2
print(b)
```
