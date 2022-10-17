# Arrow functions

alternative but limited way to write functions. 

- dont have bindings to `this`, arguments or super. DONT USE AS METHODS!
  - unsuitable for call, apply and bind methods
- cant use `new.target`
- cant use `yield` within body

```JavaScript
// traditional:
function (a) {
  return a +100
  };

// arrow
a => a + 100;

```

Braces {} , parentheses () and `return` are required in cases where you have multiple arguments or no arguments:

```JavaScript
// traditional
(function (a, b) {
  return a + b + 100;
});

// Arrow Function
(a, b) => a + b + 100;

const a = 4;
const b = 2;

// Traditional Anonymous Function (no arguments)
(function() {
  return a + b + 100;
});

// Arrow Function (no arguments)
() => a + b + 100;

```
``` JavaScript
// Traditional Anonymous Function
(function (a, b) {
  const chuck = 42;
  return a + b + chuck;
});

// Arrow Function
(a, b) => {
  const chuck = 42;
  return a + b + chuck;
};
```

Named functions are treated like variables

```JavaScript
// Traditional Function
function bob(a) {
  return a + 100;
}

// Arrow Function
const bob2 = (a) => a + 100;
```

Simple expressions:
  - return is not needed
  - multiple parameters require parenthesis 
  ```Javascript
  (param1, param2) => expression
  ```
<br>

Multiple line statements:

- require body braces and returns
- multiple params and statements require ( ) and { }, respectively

Line breas between `=>` and its parameters cause errors, line break after `=>` are okay