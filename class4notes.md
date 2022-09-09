# Class Four Notes

## Wireframe and Design

Wireframing is the planning of info hierarchy of design for a website, app or product. User experience on their platform. Best practice to plan out before any coding, wheter it be on paper or on a drawing tool online. 

1. sketch, dont draw. Remember: you’re outlining and representing features and formats, not illustrating in mighty fine detail. There’s nothing worse than a blank piece of paper, so you need to start getting your ideas down pronto—that’s the imperative for step three.
less detail is best.

2. add detail after simple sketch
Usability conventions, such as putting the navigation at the top next to your logo, having a search box on the top right, and so on
Simple, instructional wording for i.e. calls-to-action
Trust-building elements: What do you need to build trust in your customers and where would be the best place to put these elements?
Tooltips to indicate any functionality that could be included in a prototype transition

3. turn wireframes into prototypes
 Sketch and the browser-based, new(ish) kid-on-the-block, Figma. Once you’ve developed your wireframes in Sketch, you can import them into the industry-leading prototyping tool InVision (which, incidentally, we built a course in conjunction with) and interlink your screens for a second round of high-fidelity user testing.


Three key principles of making a good wireframe:

- clarity: visualization of layout ensuring that user's most important questions are answered. Goals are achievable without the distractions of asthetics. '
- confidence: ease of navigation on site creates user confidence. Making sure the site is intuitive and feels familiar to user will help user confidence.
- simplicity: layout and information simplicity will help the site be less distracting to user allowing them to navigate more easily.


## Mozilla HTML Basics

HTML is a markup language that defines the structure of your content. HTML consists of a series of elements, which you use to enclose, or wrap, different parts of the content to make it appear a certain way, or act a certain way

![html example](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics/grumpy-cat-small.png)

The opening tag: This consists of the name of the element (in this case, p), wrapped in opening and closing angle brackets. This states where the element begins or starts to take effect — in this case where the paragraph begins.
The closing tag: This is the same as the opening tag, except that it includes a forward slash before the element name. This states where the element ends — in this case where the paragraph ends. Failing to add a closing tag is one of the standard beginner errors and can lead to strange results.
The content: This is the content of the element, which in this case, is just text.
The element: The opening tag, the closing tag, and the content together comprise the element.

#### Attributes

![attribute](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics/grumpy-cat-attribute-small.png)

Attributes contain extra information about the element that you don't want to appear in the actual content. Here, class is the attribute name and editor-note is the attribute value. The class attribute allows you to give the element a non-unique identifier that can be used to target it (and any other elements with the same class value) with style information and other things.

An attribute should always have the following:

- A space between it and the element name (or the previous attribute, if the element already has one or more attributes).
- The attribute name followed by an equal sign.
- The attribute value wrapped by opening and closing quotation marks.

#### Nesting

You can put elements inside other elements. example:
    <p>My cat is <strong>very</strong> grumpy.</p>

#### HTML doctument requirements

- <!DOCTYPE html> — doctype. It is a required preamble.
- <html></html> : wraps all content on entrire page; root element. 
- <head></head> : page description that you want to appear in search results and other things
- <title></title> : title on the page that appears on the browser tab
-<body></body> : all the content you want web users to see when they visit page. 

Adding images: 
<img src="images/firefox-icon.png" alt="My test image">

📔[Back to Main Page](README.md)