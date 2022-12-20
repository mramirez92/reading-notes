# 2.  Testing and Modules

## In Tests We Trust — TDD with Python

Unit tests are some pieces of code to exercise the input, the output and the behaviour of your code.

Write small tests that test code in small, bare ways

Be descriptive in what you expect and what you're testing. 

Structure with AAA:
    - arrange: organize data needed to execute input
    - act: execute code tested 
    - assert: check results match expectations 

Cycle:
    - fail test
    - pass test 
    - refactor code

Practice, practice,practice!

## if __name__ == “__main__”

Before executing code, Python interpreter reads source file and define few special variables/global variables
    - if that module is run: special __name__ variable to have a value “__main__”
    - if file is imported from another module: __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable. 
## Recursion

Recursive= continuously runs(loop), changing values that will eventually cascade down.
    - this breaks down the problem into smaller problems
    - needs a base condition to break a loop

## Things I want to know more about
I want to learn how to test my code efficiently and practice writing recursive code more. 

## Resources 

[In Tests We Trust — TDD with Python](https://code.likeagirl.io/in-tests-we-trust-tdd-with-python-af69f47e6932)

[if __name__ == “__main__”](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)

[What on Earth is Recursion](https://www.youtube.com/watch?v=Mv9NEXX1VHc)

📔[Back to Main Page](README.md)