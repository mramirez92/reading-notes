# 9. Functional Programming

## Why is this important:

Modules allow us to componentize our backend code.

## Functional Programming

What is functional programming?

-  the process of building software by composing pure functions, avoiding shared state, mutable data, and side-effects

What is a pure function and how do we know if something is a pure function?

- a function that always returns the same result if the same arguments are passed

What are the benefits of a pure function?

- precise and simple: take input give output. 

What is immutability?

- values whose content cant be changed without creating new value 

What is Referential transparency?

- a function can be replaced by its value, for the same result

----

## Modules

What is a module?

- code blocks that have specific functionalities for our applications

What does the word ‘require’ do?

- it read a file , executes and returns exported object

How do we bring another module into the file the we are working in?

-  `require(moduleName)`

What do we have to do to make a module available?

-  `module.exports = moduleName`

### Things I want to know:

More modules!!! having  functions on one page and having the ability to call them anywhere is amazing.

### Resources

[Functional Programming](https://medium.com/the-renaissance-developer/concepts-of-functional-programming-in-javascript-6bc84220d2aa)
[Modules](https://www.youtube.com/watch?v=xHLd36QoS4k)

📔[Back to Main Page](../README.md)