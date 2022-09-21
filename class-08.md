# 08. CSS Layout

## Why is this important?

Css layout is important because it will allow to create a better page flow and a better user experience. 

##  CSS Flexbox

Flexbox is a layout mechanism designed for laying out groups of items in one dimension.[^1]

- can display as a row, or a column.
- respect the writing mode of the document.
- single line by default, but can be asked to wrap onto multiple lines.
- items in the layout can be visually reordered, away from their order in the DOM.
- space can be distributed inside the items, so they become bigger and smaller according to the space available in their parent.
- space can be distributed around the items and flex lines in a wrapped layout, using the Box Alignment properties.
The items themselves can be aligned on the cross axis.

### Main Axis and Cross Axis

Main Axis:
 
- set by *flex-direction* property.
- !!!! flex items move as group

Cross Axis:

- Other direction of main axis, so this would by vertical while main is running horizontal?

- You can move the items individually or as a group so they align against each other and the flex container. Also, if you have wrapped flex lines, you can treat those lines as a group in order to control how space is assigned to those lines.

Flex-Container Creation:

1. Provides us  greater control over alignment and space distribution between items within a container.

2. Main axis is defined by the flex-direction property, and the cross axis runs perpendicular to it.

3. Reordering only happens for the visual order, not the logical order.

## More Flexbox


*</section>* element becomes a flex container and its children to become flex items [^2]

```css

/*flex is shorthand*/
section {
  display: flex;
}
/*items centered horizontally and vertically*/
div {
  display: flex;
  align-items: center;
  justify-content: space-around;
}
```

1. Flexbox allows us to center a block of content inside parent,children of a container take up an equal amount of the available width/height, regardless of how much width/height is available,
columns in a multiple-column layout adopt the same height even if they contain a different amount of content.

2. This will help me create a more user friendly experience and create  pages that have a greater flow and look a lot better.

[^1]: Reference [Learn CSS](https://web.dev/learn/css/flexbox/#what-can-you-do-with-a-flex-layout)

[^2]: Reference [More Flexbox](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox)

## Things I want to know more about

This, I want to practice it and see it in action. 

📔[Back to Main Page](README.md)
