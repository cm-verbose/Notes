# Order of Execution
Python programs gets executed by a compiler from the **top** of the file to the **bottom** of the file. So that means that everything is read **line by line** from top to **bottom**. For example, take this example script : 

```py
print("1")
print("2")
print("3")
print("5")
print("4")
```

In order, this will return in the terminal : 

```py
1
2
3
5
4
```
This is because every **`print()`**  function in this script was written in this particular order. 
