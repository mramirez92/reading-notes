# Local Storage and How To Use It On Websites

## Why this is important:

Adding local storage to our web apps will allow a smoother user experience. Users will not have to readd previously set settings if the settings are stored locally. 


## Data Persistence

## Local storage

keep a key on the user’s computer and read it out when the user returns.<sup>[^1]</sup>

- stored on our hard drives
- specific to one computer

- session storage, clears when browser closed

 Use local storage by modifying localStorage object in JS.

- object that our browser give our js file to use.

- Data is stored as a string
  - JSON - JavaScript Object Notation
  - `JSON.stringify();` makes data into strings
    - changes data, strips away any functions or usage of constructors. objects wont know they can inherit constructor properties and methods

### Methods

- `localStorage.setItem(key,value)`: Store items and update
  - when item already exists, you can override its value by setting it again "update"

- `localStorage.getItem(key)`: get items

- when items retrieved are strings, run JSON.parse

- `localStorage.clear()`

- `localStorage.removeItem(key)`

- `JSON.parse()` : When receiving data from a web server, the data is always a string.
Parse the data with JSON.parse(), and the data becomes a JavaScript object. <sup>[^2]</sup>

``` JavaScript
// text from web server: '{"name":"John", "age":30, "city":"New York"}'
//JSON.parse() converting it to js object:
const obj = JSON.parse('{"name":"John", "age":30, "city":"New York"}');
```

1. To store user settings and non-sensitive  information next user accesses web application
2. sensitive info should not be store in local storage
3. local storage stores data as strings, use JSON.parse to convert it.

## Things I want to know more about:

I want to learn more about how exactly JSON.parse() works. 

[^1]: Reference [Local Storage](https://www.smashingmagazine.com/2010/10/local-storage-and-how-to-use-it/)
[^2]: Reference [w3schools](https://www.w3schools.com/js/js_json_parse.asp)

📔[Back to Main Page](../README.md)