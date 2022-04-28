# Conditional 
Conditional statements can be written in Python with the `if`, `elif` and `else` keywords. `if` and `elif` tests if a value, if evaluated, correspond to the boolean `True` or `False`. This permits us to the program to make choices depending on the values that it receives. Here are a few examples for the usage of a conditional statement (also known as `if` statement) :

## `if`
The `if` keyword is a mandatory keyword, which is used to introduce the conditional statement. Only the `if` statement can introduce these statements. The if statement is then followed by a condition, the expression we want to test it's truthiness and then followed by a colon. Here is an example of `if` statement to check if the number that we entered in an input is smaller than `0.5` : 

```py
number = float(input("Enter a number\n"))
if number < 0.5: 
  # Don't forget your tab here 
  print(f"{number} is smaller than 0.5"); # If I would of typed "0.3" for example, it would return here : "0.3 is smaller than 0.5"
  # This is because that 0.3 < 0.5 evaluates to True in Python

print("Program finished") # Here, this line of code will always run, but not always the if statement, if it evaluates to False
```

## `elif`
The `elif` keyword is an optional keyword, which is used to add another to test if the first one evaluates to `False`. This statement will again test if the condition is `True` or if it is false. If it is false, like the `if` statement, the code inside of it will not run. We can add another test to see if the number is greater than `0.25`, or any value you want in this case : 

```py
number = float(input("Enter a number\n"))
if number < 0.5:
  print(f"{number} is smaller than 0.5")
elif number < 0.25:
  print(f"{number} is smaller than 0.25")
```

If you have tested the program before, you'd know that something is wrong here. That is that the `elif` statement is not executed, and that we only get that the number we have entered is smaller than `0.5`. This is because that an `if` statement will automatically end when one of the conditions is met. So in this case, we need to re-write this program as : 

```py
number = float(input("Enter a number\n"))
if number < 0.25:
  print(f"{number} is smaller than 0.25") # 0.1 is smaller than 0.25
elif number < 0.5:
  print(f"{number} is smaller than 0.5") # 0.45 is smaller than 0.5
```
Note that this will only return one print statement. 

## `else` 
The else statment is a statement that gets run if every conditional statements preceding it has returned `False`, or failed. There are no other conditions after the else statement, because it's the very end of the `if` statement. There are also no conditions for the `else` statement, due to it being that last statement. Here is an example of this else statement, to say something is the number is not smaller than `0.25` and `0.5` : 

```py
number = float(input("Enter a number\n"))
if number < 0.25:
  print(f"{number} is smaller than 0.25")
elif number < 0.5:
  print(f"{number} is smaller than 0.5")
else: 
	print(f"{number} is bigger than 0.5 and 0.25") # 0.6 is bigger than 0.5 and 0.25
```

# Logical operators
Logical operators in Python are operators that can modify or compare the properties of Booleans, or the `True` or `False` values in multiple ways. The basic logical operators are `and`, `or`, and `not`. Here is a guide on how to use them. 

## `and`
The `and` keyword checks if both boolean values are `True`. If one of the statements is `False`, then it returns `False`, otherwise, it will return `True`

```py
is_mean = True
is_very_mean = True

if is_mean and is_very_mean:
  print("This person is mean >:D") # is_mean and is_very_mean are checked here, in this case both are true so this print will work
```

```py
is_mean = True
is_very_mean = False

if is_mean and is_very_mean:
  print("This person is mean >:D") # Here, the print statement will not work because is_very_mean is False
```

# `or`
The `or` keyword checks if atleast one of the boolean values is `True`. If one of the statement is true, then the expression returns `True`. If neither of them are true, then it returns `False`. For example : 

```py
is_mean = True
is_very_mean = False

if is_mean or is_very_mean: 
  print("This person is mean >:D") # Here the print statement will work because is_mean is true
```

# `not`
The `not` keyword changes the bolean value to it's inverse. So for example, `not True` would be `False`, and `not False` would be `True`. Here is an example : 

```py
print(not True) # False
print(not False) # True
```
