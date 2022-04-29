# Comparison Operators
The comparison operators are operators that compare the value of two `numbers` (`float` and `int` types), returning a **boolean value** depending on the operators and the numbers. They can be useful for checking if for example, a user has a name that has more than two characters but has less than 50 characters. Here are some of the comparison operators that are present in Python : 

- `>` : Greater than operator
  This operator checks if the first number of the provided values is greater than the second. If it is not greater than the second, then this boolean expression will become false. **Note that if the numbers is equal, this expression will return `False`** For example : 
  ```py
    x = int(input('Enter an integer\n')) 
    if x > 5:
	    print(f'{x} is greater than 5')
	    print(x > 5)
    else: 
	    print(f'{x} is smaller than 5') # Note that this will run if the number is equal to 5
	    print(x > 5)
  ```
 
 - `<` : Smaller than operator
  This operators checkes if the first number of the provided values is smaller than the second. This works like the greater than operator. 
    ```py
    print(7 < 4) # False
    ```
 
- `>=` : Greater than or equal to operator 
  This operator checks the values of the two numbers and returns `True`, either by being equal or that the first number is greater than the second. It is false if it is smaller. This can erase some of the issues with two equal numbers with the greater than operator. 
  ```py
    print(7 >= 3) # True
    print(4 >= 4) # True
    print(2 >= 3) # False
  ```
  
- `<=` : Smaller than or equal to operator 
  This operator checks, like the greater than or equal operator, the values of two numbers. It returns the boolean value `True` is the first number is smaller than or equal to the second. This also erases some of the issues with the operator. 
  ```py
  print(2 <= 3) # True
  print(2 <= 2) # True
  print(5 <= 3) # False
  ``` 
  
 - `==` : Equal operator 
  This operator checks if both numbers are equal. Remember that it has two equals, unlike the assignment `=`. 
    ```py
    print(5 == 5) # True
    print(6 == 7) # False
    ```
  
- `!=` : Not equal operator 
  This operator can be thought as the inverse of the equal operator, checking if two numbers that are **not equal**. For example, these two staments below are equal : 
  ```py
  print(not 6 == 6) # False
  print(6 != 6) # False
  ```
