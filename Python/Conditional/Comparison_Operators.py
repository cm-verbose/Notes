# Greater than operator
x = int(input('Enter an integer\n')) 
if x > 5:
  print(f'{x} is greater than 5')
  print(x > 5)
else: 
  print(f'{x} is smaller than 5') # Note that this will run if the number is equal to 5
  print(x > 5)
      
# Smaller than operator
print(7 < 4) # False

# Greater than or equal operator
  print(7 >= 3) # True
  print(4 >= 4) # True
  print(2 >= 3) # False
  
# Smaller than or equal operator
print(2 <= 3) # True
print(2 <= 2) # True
print(5 <= 3) # False

# (is) Equal operator
print(5 == 5) # True
print(6 == 7) # False

# (is) Not equal operator
print(not 6 == 6) # False
print(6 != 6) # False
