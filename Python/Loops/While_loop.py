# While loop

i = 0 
while i <= 3: 
  print(i) # prints 1, then 2, then 3
  i += 1 # Incrementing i such that it can reach 3 and not print infinitly
print("hello") # This line of code will run after that the loop is finished

# Break keyword

i = 0 
while i < 5: 
  if i == 4:
    print("This number is ${i}")
    break # Here the loop will finish when i = 4
  print(i) # This statement will be ran before that i = 4

# Else keyword

i = 0 
while i < 5:
  print(i)
else: 
  print("The loop finished successfully") # This statement will be ran
