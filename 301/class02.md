# Class 02 Notes: React

## Why is this important:

It's important to learn more about React.

## React Lifecycle

Mounting, Updating, and Unmounting are the three phases of the component lifecycle.<sup>[^1]</sup>

Mounting:

When an instance of a component is being created and inserted into the DOM it occurs during the mounting phase.

Updating:
Anytime a component is updated or state changes then it is rerendered. These lifecycle events happen during updating in this order.

Unmounting:
The final phase of the lifecycle if called when a component is being removed from the DOM.

1. Based off the diagram, what happens first, the ‘render’ or the ‘componentDidMount’?
  
  - render

2. What is the very first thing to happen in the lifecycle of React?

  - Mounting

Put the following things in the order that they happen: componentDidMount, render, constructor, componentWillUnmount, React Updates

  - constructor, render, react updates, componentDidMount, componentWillUnmount

## React State Vs Props

What does componentDidMount do?

  - This method is invoked immediately after a component is mounted.

What types of things can you pass in the props?

- things you want your function to initialize, things you want to display in a component. props allow us to create dynamic components. 

What is the big difference between props and state?

- props can pass into a component(outiside); states are handled inside the component can be updated inside as well. 

When do we re-render our application?

- we re-render when applications needs updating

What are some examples of things that we could store in state?
-things that constanstly need an update

## Things I want to know more about:
I want to know more about React in general.

[^1]Reference [React Lifecycle](https://medium.com/@joshuablankenshipnola/react-component-lifecycle-events-cb77e670a093)
[React Props vs States](https://www.youtube.com/watch?v=IYvD9oBCuJI)
