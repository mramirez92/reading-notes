# 3. Readings: HTML Lists, Control Flow with JS, and the CSS Box Model 

## "Why is this material important?"

There's so much information about these languages/tools. Continuos reading is needed to hammer in what I don't know.CSS is still an area where I am the least comfortable in, and that means I need to dive deeper into it.

## HTML

### Ordered lists

**<ol>** typically a numbered list include **<li>** element.<sup>[^1]</sup> Attributes:

- **reversed** item order reversed, numbered high to low.
- **start**  start counting from number specified.
- **type** sets number type:
  - **a** lowercase letters
  - **A** uppercase letters
  - **i** lowercase roman numerals
  - **I** uppercase roman numerals
  - **1** numbers (default)

### Unordered lists

**<ul>** unordered list; bulleted list.<sup>[^2]</sup>

- has to have **<li>** element.
- can be nested
- change bullet style by using **type=** attribute

```
<ul>
  <li>one</li>
  <li>two</li>
</ul>
```

1. use when order is meaningless, numerical order not needed.
2. using type attribute  
3. when order is important use ordered list
4. using type attributes, for example **a** lowercase letters **A** uppercase letters.

## Learn CSS: <sup>[^3]</sup>

HTML Elements win an id *<p id="different">*
are called in in css using *#id-name{}*

### Box Model

Everything in CSS is in a box. boxes have an inner display type and outer display type. type determines behavior and page flow in relation to other boxes.[^4]

use **display** property to set type of box.

Outer Display type:

Outer display type of **block**:

- box breaks onto new line
- width and height properties respected
- padding
- padding, margin and border will cause other elements to be pushed away from the box
- box fills space available in container, most always filling up 100% of space available.
- html elements that use **block** as outer display: h1 and p

Outer display type with **inline**:

- box doesn't break new line.
- vertical padding, margins, and borders. will apply causing other inline boxes to move away from it.
- html elements with inline: a, span, em, strong

```
<p>I am a paragraph. A short one.</p>

<p>I am another paragraph. Some of the <span class="block">words</span> have been wrapped in a <span>span element</span>.</p>
```

```
.block {
  display: block;
}    
```

Inner Display type:
Dictates layout of elements inside box.

- set by default lay out of normal flow, behave as block/inline boxes
- can change display box to **display: flex**

Parts of a box:

- Content box: where content displayed; size it using **inline-size, block-size, or width and height**

- Padding box: white space around content. **padding**
  - no negative padding
  -background displayed behind padding
  - **padding** property controls all sides, but sides can be controlled individually ex: **padding-top**

- Border box: wraps content and any padding **border**
  - four border sides: top, right, bottom, left.
  - size of border is added to width and height of box.

- Margin box: outermost layer, wrapping all of the above  as whitespace. **margin**
  - four margins sides: top, right, bottom, left. each can be style individually as well.
  - two positive margins combine to become one margin. size will be equal to largest individual margin.
  - two negative margins collapse, smallest (furthest from zero) value used.
  - one negative margin, subtracted from total.

![image from developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model/box-model.png)[^9]

1. Margin would be the big winter coat and padding would a sweater on the content.
2.

- Content box: where content displayed; size it using **inline-size, block-size, or width and height**
- Padding box: white space around content. **padding**
- Border box: wraps content and any padding **border**
- Margin box: outermost layer, wrapping all of the above  as whitespace. **margin**

## JavaScript

### Arrays

Arrays [^6] store list of data items under single variables. Each variable can be accessed individually.

- store multiple data types and can mix them.
  - strings
  - numbers
  - objects
  - arrays

```
const random = ['cats', 'dogs', 3, 5, [banana, apple]];
```

Arrays use *index* to label items, starts from left at 0. Call and modify items by using index.

```
const random = ['cats', 'dogs', 3, 5, [banana, apple]]; 
random[2] = 'birds'
console.log(random);
//random returns: ['cats', 'birds', 3, 5, [banana, apple]]
```

Accessing item inside array inside array, ha.

```
const random = ['cats', 'birds', 3, 5, [banana, apple]];
random[4][1];
//returns apple
```

```
const random = ['cats', 'dogs', 3, 5, [banana, apple]];
console.log(random.indexOf('dogs')), // 1
console.log(random[3]), // returns item on index 3 
console.log(random[0][1]) // return item at first index and second index returns item/character at that index within first called index--> 'a' from cats beacause cats is at index 0
```

can  add items or replace to array with:

**arrayName** [ *index* ]= *item-adding*

- if array index ends at 5 and were adding an item at index 7, index 6 in that array will now be an undefined value/item.
- if the index we are calling exists in the array, the item we are adding will replace it.

### Array properties

- **.length** tells us how many items are in our array

```
let food = ['appple', 'banana', 'mango', 'orange'];
console.log(food.length); 

// returns size of array-->4

console.log(food[food.length-1])

// if lenght is 4, that minus 1 takes length minus one returning item at that number 4-1=3, return at index 3. here it would be 'orange' 
```

**indexOf()** method:
helps find index of item by inserting item as parameter. returns index.

**push()** adding items to end of list, item has to be inside parenthesis

- can add more than one element, seperated by commas

- seperate items with commas

**unshift()** adds items to start of array

**pop()** removes last item in array

**shift()** removes first item in array

**splice(index, index-number)** remove a known item from array, call it using index as first parameter. second parameter how many items to be removed.

**for**(*variable* **of** *iterable*)
access every item in array.

**split()** split strings to separate items. parameter is where you want to split

### Loops: For and While

**For** is great for looping/iterating and doing something for a certain number of times

- great for looping arrays because they have length

```
for(starting value; condition increment){
  **do**something until that condition isn't true
}
```

```
let nums=[1, 2, 3, 4, 5];

for (let i=0; i<nums.length; i++){
  console.log(`items in my array ${nums[i]}`);
  }
  
    // console logs nums at each i iteration. at each loop, until conditions are no longer true
```

```
let friends= ['vicky', 'bridget','gaby'];
for (let i=0; i<friends.length; i++){
  if(friends[i]=== 'bridget'){
    console.log("homies for life");
  }
  else{
    console.log("yellooooowww!");
  }
  }
  /// logs yellooooowww!
homies for life
yellooooowww!

```

**While** loops repeat until no longer true, can create infinite loops
while loops will continue to run until answer is false

```
while(condition){
  codeblocks running until condition no longer true, 
```

```
let myNum=15; 
let userGuess = prompt('guess what number im thinking about, between 1 and 20');

while (userGuess != myNum){
  userGuess= prompt('Guess again');
}
```

1. Arrays store can store any strings, numbers, objects,  lists, other arrays
2. yes its a valid array, can access its store values by calling upon them by index and we can also store them in another array or variable.
3. Shorthand operators:

- += adds value of the right operand to a variable
- -= subtracts value of the right operand from a variable
- **= exponential; power of operand to the right applied to variable
- *= multiplies value of right operand to variable<sup>[^7]</sup>

4. Age verification can be used on a website. User authentication as well.

5. variables a and b are truthy, they are added. variable c is false (falsey) which is also equal to 0. So the answer would be  '10dog'

6. Loops allows to run a code block multiple times without having to repeat it each time.

## Things I want to know more about

I want to know how to manipulate elements more with CSS. There's a lot to learn, it can get overwhelming.

[^1]: Reference [ordered](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)

[^2]: Reference [unordered](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)
[^3]: Reference [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)

[^4]: Reference [Box-Model](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model)

[^6]: Reference [arrrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Arrays)

[^7]: Reference [Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators)

[^9]: Image[image from developer.mozilla](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model/box-model.png)

📔[Back to Main Page](README.md)
