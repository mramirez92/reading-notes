# Data Modeling 

## Constructor Function and Prototypes

ES6 classes

``` JavaScript

class Animal {
  // constructor
  constructor(name,legs){
    this.name= name;
    this.legs =legs;
  }
  // what would be prototypes that invoke constructors are now methods inside class. 
  walk(){
    this.isWalking =true;
  }
  eat(){
    this.isEating= true;
  }
}
//subclass of animal called Dog
 class Dog extends Animal{
  speak(){
    console.log('woof!');
  }
  }

let rosie = new Animal ('rosie',4);

console.log(rosie);
```

a more efficient way to create objects. Prototypes are inside of class as methods.
created a class called animal and a subclass called Dog. Because we added a method to subclass of Dog, we didnt have to call it because it its a child of Animal class. its an extension of Animal, which means it can participate in anything that lives in the Animal class. 

extends => typeof, belongs to 
