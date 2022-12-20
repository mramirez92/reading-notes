# Data Structures and Algorithms

Data Structures: organizing/storing data in computers to perform operations more efficiently.

1. arrays
   - fixed-size, same data type 
   - indexed
   - Traverse: Go through the elements and print them.
   - Search: Search for an element in the array. You can search the element by its value or its index
   - Update: Update the value of an existing element at a given index
   - Used for different sorting algorithms such as insertion sort, quick sort, bubble sort and merge sort.

2. Linked lists
   - A linked list is a sequential structure that consists of a sequence of items in linear order which are linked to each other.
   - elements = nodes 
     - nodes are made up of key and next pointer that points to successor "next"
       - last element called tail

3. Stacks
   - LIFO, last element accessed first "stack of plates"
    - push: insert element to the top
    - pop: delete topmost element and return it

4. Queues
    - FIFO, first element accessed, "first person in line, next, next"
    - priority queuing
   
5. Hash Table
   - key, value pairs 
   - Used to implement database indexes.
   - Used to implement associative arrays.
   - Used to implement the “set” data structure.

6. Trees
   - hierarchical structure where data is organized hierarchically and are linked togethe

7. Heaps
    - parent nodes are compared to their children with their values and are arranged accordingly
   
8. Graphs 
   - A graph consists of a finite set of vertices or nodes and a set of edges connecting these vertices.
   - The order of a graph is the number of vertices in the graph. The size of a graph is the number of edges in the graph.
   - Two nodes are said to be adjacent if they are connected to each other by the same edge.

## Disscution
1. What is 1 of the more important things you should consider when deciding which data structure is best suited to solve a particular problem?
   - It is important to identify the type data you are going to be storing, how and when you need to access it.

2. How can we ensure that we’ll avoid an infinite recursive call stack?
   - You need to stop the function from running with the implementation of a base case 

## Resources

[8 Common Data Structures every Programmer must know](https://towardsdatascience.com/8-common-data-structures-every-programmer-must-know-171acf6a1a42)

📔[Back to Main Page](README.md)