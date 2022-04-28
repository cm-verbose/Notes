# if keyword

number = float(input("Enter a number\n"))
if number < 0.5: 
  # Don't forget your tab here 
  print(f"{number} is smaller than 0.5"); # If I would of typed "0.3" for example, it would return here : "0.3 is smaller than 0.5"
  # This is because that 0.3 < 0.5 evaluates to True in Python

print("Program finished") # Here, this line of code will always run, but not always the if statement, if it evaluates to False

# elif keyword

number = float(input("Enter a number\n"))
if number < 0.5:
  print(f"{number} is smaller than 0.5")
elif number < 0.25:
  print(f"{number} is smaller than 0.25")

# Single result explanation

number = float(input("Enter a number\n"))
if number < 0.25:
  print(f"{number} is smaller than 0.25") # 0.1 is smaller than 0.25
elif number < 0.5:
  print(f"{number} is smaller than 0.5") # 0.45 is smaller than 0.5
# Note that this will only return one print statement.

# else keyword

number = float(input("Enter a number\n"))
if number < 0.25:
  print(f"{number} is smaller than 0.25")
elif number < 0.5:
  print(f"{number} is smaller than 0.5")
else: 
	print(f"{number} is bigger than 0.5 and 0.25") # 0.6 is bigger than 0.5 and 0.25

# Logial operator and 

is_mean = True
is_very_mean = True

if is_mean and is_very_mean:
  print("This person is mean >:D") # is_mean and is_very_mean are checked here, in this case both are true so this print will work
is_mean = True
is_very_mean = False

if is_mean and is_very_mean:
  print("This person is mean >:D") # Here, the print statement will not work because is_very_mean is False

# Logial operator or

is_mean = True
is_very_mean = False

if is_mean or is_very_mean: 
  print("This person is mean >:D") # Here the print statement will work because is_mean is true

# Logical operator not

print(not True) # False
print(not False) # True
