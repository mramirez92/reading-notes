# 3. Passing Functions as Props

## Why is this important:

This can help us create dryer code and add functionality.

## Lists and Keys

You can build collections of elements and include them in JSX using curly braces {}.

Below, we loop through the numbers array using the JavaScript map() function. We return a <li> element for each item. Finally, we assign the resulting array of elements to listItems:

```Javascript
function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>
    <li>{number}</li>
  );
  return (
    <ul>{listItems}</ul>
  );
}

const numbers = [1, 2, 3, 4, 5];
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<NumberList numbers={numbers} />);
```

Keys identify which items have changed, are added, or are removed. Give elements inside array to give them a stable identity.
- Most often you would use IDs from your data as keys

```JavaScript
function ListItem(props) {
  // Correct! There is no need to specify the key here:
  return <li>{props.value}</li>;
}

function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>
    // Correct! Key should be specified inside the array.
    <ListItem key={number.toString()} value={number} />
  );
  return (
    <ul>
      {listItems}
    </ul>
  );
}
```

1. What does .map() return?

  - returns new array with its elements being the result of a callback function

2. If I want to loop through an array and display each value in JSX, how do I do that in React?

  - we use curly braces to embed an expression

3. Each list item needs a unique key.

4. What is the purpose of a key?

- key identifies item, makes them more stable. 


## Spread Operator ...

Spread operator: can be used for adding items to array, combining arrays/objects, and spreading an array out into a function’s arguments. It expands an iterable object, usually an array, though it can be used on any interable, including a string.

- copy array
- combine arrays
- be used for Math Functions
- used to pass array as arguments
- add item to list
- add state in React
- combine objects
- convert NodeList to an array

1 What is the spread operator?

- spread operator is used for expanding iterable objects

2. List 4 things that the spread operator can do.- 

- copy array
- combine arrays
- be used for Math Functions
- used to pass array as arguments

3. Give an example of using the spread operator to combine two arrays.

```JavaScript
const oddNum = [1, 3, 5];
const evenNum = [2, 4, 6];
const numList =[...oddNum, ...evenNum]
```

4. Give an example of using the spread operator to add a new item to an array.

```JavaScript
let animals = ['fish', 'bird'];
let moreAnimals = [...animals,'reptile'];
```

5. Give an example of using the spread operator to combine two objects into one.

```JavaScript
const objectOne = {pet= "dog"}
const objectTwo = {name: "skittles"}
const objectThree = {...objectOne, ...objectTwo, breed: "lab"};
```

## Pass Functions Between Components

1. In the video, what is the first step that the developer does to pass functions between components?

- create a function where the state is thats going to change.

2. In your own words, what does the increment function do?

- creates new array that updates counts based on the names that are passed in

3. How can you pass a method from a parent component into a child component?

-call the method in th parent component using this.props

4.How does the child component invoke a method that was passed to it from a parent component?
- pass it like any prop, using this. calling the method in the function residing in the parent.

## Things I want to know more about

I want to learn more about passing functions.

[Reference](https://reactjs.org/docs/lists-and-keys.html)
[Reference](https://medium.com/coding-at-dawn/how-to-use-the-spread-operator-in-javascript-b9e4a8b06fab)
[Reference](https://www.youtube.com/watch?v=c05OL7XbwXU)