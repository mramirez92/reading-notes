# Transform, Transitions and Animations

## Why is this important:

User experience is important and so is user
engagement. 

## Transform

transform property comes in two different settings, two-dimensional and three-dimensional

Elements may be distorted, or transformed, on both a two-dimensional plane or a three-dimensional plane. Two-dimensional transforms work on the x and y axes, known as horizontal and vertical axes. Three-dimensional transforms work on both the x and y axes, as well as the z axis. These three-dimensional transforms help define not only the length and width of an element, but also the depth. We’ll start by discussing how to transform elements on a two-dimensional plane, and then work our way into three-dimensional transforms.
<sup>[^1]</sup>

```CSS
div {
  -webkit-transform: scale(1.5);
     -moz-transform: scale(1.5);
       -o-transform: scale(1.5);
          transform: scale(1.5);
}
```

1. It allows them to transform them on any axis. 

2. You can use it to render a 3d object, maybe a globe to show positioning of store locations around the globe. 

## CSS Transitions & Animations

With CSS3 transitions you have the potential to alter the appearance and behavior of an element whenever a state change occurs, such as when it is hovered over, focused on, active, or targeted.<sup>[^2]</sup>

Animations: appearance and behavior element to be altered in multiple keyframes

- set multiple points of transition upon different keyframe

### Transitions

Transitions: change in state takes place, different styles have to be identified for each state.

- `:hover` `:focus` `:active` `:target`   pseudo-classes.

- `transition-property`: identifies specific properties that are going to be affected by transitions,all of the properties within an element’s different states will be altered upon change.

- `transition-duration`: transition timing set in seconds, milliseconds

- `transition-timing-function,`: sets speed of transition

  - `linear` `ease-in` `ease-in-out`

- `transition-delay`: sets a time value, seconds or milliseconds, that determines how long a transition should be stalled before executing

### Animations

Animations are more controlled.

use `@keyframes *animation name*` to declare animation elements.

```CSS
.stage:hover .ball {
  animation-name: slide;
  animation-duration: 2s;
  animation-timing-function: ease-in-out;
  animation-delay: .5s;
}
```

1. Transitions: provide change from one state to another. 

2. Transitions provide a change from one state to another, while animations can set multiple points of transition upon different keyframes.

## More Transitions

Effects are hardware accelerated and can be used immediately.
`trasition`

- fade in: set initial state, then set change. Ex: opacity changes
- grow and shrink by changing scale of element
  - scale larger than 1 to grow, less than 1 to shrink

```css
transform: scale(1.3);
```

- rotate by setting `transform: rotatez(#deg)`
- square to circle and vice versa: elementhover with a border radius change
- inset border: no background color, heavy border
```CSS box-shadow: inset 0 0 0 25px #53a7ea;```<sup>[^3]</sup>

1. Transitions make a page more dynamic creating a better more exciting user experience.

2. Transitions can increase user engagement. That they could spend more time on my website/app.

## Things I want to know more about:

I want to learn how exaclty to implement animations. 


[^1]: Reference [Transforms](http://learn.shayhowe.com/advanced-html-css/css-transforms/)

[^2]: Reference [Transitions & Animations](https://learn.shayhowe.com/advanced-html-css/transitions-animations/)

[^3]: Reference [CSS Transitions](http://www.webdesignerdepot.com/2014/05/8-simple-css3-transitions-that-will-wow-your-users)