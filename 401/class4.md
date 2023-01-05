# 3. Classes and Object, More recursion

## Why is this important

Testing our code consistently will help development and productivity. Recursive algorithms can take complex problems and make them smaller and easier to manage. 

## Classes and Objects 

*Objects* hold variables and functions that come from *classes*
    - classes: template to create objects 

```python
class ClassName: 
    var = "string"
    
    def classFunc(self):
        print(var)

my_object = ClassName()
```

access variables/functions from class, use dot notation
`my_object.variable`

`__init__()` called when class is initiated, assigns values in a class

```python
class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'

```


## Recursion... again... and.... again....

iterative = explicit loop, loop till end is reached

```python
houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def deliver_presents_iteratively():
    for house in houses:
        print("Delivering presents to", house)
```

recursive algorithms divide work into smaller blocks to run more efficiently
    - solves simple cases, divides more complex problems into sub-problems and applies the same strategy to them. 
    - self-referential expressions

recursive functions will call itself and repeat its behavior until a condition is met to return a result. 
    - made up of *base case* and *recursive case*
    - recursive call adds to the stack frame (calls itself), until base case is reached. The function goes doesn't the stack returning its results
```python
houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

# Each function call represents an elf doing his work 
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)
```

```python
def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)

sum_recursive(1,0)
# returns 55
```

# Pytest

`pytest.fixture` 

## Things I want to know more about
I want grasp some of these testing concepts. 

## Resources

[Classes and Objects](https://www.learnpython.org/en/Classes_and_Objects)

[Thinking Recursively in Python](https://realpython.com/python-thinking-recursively/)

[Python Testing with pytest: Fixtures and Coverage](https://www.linuxjournal.com/content/python-testing-pytest-fixtures-and-coverage)
