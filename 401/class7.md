# 7. Scopes

## This is important because

Understanding scopes will helps understand how python works. This will help us write code that is efficient, easier to debug and dryer. 

## Scopes Basics

LEGB rule: Scopes determine the visibility of a variable within the code. 
- depended on where variable is created
- Local, Enclosing, Global, and Built-in
- where can you access that *name*, who can see it

Global scope: available to all code
- in scope

Local scope: only available/visible to code it resides in
- out of scope

! name is referring to identifiers of variables, functions, classes etc. etc

Namespaces: python scopes are implemented as dictionaries that map names to objects. 
- stored in `.__dict__' attribute


example: 
after importing sys, .keys() is used to inspect `sys.__dict__` keys. 
```python
import sys
>>> sys.__dict__.keys()
dict_keys(['__name__', '__doc__', '__package__',..., 'argv', 'ps1', 'ps2'])
```

referencing namespaces with dot notation or using a subscription operation to access 
```python
>>> sys.ps1
'>>> '
>>> sys.__dict__['ps1']
'>>> '
```

## LEGB Rules for Scopes

Local scope(function): 
- resides in code block or any function
- visible to code of function

Enclosing(nonlocal) scope: 
- inside nested functions, inner functions. 

Global scope:
- mr. world wide
- top-most scope in program, script, or module.

Built-in scope
- automatically loaded when script is ran or an interactive session is opened
- built in keywords, functions, exceptions and attributes

!!!! When searching for name, python searches for that name in sequential order of LEGB.

### Functions: Local Scopes

Local scopes are created at function calls
- each `def` statement = new local scope
- local scope is destroyed once function returns, names are forgotten. R.I.P.

Inspect names and parameters of a function with `.__code__` which holds information on functions internal code. 

```python
>>> square.__code__.co_varnames
('base', 'result')
>>> square.__code__.co_argcount
1
>>> square.__code__.co_consts
(None, 2, 'The square of ', ' is: ')
>>> square.__code__.co_name
'square'
```

### Modules: Global Scope

We enter the global scope immediately with main's script turned into a module called `__main__` that holds our programs' execution. 
- `if __name__ = "__main__"`
  - interpreter executes code in this module or script that serves as en entry point to program. "gateway"
- use `dir()` without an argument to get list of names living in global scope

Only one global scope per program execution, existing until program is terminated and all of its names forgotten :(
- Write self-contained functions that rely on local names rather than global ones.
- Avoid global name modifications throughout your programs.
- Use global names as constants that don’t change during your program’s execution.

## Things I would like to know more about:
I would like to watch that big o video 

## References: 

[LEGB](https://realpython.com/python-scope-legb-rule/#globals)