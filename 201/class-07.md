# Object-Oriented Programming

## Why is this important

## Domain Modeling

Domain modeling is the process of creating a conceptual model in code for a specific problem. A model describes the various entities, their attributes and behaviors, as well as the constraints that govern the problem domain.<sup>[^1]</sup>

1. Domain modeling allow us  to apply same properties across many objects efficiently.

## HTML Tables

1. Using tables as HTML layout reduces accessibility, tables produce tag soup, and they are not automatically responsive.
<sup>[^2]</sup>

2. td: table cell, table data, tr: table row, th: table header
th: at the top of row or colum, describe whats in the cells and rows.

# Constructors

Constructors

```JavaScript
 let ConstructorName = function (uniqueParameter1, uniqueParameter2) {
  this.uniqueParameter1 = uniqueParameter1;
  this.uniqueParameter2 = uniqueParameter2;
}
```

- special type of function
- acts like a blueprint/factory for objects
- starts with keyword "function" and named with capital letter
- storing data inside properties allows any new created object can access that data later.
- instantiate objects, properties are initialized when constructor is called

```JavaScript
let Person = function(name, age) {
  this.name = name;
  this.age =age;
}
// new creates new object that initializes functiion from Person constrctor using this variables
new Person = [monica, 30];

```

why:

- keeps our code dry
- prevents bugs

1. Constructors allow us to store properties that many objects can access.<sup>[^3]</sup>

2. this allows us to use same method for every object we create.

### Prototypes

- **inherits** === prototypes

Prototypes allows us to access data stores in Constuctors and apply them to our objects.<sup>[^4]</sup>

### Things I want to know more about

I want to understand more about DOM.

[^1]: Reference [domain modeling](https://github.com/codefellows/domain_modeling#domain-modeling)

[^2]: Reference [html table](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics)

[^3]: Reference [constructors](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics#what_is_this)

[^4]: Reference [prototypes](https://ui.dev/beginners-guide-to-javascript-prototype)

📔[Back to Main Page](../README.md)
