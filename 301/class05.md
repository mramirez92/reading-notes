# 5. Putting it all together

## Why this is important:

Becoming familiar with React is important. 

## React

Step 1: Component planning

Single responsibility principle: component should do only one thing, big components should be decomposed into smaller subcomponents.

Ex:

- FilterableProductTable
  - SearchBar
  - ProductTable
    - ProductCategoryRow
    - ProductRow

Step 2: Static app

 Build a static app, pass data only with props and no states. One way data flow.

Step 3: State

For each piece of state in your application:

- Identify every component that renders something based on that state.

- Find a common owner component (a single component above all the components that need the state in the hierarchy).

- Either the common owner or another component higher up in the hierarchy should own the state.

- If you can’t find a component where it makes sense to own the state, create a new component solely for holding the state and add it somewhere in the hierarchy above the common owner component.



## Questions

1. What is the single responsibility principle and how does it apply to components?
    - to focus on doing a single thing

2. What does it mean to build a ‘static’ version of your application?
    - build a site without interactivity, no states

3. Once you have a static application, what do you need to add?
    - interactivity through passing of states.

4. What are the three questions you can ask to determine if something is state?
    - Passed from parents via props? = not state
    - data unchanged? = not state
    - can compute based on other state or props? = not state

5. How can you identify where state needs to live?
    - Aim for minimal representation of state, find common owners that need state in the hierarchy.

## Higher-Order Functions

Higher-Order Functions: functions that operate on other functions, either by taking them as arguments or by returning them.

1. What is a “higher-order function”?
    - Functions that operate on other functions, either by taking them as arguments or by returning them.

2. Explore the greaterThan function as defined in the reading. In your own words, what is line 2 of this function doing?
    - returning m if m is true or false

3. Explain how either map or reduce operates, with regards to higher-order functions. 

    - they transform an array by applying a function to all of the array elements while returning a new array with those values.

## Things I want to know more about:

I want to know more about reduce.

### References

[Thinking in React](https://reactjs.org/docs/thinking-in-react.html)

[Higher-Order Functions](https://eloquentjavascript.net/05_higher_order.html#h_xxCc98lOBK)


📔[Back to Main Page](../README.md)
