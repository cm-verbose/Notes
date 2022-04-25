# Arithmetic operations 
Arithmetic operations are operations that have effect on numbers. Many of these operators, we already know, such as **addition**, **substraction**, **multiplication** * **division** and so on. In Python, there are these same operators that we can use on numbers. Here is a list of them. 

- ## Addition
  The addition operator `+` can be used to add 2 numbers. Be careful with it, because it can also concatenate two strings. 
  ```py
  ans = 10 + 9 
  print(ans) # 19 
  ```
- ## Substraction
  The substraction operator `-` can be used to substract 2 numbers. 
  ```py
  ans = 9 - 10
  print(ans) # -1 
  ```
- ## Multiplication
  The mutliplication operator `*` can be used to multiply 2 numbers. 
  ```py
  ans = 9 * 10
  print(ans) # 90
  ```
- ## Division 
  The divion operator `/` divides two numbers. 
  ```py
  ans = 8/9
  print(ans) # 0.8888888888888888
  ```
  
- ## Floor division 
  The floor division operator `//` divides the number and then floors it. Thus `1//2` is equivalent to `floor(1/2)`. 
  ```py
  ans = 30 // 9 # 3
  print(ans)
  ```

- ## Modulo operator
  The modulo operator is like the division operator but it returns the remainer of the division. Think of it as `x mod y`. 
  ```py 
  ans = 10 % 5
  print(ans) # 0 
  ans = 10 % 6
  print(ans) # 4
  ```
 
- ## Exponentiation
  The exponentiation operator `**` raises a value `x` to a value `y` giving thus x<sup>y</sup>. Note that it can also take roots of numbers with decimal exponents.
  ```py
  ans = 5 ** 5
  print(ans) # 3125
  ans = 81 ** 0.5
  print(ans) # 9.0
  ```

## Augmented Assignment operators 
Augmented Assignment operators help us write assingment of a variable while performing a an operation on the variable we want. Here are some of the operators that have augmented assignments to them : 

- ## Addition
  The `+=` performs addition on two numbers and assigns them. In this case, `x += y` is equal to `x = x + y`, which is longer to write out then the augmented assignement. 
  ```py
  ans = 5; 
  ans += 14
  print(ans)  # 19
  ```

- ## Substraction
  The `-=` performs substraction on two numbers where they are reassigned.
  ```py
  ans = 5; 
  ans -= 14
  print(ans)  # -9 
  ```

- ## Multiplication
  The `*=` performs mutliplication on two numbers where they are reassigned.
  ```py
  ans = 5
  ans *= 14
  print(ans) # 70
  ```
  
- ## Division
  The `/=` performs division on two numbers where they are reassigned.
   ```py
  ans = 5
  ans /= 14
  print(ans) # 0.35714285714285715
  ```
  
- ## Floor Division
  The `//=` performs floor division on two numbers where they are reassigned.
  ```py
  ans = 5
  ans //= 14
  print(ans) # 0
  ```

- ## Modulo
  The `%=` performs modulo division on two numbers where they are reassigned.
  ```py
  ans = 5
  ans %= 14
  print(ans) # 5
  ```
  
- ## Exponentiation
  The `**=` performs exponentiation on two numbers where they are reassigned.
    ```py
  ans = 5
  ans **= 14
  print(ans) # 6103515625
  ```

## Operator Precedence
Operator Precendence allows for the arithmetic operations that we run to follow the exact same rule as in mathematics. So if you remember them correctly, in order operations follow this order : 
  - Parenthesis
  - Exponentiation & Roots
  - Multiplication & Division
  - Addition & Substraction
  
Here is an example of a mathematical expression that is correctly solved using operator precedence : 
```py
expr = (5 - 3) * 234 ** 2 + 4 
# 2 * 234 ** 2 + 4
# 2 * 54756 + 4
# 109512 + 4
# 109516
print(expr) # 109516
```

## Math Module 
The Python module is a module that we can import in order to compute mathematical expressions that are more complex. Here, a module is a file that contains valid python code and that can be used to simplify our code by writting less in the main file. [Here](https://docs.python.org/3/library/math.html), you can find a list of all functions contained within this module and it's usage.

  
