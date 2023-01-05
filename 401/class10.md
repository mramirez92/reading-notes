# 10. Stacks and Queues

## Stacks

A stack is a way to organize items in a certain order. It's like a stack of pancakes. When you make pancakes, you usually put them on top of each other in a stack. You can only add new pancakes to the top of the stack, and you can only take pancakes off the top of the stack. 
- most recent added node will be at the very top
- first node added will be positioned at the very bottom of a stack 
- stacks nodes only know about the top and their nodes only know about their next

Terminology:
- `push`: Nodes or items added are *pushed*
  - O(1) time complexity, same amount of time to push no matter the amount of nodes in our stack
  - new addition will have their next value set to the previous top value, their value is now the new top of stack 
  
- `pop`: Nodes or items removed, empty stack raises exception
  - O(1) time complexity, same amount of time to pop no matter the amount of nodes in our stack
  - popped off node is no longer in stack, meaning that the top most node(previously top's next) will be assigned as the new top

- `top`: top of stack
  - 
- `peek`: see value at the top of stack, exception is raised when stack is empty
  - O(1) complexity
  - inspecting top, not modifying anything
  
- `isEmpty`: return `True` when stack is empty
  - O(1)
  - check if stack is empty before peek
  

**FILO**
  First In Last Out
- first item is the last item popped out of a stack.

**LIFO**
Last In First Out
- last item in, first to be popped out

ex: 
input: `[a,b,c,d]`
stack:

| Position | Value    | Next       |
|----------|----------|------------|
| top      | value: d | next:c     |
|          | value: c | next: b    |
|          | value: b | next: a    |
|          | value: a | next: None |
|          | None     |            | 



## Queues 

Waiting in line, front of the line and back of the line. 

Terminology: 
- `enqueue`:  Nodes or items to be added to queue 
  - O(1) operation is performed the same no matter amount of nodes/items
- `dequeue`: Nodes or items that are removed from the queue, exception is raised when queue is empty
  - O(1), only adjustment is to the front of the line
- `front`: front/first Node of the queue
- `rear`: rear/last Node of the queue.
- `peek`: view front of queue value, empty queue raises an exception
  - O(1)
- `isEmpty` - returns true when queue is empty otherwise returns false.
  - O(1)

**FILO**
  First In Last Out
- first item is the last item popped out of a queue.

**LIFO**
Last In First Out
- last item in, first to be popped out

| Position: | Rear      |         |          | Front    |
|-----------|-----------|---------|----------|----------|
|           | value:4   | value:3 | value: 2 | value: 1 |   
| None      | next:None | next: 4 | next: 3  | next: 2  |