# Introduction to React and Components

## Component-based Architecture

Components encapsulate functionality and behaviors of an element making them *reusable* and self-deployable.

-design decomposed into individual functional or logical components that represent well-defined communication interfaces containing methods, events, and properties.

- provides a higher level of abstraction and divides the problem into sub-problems, each associated with component partitions<sup>[^1]</sup>

Advantages:

- reduction in time; market and development
- reliability increase with reuse of exisiting components

### What is a component?

Components are modular, portable, replacable and reusable set of functionalities that encapsulate its implementation and export it as a high-level interface.

- software object that interacts with other components
- unit of composition with specified interface and explicit context dependencies only; can be deployed independently

### Component Views

<details><summary> Classes Overview</summary>classes are groups of objects with common properties, operations, and relationships to other objects and meanings. Analysis classes can be thought of as classes that have to do with the real world (ex: people, physical things, locations etc).Design classes are classes within the context of the software itself.[^3]
</details>

<br>
Object-oriented view: set of collaborating classes. Problem domain (analysis) and infrastructure (design) classes identify attributes and operations to that apply its implementation. Interfaces are defined enabling classes to communicate and cooperate. 

Conventional-view: functional element that integrates the processing logic and internal data structures to perform its task, as well as the interface that allows for calling the component and passing data to it.

Process-related view: system builds from existing components from our library. 

1. What is a “component”?
 
    - Components are modular, portable, replaceable and reusable set of functionalities that encapsulate its implementation and export it as a high-level interface.

2. What are the characteristics of a component?

    - reusability
    - replaceable
    - not context specific
    - extensible
    - encapsulated
    - independent

3. What are the advantages of using component-based architecture?

    - components are more time efficient, reusable and reliable.

## What is Props and How to Use it in React

In react components communicated (send data to each other) by using **props**: properties, used for passing data from one component to another.

Props are passed in a *unidirectional flow* (one way parent to child)

- props data is read-only, child components should not change them

1. What is “props” short for?
    - keyword for used for properties, pass data from one component to another.
2. How are props used in React?
    - They are used to create dynamic components
3. What is the flow of props?
    - one way direction, data passes only from parent to child components


[Component-Based Architecture](https://www.tutorialspoint.com/software_architecture_design/component_based_architecture.htm)
[What is Props and How to Use it in React](https://itnext.io/what-is-props-and-how-to-use-it-in-react-da307f500da0#:~:text=%E2%80%9CProps%E2%80%9D%20is%20a%20special%20keyword,way%20from%20parent%20to%20child)

[Component-Level Design: Definition & Types](https://study.com/academy/lesson/component-level-design-definition-types.html#:~:text=In%20the%20object%2Doriented%20view,do%20with%20the%20real%20world.)