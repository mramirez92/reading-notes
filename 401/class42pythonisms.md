# 42. Pythonisms

## Dunder Methods

🪄"magic methods"🪄 that  allow instances of a class to interact with the built-in functions and operators in python. 

**`__init__` **:constructor takes care of setting up the object 

**`__str__`** :printable string representation of an object

**`__repr__`** The “official” string representation of an object. This is how you would make an object of the class

```Python
class Account:
    # ... (see above)

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(
            self.owner, self.amount)
```

**`__call__`**: make an object callable like a regular function, downside of this method on your objects is that it can be hard to see what the purpose of calling the object is.

## Iterator

**`__iter__`**:  used to iterate through items in class methods, returns any object with the __next__ method

**`__next__`**: object that can be accessed one element at a time

## Generators

Generator functions are syntactic sugar for writing objects that support the iterator protocol. Generators abstract away much of the boilerplate code needed when writing class-based iterators

``` Python
def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value
```

Yield vs. Return: 
- return: **disposes of a function’s local state**, permanently passes control back to the caller of the function
- yield: **suspends the function and retains its local state**, passes control back to the caller of the function—but it only does so _temporarily_
	-  local variables and the execution state of the generator function are stashed away temporarily. 

## Things I want to know more about:

I work with dunder methods more,  i find myself googling a lot how to print a binary tree class. 

## Resources 

[Dunder Methods](https://dbader.org/blog/python-dunder-methods)

[Python Iterators](https://dbader.org/blog/python-iterators)

[Python Generators](https://dbader.org/blog/python-generators)
