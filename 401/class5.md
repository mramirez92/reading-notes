# 5. Linked Lists

## Linked lists 

A Node is a data structure that stores a value that can be of any data type and has a pointer to another node

*linked lists* are nodes connected/linked with each other. Nodes references the next node in link.
- Singly - Singly refers to the number of references the node has. A Singly linked list means that there is only one reference, and the reference points to the Next node in a linked list.
- Doubly - Doubly refers to there being two (double) references within the node. A Doubly linked list means that there is a reference to both the Next and Previous node.
- Node - Nodes are the individual items/links that live in a linked list. Each node contains the data for each link.
- Next - Each node contains a property called Next. This property contains the reference to the next node. 
  
- Head - The Head is a reference of type Node to the first node in a linked list.
- Current - The Current is a reference of type Node to the node that is currently being looked at. When traversing, you create a new Current variable at the Head to guarantee you are starting from the beginning of the linked list.
- 
ex: [node1 has value: 4 next: node 2] [node 2 value: 8 node:3] [node 3 value: 15 next: null] node 3 has next as null because its the end of our list
    - node 1 is our `Head`
    - this list is a singly 
    - O(1)

### Moving around, traversing

`for` loops cant be used. We use `Next` value in each node to guide us to where the next reference is pointing. This allows us to extract data.
`while()` loops allow us to continuously check next node is in the list and not null. `null` will crash/end our program. 
`Current` tells us where we are in our linked list, allowing us to move foward until the end. 

Traversal Big o
- Time for `Includes` = 0(n) when we are traversing/moving through a linked list we will look in every node until we find what we need (n). Time increases as the search keeps going. 
- Space for `Includes` = O(1) because we are traversing the linked list we are already being given, linear (doesnt grow)

### Adding Nodes

Adding O(1) 
Link/node need to be properly assigned.  
With O(1), we replace the current `Head` (first node) with the new node.
- adding a new node to the beginning of list will always be O(1) because it takes the same amount of time/ resources to add new node. 

Adding O(n)
Time: Adding to the middle of the list is going to shift nodes around, re-allocate to make room for the new node. 

When adding before with `AddBefore`
    - time: O(n), while loop will run until we get to our target destination
    - space: O(1), no outside space needed we only need what is given to us in the input. 

### Prinint nodes
we use a while loop to check that we are not at the end of a linked list, we move current to next node until we reach null (end of link list)

## Big O: Analysis of Algorithm Efficiency

Big O describes the efficiency of an algorithm or function based on 2 factors:
    - Running time(time efficiency/complexity); running time
    - Memory space (space efficiency/complexity); amount of resources needed

4 key areas to consider an algorithms limiting factors:
1. Input size
        - accounts for size of each parameter value. High input size increases the *running time* and *memory space*

2. Units of Measurement
    Running time:
    - Start to finish execution of function in milliseconds
    - number of *operations* executed, line of code top to bottom
    - number of *basic operations*  executed, the most time consuming operation
    Memory Space
    - space needed to hold code for algorithm, storage size
    - space needed for input data storage
    - space needed for output data storage
    - space needed for work performed during calculations

3. Orders of Growth 
   - *constant complexity* runs linear, always using the same amount of time and space no matter the input.
        - reaches element directly
        
```python
#O(1)
sum(a, b)
total = a+bd
return val

```
- *logarithmic complexity* as our input increases complexity decreases, 
  - ex: when you eat food, your food goes through a digestion process, breaks down little by little, traversing many systems to get the nutrients or waste to the right destination. 
  - ex: binary search worst case: looks at array for an element, splits the array in two and searches for element in each until found, if the element is not found the process repeats until the element is found with each iteration becoming smaller and more precise. 

- *linear complexity* growth, the size of inputs determine *memory space* and *running length*, common with loops or recursive algorithms. 
    -like filling a pool, the bigger the pool the more water and time it will take to fill

4. Best Case, Worst Case, and Average Case
    - worst case: longest run, example: connecting flights, with long layovers...like southwest
    - best case: most efficient, ex: direct flight
    - average case: assumptions, ex: direct flight, without assigned seats could get window seat, could get front of plane, they still give you inflight snacks. 


📔[Back to Main Page](README.md)