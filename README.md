# Object Oriented Programming and Functions
## Functions
A function is a block of code that only runs when it is 
called, and it carries out a single purpose. Functions
encourage the DRY (Don't Repeat Yourself) principle 
by reducing repetition and clutter in code.

A standard function
```python
# Calling the function will output the message.
def greeting():
    print("Welcome on board.")

# The function must be called to display the output
greeting()
```

A function taking in arguments
```python
def greeting(name):
    print("Welcome on board " + name + ".")

# Outputs "Welcome on board King."
greeting("King")
```

A function returning a value
```python
def sum_return(num1, num2):
    return num1 + num2

# Outputs 6
print(sum_return(2, 4))
```

### Use cases
* Allow sections of code to be reusable
* Reduces repetition of code
* Easier to find bugs
* When different arguments are needed for the same operations

### Best practices
* A function should carry out a single purpose
* Should be named based on its purpose