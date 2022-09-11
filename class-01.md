# Class 01

## JavaScript

JS is a dynamic language.Tools have been develop to add max function with minimum effort.

![webpagecake](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript/cake.png)

<details>
    <summary> Browser application progamming interfaces (APIs)</summary>
    <p>- built into web browsers; dynamic HTML & CSS styles
    - generating 3D graphics/audio
    - manipulating stream from user webcam

- Third party APIs allow devs to incorporate functionality in sites from other content providers

- Third-party frameworks/libraries you can apply to HTML</p>
    </details>

## Variables

variables= containers that store values.

- Values are assigned by using equal sign
- Case sensitive
- Cant start with numbers, use camel case.
  - can use numbers, letters, $ or _

### Variable data types

| Variable | explanation | example |
| ----- | ------------ | -------- |
|String| enclosed in single, double quotes or backticks| let myVar= 'bob';|
|Number|numbers, including float| let myVar= 10;|
|Boolean|True or False|let myVar= true; |
|Array| structure allowing us to store multiple values in single place| let myVar = [ 1, 'bob'];|
|Object| can be anything, everything in JS is an object and can be stored in variable | let myVar = document.querySelector('h1';)|

```
let variableName;
```

comments, not ran (ignored) written using /*comment*/

<details>
    <summary>&#128209;Operators</summary>

    + addition 
    - subtraction
    * multiplication
    / division
    = assignment of variable
    == equal to 
    === strict equality, type has to match 
    ! , !== not; doesnt equal

</details>

<details>
<summary>&#128209;Getting Started Questions</summary>

This topic is imporant because JavaScript is a dynamic language. It has many different functions from front end to backend, it's versatile.

1. Web address is translated into an ip address using DNS. Three way handshake is then performed (TCP Handshake); establishing communication between two parties over using HTTPS protocol. After synchronizations and acknowledgements are sent back and forth, a connection is established.
HTTP GET request is sent from user= get HTML file. packet with 14kb of data is received by user. More packets are sent, after each is acknowledged by user.

2. After first packet is receivedm parsing happens(building of page). HTML, CSS, and JS have to be parsed before anyting is on screen. HTML-->skeleton(DOM tree) CSS-->makeup(CSSOM tree) JavaScript-->muscle, dynamics(abstract syntax tree)
render->interactivity->done
3. Google search is a good place to search for images, using license filter to choose Creative commons licencses.
4. Strings are created by encapsulated characters in between quotation marks, single or double. Numbers are integers with or without decimals, they dont have quoatation marks.
5. Variable is an object that stores values.

</details>

## HTML

HyperText Markup Language structures web pages.

- elements (wrap; markup) part of DOM.
- tags begin/end element in source code. not case sensitive.

```
</p>I love cats</p>
```

- < p> </ p> : opening/closing tags
- I love cats : content
- whole thing is an element

Elements can be nested within other elements

```
<p>My cat is <strong>very</strong> grumpy.</p>
```

Block-level ekements:

- visible block on page
- structural elements: headings, paragraphs, lists, navigation menus or footers
-causes new lines to appear

Inline elements:

- contained within block-level elements
- used with text ex :< a></ a> for links, < strong></ strong> for emphasis

Empty elements:

- no closing tag, just opening tag.
- insert/embed something in document. ex:

```
<img src="https://raw.githubusercontent.com/mdn/beginner-html-site/gh-pages/images/firefox-icon.png">
```

### Attributes

```
<p class="notes>My class notes</p>

class="notes" is attribute
```

Attributes wont appear in content, just have extra info on content. Set witihin first tag.

- space between attribute and element
- attribute name, followed with equal sign =
- attribute value wrapped in quoatation marks.

| Attribute | Defenition | Example |
| ----- | ------| ------ |
|href| web address specification| href="<https://www.mozilla.org/> |
|title| descriptor, appears when cursor hovers over elememt | title= "Cat pic"|
|target| specifies browsing content used to display text| target= "_blank"|

Anatomy of HTML document

```
<!DOCTYPE html> 
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
</html>

<!DOCTYPE html> include this always
<html></html> root element, wraps all content on page
<head></head> isnt content, viewers wont see it. page description, css to style content etc. contains metadata
<meta> metadata not represented in meta-related elements <link>, <style>, <title>, <base>
<title></title> page title, what appears in browser tab. page descriptor
<body></body> ALL contents displayed on page
```

## Metadata in the \<head>\</head>

Head element has all the metadata info like css page  link, author info, important keywords.

- title tag: page title
- meta tag:  what languages your page can handle?
  - name(type of meta element) and content (actual meta content)

```
<meta name="author" content="Chris Mills">
```

<details>
    <summary>&#128209;Intro to HTML questions</summary>

1. Attribute is extra info on an element.
2. An element is made up of content and tags. The content is what is shown. Tags are what define what that content is.
3. Article is a way of adding extra info about an element. A section is an actual section on page
4. !DOCTYPE html, html, head, title, body, sections are typical elements used in website.
5. Including specific descriptions into the meta tag can help search engines make it more visible on result pages
6. Meta used to add info about the page, its creators, things that your user doesnt need to see

</details>

## Website Design

1. First step is project ideation, "whats the goal? what do I want to accomplish? steps to reach goal"
2. The most imporant question to answer when designing a website is "what do I want to accomplish?"

## Semantics

Semantics: meaning of code, its function etc.

In HTML code should represent data that will be populated, not based on default presentation styling. Presentation is done with CSS.

"What element best describes/represents data?"
List of some semantic elements:

- article
-aside
- details
- figcaption
- figure
- figure
- footer
- header
- main
- mark
- nav
- section
- summary
- time

1. h1 header has the benefits of semantics, while span is more of a presentation of a header.
2. Benefits of using semantic elements: content is considered as important keywords to influence page's search ranking, important for screen readers, easier to find meaningful code etc.

## What is JavaScript?

- HTML: Markup language, STRUCTURE, meaning to web content.
- CSS: styles HTML content
- JavaScript: dynamic language.

core client-side:

- variables
- operations
- events/functions

Application Programming Interfaces (APIs):

- ready-made sets of code allowing devs to implement programs

Browser API built into web browser.

- DOM (document object model) manipulation of HTML/CSS, allowing dynamic application of new styles to page.
- geolocation APIs
- canvas and WebGL APIs create animated 2D/3D graphics.
- Audio/Video APIs: HTMLMediaElement and WebRTC play audio/video in webpage or grab video from web cam and display it on someone else's computer.

Third party APIs not built into browser, grab their code from some other server

- twitter API allowing you to display latest twee
- google maps API

Order of code is important, JS is read from top to bottom.
JS is an interpreted language, read and run as is.

Internal JavaScript in HTML code:

```
<head>
    <script>
        JavaScript code
    </script>
</head>
```

External JavaScript, link JS file:

```
<head>
    <script src="script.js" defer></script>
</head>
```

### Loading scripts

- defer:  load in order that they appear on page. Page will only run until all content loaded, scripts that depend on DOM
- async: script dowloaded without code blocking while script is being fetched. "load asap." contenet executed as soon as download complete.

1. JavaScript allow for pages to be dynamic like the ablity to fill out webforms or displaying your webcam image onto someone else's screen.  
2. You add JavaScript to HTML with < script>

## Things I want to know more about

More on how to build dynamic website features, especially ones where user input is required. 


📔[Back to Main Page](README.md)