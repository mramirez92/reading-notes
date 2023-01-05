## class 2 notes

include 2 white spaces between functions!!!!!!!
tabs are important, defines function start and end

format in pycharm: ctrl/cmd + alt/option + L

ALL FUNCTIONS MUST CONTAIN SOMETHING, thats why we write `pass` when we create the function

return statements stop functions, just like js end all 

algo 
big 0 
time 0(n) each item must be visited
space 0(n) algo will run in linear state

Input/output: use short interesting cases, keep them simple, keep them small, keep them consistent
    - 0, 1, 2 
step through use table: what is step through 
- use one example to step through 
- keep variables in rows, steps over time place in column 
- line by line 
- input row 
- standard output below it, what happens when that variable is put through our function

return = output
- when return is missing return value is none 

print= console log 

***** code challenge you can use insert 
practice slow 
get it down 

python -m venv .venv = creates virtual environment, creating venv folder 
source .venv/bin/activate = run venv script 

python install package = pip
look at installed libraries and write them to this file: pip freeze> requirements.txt
these are local to the .venv being run, install in when inside .venv
`pip install pytest`
`pip freeze> requirements.txt`
`mkdir tests`

[//]: # tests needs __init__.py file jut empty()
`mkdir fizz_buzz`
[//]: # (packages require underscore in names)
`charm .` 

[//]: # in pycharm in fizzbuzz pacakge()
file: fizz_buzz.py

[//]: # ( py charm: in tests folder, test files must begin with test_ : test_fizz_buzz.py )
`import pytest `


## Resources 
real python website

## py test

script: file intended to run directly 

module: file intended to be imported into scripts or other modules 
    - if it ends in .py = module 
    - defines classes, functions, variables
packages: 
    - collection of modules working together to bring functionality 

TDD: test driven development
    - testing allows for better development and allows us to implement incremental changes as we work on code 
    - end goal in mind= test drives development
    - test all criteria to functions? 
    - naming conventions for tests name them what youre testing for to be as clear as possible 
    - when tests fail, think about what exactly the code is supposed to do before changing anything. 
        - DO NOT WRITE CODE JUST TO MAKE IT PASS. what is it that i need? what am i expecting?
### when testing in wsl 
to test:
`pytest`  

install library to test as code changes 
`pip install pytest-watch`
initialize pytest-watch
`pytest-watch`

## lab 02 
 
fibonacci number= recursive set of numbers where the previous two equal the present
next number in the series is the sum of the previous numbers in the series 
- first number want to be 0, because we index at zero 

take in integer return nth number in series

lucas numbers: start at 2 1 

write tests!!!!!! break things to understand


## Recursion 
recursive function is any function that calls itself, loop
needs base case, a break


