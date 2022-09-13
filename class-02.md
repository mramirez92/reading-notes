# Class 02 Notes

## "Why is this material important?"

HTML, CSS, and JavaScript are all languages used to create a website. It is important to become familiar with JavaScript as it is a versatile language.

## Intro to HTML cont

HTML gives our text structure allowing the browser to display it how we want.

HTML structure:

- preferred to have only one \<h1> per page; top level
- keep headings in correct order.
  - ex: ,\<h3> should not come before \<h2>
- use no more than 3 heading levels per page.

Structure allows for readability, better searchability, accessability (screen readers), and CSS/JavaScript targeting efficiency.<sup>[^1]</sup>

### Semantics

Semantics help us label/ identify the function of elements. They are used by search engines and screen readers.

### Lists

Unordered **\<ul>**

- order doesn't matter.

```
<ul>
  <li>banana</li>
  <li>apple</li>
  <li>mango</li>
</ul>
```

Ordered **\<ol>**

- order matters.

```
<ol>
  <li>banana</li>
  <li>apple</li>
  <li>mango</li>
</ol>
```

Nested lists

```
<ol>
  <li>banana</li>
  <li>apple</li>
    <ul>
      <li>honeycrisp</li>
      <li>granny smith</li>
    </ul>
  <li>mango</li>
</ol>
```

### Emphasis and Importance

- \<em> : italic in html
- \<strong> : bold
- \<span> element can also be used; 

Presentational elements, no sematic values: \<i>, \<b>, \<u>

## Advanced HTML 

Advanced HTML formatting:  <sup>[^2]</sup>

Description lists **\<dl>** allow for lists with items with sub points; terms are wrapped in  **\<dt>** with each description definition wrapped in \<dd>.

```
<dl>
  <dt>apples</dt>
  <dd>fiber</dd>
  <dd>antioxidants</dd>
  <dt>bananas</dt>
  <dd>High in potassium and magnesium.</dd>
</dl>
```

### Quotations using blockquotes **\<blockquote>** and **\<cite>** for quotes that require paragraph breaks. 

```
<p>another source for explaining blockcode</p>
  <blockquote cite="https://www.w3schools.com/tags/tag_blockquote.asp">The <blockquote> tag specifies a section that is quoted from another source.
  </blockquote>
```
<sup>[^6]</sup>

Inline quotations using **\<q>** are intended for short quotations that don't need paragraph breaks.

```
<p>quote element
<q cite= "https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Advanced_text_formatting"> no needed break </q>
</p>
```

### Abbreviations and acronym using **\<abbr>** 

```
<p>this is an abbreviation in use, <abbr>HTML</abbr>, Hypertext Markup Language</p>

<p>abbreviation using title <abbr title="mister'>Mr.</abbr> Peter Python</p>
```

Contact details using **\<address>**

- only use to provide contact info
- keep within \<article>  or \<body> or \<footer>

**\<sup>** and **\<sub>** are used for used for dates and math equations/chemical formula,  respectively.

```
<p>Today is the 12<sup>th</sup> of September.</p>
<p>Drink your H<sub>2</sub>O!!</p>
```

1. important of semantic element usage
2. There are 6 levels of heading h1-h6, with h1 being the biggest and h6 being the smallest
3. sub and sup tags are used for math equations, dates, chemical formulas. 
4. Title attribute 

## Learn CSS

CSS can be applied in three ways <sup>[^3]</sup>:

External Stylesheet via **\<link>** element with **href** attribute referencing css file in system.


```
<html>
<head>
<link rel="stylesheet" href="styles.css">
</head>
</html>
```

Internal stylesheet lives in \<head> uses **\<style>** tag. 

```
<head>
<style>
  h1{
    color: green;
    background-color: yellow;
  }
<style>
</head>
```

Inline styles placed within single element 

- least efficient, less legible

```
<h1 style="color: blue; border: 1px solid; border-color: black;">Hello</h1>
```

Selectors are the HTML elements CSS is going to style ex: h1, p, body.  You can specify certain elements using **class= "classname"** attribute within element.

### Properties and values

Properties are stylistic features you want to modify. Ex: **font-size, width**

Values: indicate how to style property

When property is paired with value we call it a *CSS declaration.*

- Creates a declaration block.
-  Declaration blocks paired with selectors are called *CSS rulesets*
- case-sensitive, separated by colon

Some CSS functions

Transform: transforms element, ex: transform: rotate;

Comments can be made using /* /*

1. apply css locally on html file with \<style> or apply externally by linking css stylesheet via \<link> element.
2. It is not efficient and is less legible.
3. color and padding are both properties.

## Learn JS

JavaScript is dynamic. Added to our html file with **\<script>** element using **src** attribute within \<body>.
<sup>[^4]</sup>

```
<script> src="scripts/main.js"></script>
```
| variable type | explanation | example |
| ------ | ------ | ------ |
|string| any kind of text within single/double quotation marks | let variable1 = 'Monica';|
|boolean| True or false | let variable1= true;
|number| integers, including float | let variable1= 10; |
|array| stores multiple values within single reference | let variable1 = \[1, 'monica', true];
|object| could be anything| all examples above and more |

### Functions

Functions are reusable, executed when called.

- take parameter: bits of data needed to do job. inside parentheses.

```
let name;
function user(name):{
  prompt('what is your name');
  alert('hello person');
} 
```

1. Strings are enclosed in quotation marks
2. addition +, assignment =, strict equality ===, doesn't equal !=
3. Building a website that requires age verification. 

### Conditionals

```
let number= prompt ('give me a number');
function userAnswer(number){
  if (number>=100){
    console.log('yass');
    }
  else if (number>=50 && number<100){
    console.log('okay');
  }
  else {
    console.log('too low');
    }
}

userAnswer(number);
``` 

[^5]

1. An if statement checks a *condition* and if it evaluates to *true*, then the code block will execute
2. Else if is a conditional statement that comes after "if" statement if it wasn't true, but is checked before the "else" statement.
3. Comparison operators:
    - < less than
    - != doesn't equal
    - == equal/same
    - \> greater than

4. && means "and" both expression true; || means "or" only one of those expression has to be true

## Things I want to know more about

I want familiarize myself more with JavaScript functions. 

[^1]:Reference[link](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals)

[^2]:Reference[link](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Advanced_text_formatting)

[^3]:Reference[link](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_is_structured)

[^4]:Reference[link](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)

[^5]:Reference[link](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals)

[^6]:Reference[w3schools](https://www.w3schools.com/tags/tag_blockquote.asp)


📔[Back to Main Page](README.md)