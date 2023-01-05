# 8. List Comprehension

## This is important because:
Clean code is easier to read than code that is convoluted and long. This something I want to master. 

## Write Cleaner Code With List Comprehension
List comprehensions are a way to create and modify lists in Python. They allow you to perform tasks such as constructing lists using the range() method, creating lists using loops, multiplying parts of a list, filtering lists based on conditions, and working with strings. They are generally more efficient and concise than using for loops and are a useful tool when working with lists in Python.
- more concise 
- compact way of creating lists
- flexible

Example of code reduction using list comprehension:
```python
# create a list using list comprehension
squares = [x**2 for x in range(10)]

print(squares)
```

- code above appends the results for each number squared in the given range. 
- removes need for multiple lines

```python
even_numbers = [ x for x in range(1,20) if x % 2 == 0]
# output [2, 4, 6, 8, 10, 12, 14, 16, 18]
```

passing arguments to list comprehension: 

```python
def double(x):
    return x*2

nums = [double(x) for x in range(1,10)]
print(nums)
```

## Resources

[List Comprehension](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)

## Things I want to know more about:
I want to write more code usin list comprehension, its a learning curve, but its is extremely beautiful. 