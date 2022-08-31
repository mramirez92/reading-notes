## Class Six Notes

## What is javascript?

JavaScript is a scripting language that enables you to create dynamically updating content, control multimedia, animate images, and pretty much everything else. 

a few features: 
- Stores useful values inside variables.
- create strings, concantenate strings\
- Running code in response to certain events occurring on a web page. We used a click event in our example above to detect when the label is clicked and then run the code that updates the text label.

![3 muskateers](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript/execution.png)

A very common use of JavaScript is to dynamically modify HTML and CSS to update a user interface, via the Document Object Model API. 

Application Programming Interfaces (APIs) provide you with extra superpowers to use in your JavaScript code.
- eady-made sets of code building blocks that allow a developer to implement programs 
- several types of API
  - Browser: built into your web browser, and are able to expose data from the surrounding computer environment, or do useful complex things
  - Third party APIs are not built into the browser by default, and you generally have to grab their code and information from somewhere on the Web

JavaScript is read from top to bottom, **order matters!**

**< script>**
  we need to add < script > to our html file in our < head> tag inorder to use JS.

### Variables

Variables are containers for storing data (storing data values).

- var: variables
- let: values that can be modified
- const: constant values and cannot be changed

variable must have unique identifiers:
- case sensitive
- can contain letters, digits, underscores, and dollar signs

the equal sign is an assignment operator. 

strings can contain numbers, letter, symbols and spaces. they are encased in between quotation marks

integers or number dont have quotation marks. 

Creating a variable in JavaScript is called "declaring" a variable.

let *variable name*

or

let *variable name* = *value*

It's a good programming practice to declare all variables at the beginning of a script.

You can declare many variables in one statement.

Start the statement with let and separate the variables by comma:

ex:
    let *name*= *monica*, *age*=*29*

Data types: 

- Strings: text inside single quotes, can be letters, symbols, numbers
- Boolean: True or False
- Numbers/integers

