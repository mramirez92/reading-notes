# Chart.js, Canvas

## Why is this important:

Rendering our data in a more visualizing and appealing manner can create a better user experience.

## JavaScript Canvas

`<canvas>` element that allows you to draw 2D graphics using JavaScript. Set width and height attributes. Size and width can be done through inline styling, DOM.

```HTML
<canvas width="500" height="300" id="canvas"></canvas>
```

Render context:  `getContext()` takes in one argument. 
`2d` 2D rendering context allows you to draw shapes, text, images, and other objects <sup>[^1]</sup>

1. Canvas allows us to draw 2d graphics.

2. Content between the opening and closing tags is fallback content that will display only if the browser doesn’t support the <canvas> element

3. getContext() gets the drawing context for drawing graphics on canvas.

## Chart.js Documentation

Create a chart from Chart.js by having an `<canvas>` node to render chart. 

Add chart script to our page. 

Render chart by creating a window to the DOM

1. Chart.js is an open source library that allows to use JS plugins  that creates charts.

2. Bar, area and line charts.

## Animated Charts with Chart.js

Attach chart script to our HTML
`<script src='Chart.min.js'></script>`<sup>[^3]</sup>

Create a canvas element in HTML
`<canvas id="buyers" width="600" height="400"></canvas>`

Create a window to DOM

```JavaScript
  var buyers = document.getElementById('buyers').getContext('2d');
    new Chart(buyers).Line(buyerData);
```

Create data

```JavaScript
var buyerData = {
	labels : ["January","February","March","April","May","June"],
	datasets : [
		{
      fillColor : "rgba(172,194,132,0.4)",
			strokeColor : "#ACC26D",
			pointColor : "#fff",
			pointStrokeColor : "#9DB86D",
			data : [203,156,99,251,305,247]
		}
	]
}

```

1. We can compare and display data more easily.

2. It could improve readabitly of some of our data and allows to more easily compare them.

## Things I want to know more about:
I want to play around with different charts and their settings.

[^1]: Reference [Canvas](https://www.javascripttutorial.net/web-apis/javascript-canvas/)

[^2]: Reference [Chart.js](https://www.chartjs.org/docs/latest/)

[^3]: Reference [Chart.js](https://www.webdesignerdepot.com/2013/11/easily-create-stunning-animated-charts-with-chart-js/)

📔[Back to Main Page](README.md)