## Class Five Notes

### What is CSS?

CSS (cascading style sheets) make your website pretty and stylized. HTML is the structure, CSS is the decoration.
CSS can be used for very basic document text styling — for example, for changing the color and size of headings and links. It can be used to create a layout — for example, turning a single column of text into a layout with a main content area and a sidebar for related information. It can even be used for effects such as animation.

CSS rules 
- selector : HTMl element that we are going to style ex: in html we would have this element < h1>. in css its simply called h1
- curly braces { } encapsulte one or more declarations, which take the form of property and value pairs. 
- properties: CSS properties have different allowable values, depending on which property is being specified

h1 {
    color: red;
    font-size: 5em;
    }
### How To Add CSS

When a browser reads a style sheet, it will format the HTML document according to the information in the style sheet.
There are three ways to add a style sheet:

- external css= whole site
- internal css= individual page
- inline css= individual element

External styles are defined within the <link> element, inside the <head> section of an HTML page. An external style sheet can be written in any text editor, and must be saved with a .css extension
![external css](https://codebridgeplus.com/wp-content/uploads/download-5.png)

Internal style sheet may be used if one single HTML page has a unique style.
The internal style is defined inside the < style> element, inside the head section.

![internal css](https://codebridgeplus.com/wp-content/uploads/InternalCSSInternalstylingisdefinedinthe_head_sectionofanHTMLpageusinga_style_element..jpg)

Inline style may be used to apply a unique style for a single element.
To use inline styles, add the style attribute to the relevant element. The style attribute can contain any CSS property.

![](https://fitbloggin.com/wp-content/uploads/2014/06/Fitbloggin-HTML-and-CSS-for-the-Non-Technical-Blogger-9.jpg)


### CSS color

The color property specifies the color of text. Color syntax:

color: *color|initial|inherit*

- color: Specifies the text color.
- initial: Sets this property to its default value.
- inherit: Inherits this property from its parent element.

example: body {color: #92a8d1;}

Cascading order starts with:
- Inline: priority
- Internal: next priority
- External: next priority
Browser default

📔[Back to Main Page](README.md)