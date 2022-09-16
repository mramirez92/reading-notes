# Class 04 Notes

```
// 'use strict'
// //function declarations
// // declarations are run on the first of of running JS fucntions declarations HOIST
// // var gets hoisted with declarations
// //
// //global scope is what lives outside of conditionals, loops, or functions. what do any other pieces of code need to know/access
// greeting();
// function greeting(){
//   // local scope is what lives inside here, applies to loops, conditionals too
//   console.log('hello');
// }

// //function expressions are not hoisted like declarations are, 
// // functions expression
// let newGreeting = function(){console.log('new greeting');
//                             }
// newGreeting();


//using parameters=place holders that function is going to use 
function add(a,b){
  // console.log(a+b);
  //return brings what is returned to the forefront, store in variable to access it to use it elsewhere in a code. returns are for functions. 
//anything after return will not show, returns stop functions. 
  return a+b
}

//arguments are passed in function parameters, respectively 
// add(2,3)

let mySum= add(2,3)//calling function above. the return will be saved in variable of mySum;
console.log(mySum);
```