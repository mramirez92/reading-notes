# 6. Problem Domain, Objects, and the DOM

## "Why is this important:"

This is important for aesthetics and readability of a page.

## Objects

Objects are collections of related data and/or functionality.<sup>[^1]</sup>They consist of variables and functions (properties and methods inside objects). Objects are made up of multiple *members*:

- Name and value pairs. Have to be separated by commas. comma separated key/value pairs
- Object member can be anything: array, function, numbers etc. 
- Data items are object **properties**
- Functions are called object **methods** they do something with object properties.
- 

```JavaScript
//array
let myArr = ['monica', 30, true];

//object 
let person = {
  name: 'monica',
  age: 30,
  texan: true,
}
```

### Object Literal 

``` JavaScript

const objName = { // declaring an object by giving it a name
  memberName1: memberValue1, //object members are anything inside curly brackets
  memberName2: memberValue2, 
};
```

```Javascript
const person = {
  name: ['Bob', 'Smith'],//property name/value pair 
  age: 32,// property; name/pair
  bio: function () { //method; function
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
  }, //logging properties defined above, using index to pass some elements in array
  introduceSelf: function () { //method; another function calling property above by index
    console.log(`Hi! I'm ${this.name[0]}.`);
  }
};
```
### Dot Notation

Dot notation is used to access whatever lives inside object.

- Object name must be entered followed by period(dot)  and then object property/method you want to access.

```JavaScript
objectName.property
objectName.method

person.name
person.name[0]
person.age
person.bio()
person.introduceSelf()
```

### Objects as object properties

```JavaScript
const person = {
  name: {
    first: 'Bob',
    last: 'Smith',
  },
  // …
};

person.name.first // call object "person",  call object "name" that lives inside object "person", access element "first" that is member of object "name"
```

### Bracket notation

Bracket notation is used to access objects as well.

- allows us to access members like we would with index numbers.
- objects map string to values in same way that arrays map numbers to values


```JavaScript
person[`age`] // access age property that lives inside person object
person[`name`][`first`] // access name and first property living inside object
```
### Setting object members

Setting (updating) the value of members by declaring the member you want to set:

```JavaScript

person.age = 45;
person['name']['last'] = 'Cratchit';

```

You can also create new members:

```JavaScript
person['eyes'] = 'hazel';
person.farewell = function() {
  console.log('Bye everybody!');
}
```
One useful aspect of bracket notation is that it can be used to set not only member values dynamically, but member names too. Let's say we wanted users to be able to store custom value types in their people data, by typing the member name and value into two text inputs. We could get those values like this:


const myDataName = nameInput.value;
const myDataValue = nameValue.value;

// we could then add new member name/value to person object like this:
person[myDataName] = myDataValue;

```

### This 

**this.** can be used in place of object name, this allows us to use the same method definition for every object we create.  

```JavaScript

// accessing object members 
objectName.objectMember
// short way, useful, and better when using constructors
this.objectMember

```

### Constructors

When we change properties of an object, we have to update EVERY object!
A constructor is just a function called use **new** keyword. Calling constructor:

- creates new object
- binds **this** to new object
- run code in constructor
- return new object
- start with capital letter, named for type of object they create.

```JavaScript
function Person(name) {
  this.name = name;
  this.introduceSelf = function() {
    console.log(`Hi! I'm ${this.name}.`);
  }
}
//call person
const salva = new Person('Salva');
salva.name;
salva.introduceSelf();

const frankie = new Person('Frankie');
frankie.name;
frankie.introduceSelf();

```

1. An object hold information and instructions on what to do with that information.

2. They can  are more efficient, you can call functions and the data types need more easily.

3. Array uses indexes, we would have to know the specific number associated with the element we need. With objects, we use the name. 

4. If an object property name is defined at runtime then you can't use dot notation to access the value, but you can pass the name as a variable inside brackets.

5. this refers to object members "name" and "age". This allows us to use the same method definition for every object we create.  

## Intro to the DOM

Document Object Model (DOM) is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects; that way, programming languages can interact with the page.[^2]

- its where HTML and CSS come together in the browser; JS reads this whole thing as an object.

A web page is a document that can be either displayed in the browser window or as the HTML source. In both cases, it is the same document but the Document Object Model (DOM) representation allows it to be manipulated. As an object-oriented representation of the web page, it can be modified with a scripting language such as JavaScript.

- Properties, methods, and events available for manipulating and creating web pages are organized into objects.
- Every HTML document and its contents are parts of the document object model . They can be accessed/manipulated using DOM and  scripting languages. 
- DOM was designed to not be proprietary to any programming language, allowing it to structural representation of document to be available from single consistent API
- **< script>** allows us to use API in JS from within.


### DOM MANIPULATION

``` Javascript
//js needs a window into your HTML or into the dom, letting js access DOM 
//step 1
let section= document.getElementById('my-section');

//2. create elements= h2Element = <h2></h2>
const h2Elements = document.createElement('h2');

//3. give it context if necessary
// <h2> hey im an h2</h2>
h2Element.textContent = 'hey! im an h2';

//4. add to dom, adding 
//parentElement.appendChild(child)
//adding(append child) h2Element to section; 
section.appendChild(h2Element);

```

1. DOM is an api that gives us access to HTML structure.

2. Elements that are part of the DOM can be accessed and manipulated with scripting languages like JavaScript. 

## Things I want to know more about

I want to know more about constructors and this. 

[^1]: Reference [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)

[^2]: Reference [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)

📔[Back to Main Page](README.md)
