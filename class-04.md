# 4. HTML Links, JS Functions, and Intro to CSS Layout

## "Why is this important?"

It is important to learn more about css styling to create a more user friendly experience. HTML structure is also important. 

## Creating Hyperlinks 

links are housed inside **<a>** elements and use **href** attribute. <sup>[^1]</sup>

- **title** attribute contains additional info about link; description of content paged linked contains

1. We wrap them in *<a>* tag

2.  *<href*>* attributes contains the actual link to file

3.  Using *<title>* tags will help us a description to a tag, allowing for more accessability. 

## CSS Layout Positioning

Positioning allows you to take elements out of normal document flow and make them behave differently, for example, by sitting on top of one another or by always remaining in the same place inside the browser viewport.<sup>[3]</sup>

- static: default

- relative: similar to static positioning, except that once the positioned element has taken its place in the normal flow, you can then modify its final position, including making it overlap other elements on the page

- top, bottom, left and right when used with positioning specifies where to to move element.

- absolute: out of normal document flow, sits in own separate layer from everything else.

  - example uses: popup boxes, control menu, rollover panels

1. Normal flow is default css flow

2. block level elements fills space of parent element containing it  and grows along the block dimension to accommodate its content. Inline elements is just size of their content. 

3. Static positioning is default positioning for every html element. 

4. Absolute positioning is great for elements that you don't need to be fixed into the page, they are elements that sit on top of other elements. useful for popup windows etc

5. Absolute positioning fixes an element in place relative to its nearest positioned ancestor, fixed positioning usually fixes an element in place relative to the visible portion of the viewport.


## Functions- Reusable blocks of code

functions allow our code to be efficient; keeps us from having to write redundant lines of code.

parameters are values that need to be inside the function parenthesis.

- are optional

consider where variables and other things are placed

- values defined inside scope of functions can't be used outside of that function; local scope<sup>[^4]</sup>

- values defined in global scope are accessible from anywhere in the code

1. When we declare function we are creating it. When we invoke a function we are calling it. Meaning are asking it to run. 

2. Parameters are place holders that live inside the parentheses in function. Arguments are what we pass in between parenthesis when we invoke function. 


```Javascript
// 'use strict'
// //function declarations
// // declarations are run on the first of of running JS fucntions declarations HOIST
// // var gets hoisted with declarations
// //
// //global scope is what lives outside of conditionals, loops, or functions. what do any other pieces of code need to know/access
greeting();
function greeting(){
//   // local scope is what lives inside here, applies to loops, conditionals too
console.log('hello');
}

// //function expressions are not hoisted like declarations are, 
// // functions expression
let newGreeting = function(){
  console.log('new greeting');
}
 newGreeting();


//using parameters=place holders that function is going to use 
function add(a,b){
  //console.log(a+b);
  //return brings what is returned to the forefront, store in variable to access it to use it elsewhere in a code. returns are for functions. 
//anything after return will not show, returns stop functions. 
  return a+b
}
//arguments are passed in function parameters, respectively 
add(2,3)

let mySum= add(2,3)//calling function above. the return will be saved in variable of mySum;
console.log(mySum);

```

## Pair Programming 

<sup>[^5]</sup>

Learning from fellow students is a great way to get new ideas and learn. They might have solutions for things I might need help with and vice versa. We can get feedback from each other.

The job readiness is going to help me tremendously. It will help me practice my communication skills.

## Things I want to know more about

I want to know more about HTML tag organization, where elements should be placed. 


[^1]: Reference [Creating Hyperlinks](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks)

[^2]: Reference [Normal Flow](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Normal_Flow)

[^3]: Reference [CSS Layout Positioning](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Positioning)

[^4]: Reference [Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)

[^5]: Reference[Pair Programming](https://www.codefellows.org/blog/6-reasons-for-pair-programming/)

📔[Back to Main Page](README.md)