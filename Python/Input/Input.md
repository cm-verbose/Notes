# Input 
We can require user input with Python using a built-in function (that means a function that is prebuilt into Python), in order to get data from the user. This function is the **`input()`** function. Inside it's brackets, we can write a prompt for the user to answer, and we can get the value back and use it. You can also chain multiple **`input()`** functions in order to ask multiple values. Here are some examples :

```py
name = input("What is your name ? \n") # here \n is a newline, so it puts the cursor at the next line
print("Hi " + name + " !") # if you had entered a name here, it will print out "Hi John", if you would have typed "John"
```

### Using multiple inputs 
We can use multiple `input()` staments to ask for multiple variables. You just need to define them with another variable. 

```py
name = input("What is your name ? \n")
age = input("What is your age ? \n")
print("Hi " + name + " you are " + age + " years old") 
# Returns both the age and name, for example if name = "John" and age = "22", it will return "Hi John you are 22 years old"
```
