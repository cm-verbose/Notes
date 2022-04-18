# Console
The **`console`** is a JavaScript **`Object`** that can help us debug code with many features. The console varies depending on which **browser** (or runtime environment) you use but it has the **same properties** (some supported more than others). 

## Methods 
These are some of the methods of the **`console`** : 


--- 
## console`.assert()`
Like the word assertion, the **`assert()`** method of the **`console`** checks if the experssion contained within is true. If the expression is truthy, then it returns `undefined`, otherwise, it returns an error (**`Assertion failed`**).

### Example : 
```js
console.assert(1 === 2) 
// Assertion failed
console.assert(1 > 0.5)
// undefined
```


---
## console`.clear()` 
Clears the console (clears all previous logs, tables etc. in the console)


---
## console.`context` (chrome)
Lists all the methods of the **`console`** Object. Equivalent to : 

```js
console.log(console); 
```
