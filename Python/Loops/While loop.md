# While loop
A **`while loop`** is a loop that executes a block of code multiple times while a condition is **`True`**. It is created using the **`while`** keyword, then followed by the condition and then inside the loop, there is usually some code to increment an index to tell the while loop to stop when that index is reached. For example : 

```py
i = 0 
while i <= 3: 
  print(i) # prints 1, then 2, then 3
  i += 1 # Incrementing i such that it can reach 3 and not print infinitly
print("hello") # This line of code will run after that the loop is finished
```

# `break`
The `break` optional keyword is used to break the loop, in other words, it stops executing the current loop. This can be useful if you are checking something, usually if it is true or false, using a conditional `if`. For example : 

```py
i = 0 
while i < 5: 
  if i == 4:
    print("This number is ${i}")
    break # Here the loop will finish when i = 4
  print(i) # This statement will be ran before that i = 4
```

# `else` 
The `else` optional keyword is used to run additional code, if the loop finished successfully, without the `break` keyword breaking the loop. It will not run if the loop is not finished completely and can be used as such : 

```py
i = 0 
while i < 5:
  print(i)
else: 
  print("The loop finished successfully") # This statement will be ran
```
