# 5. HTML Media and CSS: Colors and Font Styling

## "Why is this important"

This is important for aesthetics and readability of a page.

## HTML Media <sup>[^1]</sup>

**<img>** element is an *empty element* (no text or closing tag) req. min. one attribute to be useful. self closer, only one tag

- uses **src** source attribute, lives inside img tag
- correct path required for source
- best practice to have images in file/ same server as HTML code.

**<alt>** attribute is a text description for image. helps deliver a usable experience when images cant be seen.

- important for accessability, if not added screen reader will read out the src tag.
- used when image cant be seen/displayed or computer connection lags, description in alt attribute will show.
- images not supported, will display alt description
- help search engine matching
- leave alt when image is for background

**<title>** attribute shows when mouse is hovering over it.

**<figure>** semantic creates container for figures, really useful to store images.

- doesn't have to be image
- can go in several places on page
- provides essential info supporting main text?
- could be images, code snippet, audio, video, table etc

**<figcaption>** links figure to caption

- place it above or below images

```html
<figure>
  <img src="images/cat.jpg" alt="picture of cat crying">
  
  <figcaption>
    Cat of white cat crying
  </figcaption>
</figure>

```

### Using Images in HTML<sup>[^2]</sup>

[caniuse.com](caniuse.com)to check to see if your code will run on across all web browsers.

When using google image, select creative usage for images free use or else credit creator owner.

[unsplash.com](unsplash.com) free images for common use.

|Type| File Format| MIME type| file extensions| Summary|
|----|--------|----|----|--------|
|AVIF|AV1 Image File Format|image/avif|.avif| high performance, better compression than png and jpeg|
|GIF|Graphics Interchange Format|image/gif|.gif| simple images, animations|
|JPEG|Joint Photographic Expert Group image| image/jpeg| .jpg, .jpeg, .jfif, .pjpeg, .pjp| quality loss w/ compression |
|PNG|Portable Network Graphics|image/png|.png|PNG is preferred over JPEG for more precise reproduction|
|SVG|Scalable Vector Graphics|image/svg+xml|.svg| Vector image format; ideal for user interface elements, icons, diagrams, etc., that must be drawn accurately at different sizes|

1. If image can't load or connection is lagging alt description will be displayed in place of image.

2. Accessability can be improved by using alt attribute within image tag.

3. Can be useful for placing video or audio

4. A gif is not a static picture, more like a short snippet of a video, like an animation that runs on a loop with no sound. Svg is an image that when zoomed in is smooth isn't made up of pixel(tiny squares).

5. Lossless WebP or PNG when compressed don't lose image quality

## CSS

An asterisk is a global selector, everything in here will be applied to all page. Individual properties need to styled to differ from whatever lives here.

Best practice to follow property styling based on how html is layed out? create comments to describe what we are styling. [^5]

Sizing:

**percentage** using percentages "its going to take up X% of the screen

- width: 50% would be half of width of parent it lives in, more responsiveness

easy centering:

- give margin of auto and a width

```css
img{
  width: 100%; 
  // image will take 100% of what it lives in more responsive
}
```

**inherit** tells that element to inherit to that property from its parent

```css

figure{
  background-color: red;
  width: 50 % 
  //will alway take up 50% of whatever it lives in , more responsive when reducing screen size
}
figcaption { 
  background-color: inherit;
}

// fig caption in html inherits color of figure html element since it lives inside figure.

```

### Color<sup>[^3]</sup>

Anything in HTML can have color applied to.

**color** property defines foreground color of HTML element content

**background-color** property defines backgroud color of element

Every element is box with content; has a background and border.

**column-rule-color** property when drawing line seperating columns of text

**outline-color** outline outside of element, not border of it.

Borders are around elements, at edges of element content

**border** property can have multiple configurations in one line or sides can be individually styled

```
border: 6mm dotted rgba(280, 220, 30, .6);
```

HSL functional notation of color is preferred, similar to RGB

### Styling HTML Text Elements<sup>[^4]</sup>

Serif font will have little arms at the end of lines ex: Times New Roman.

**font-family** specify font/list of fonts for browser to apply to selected elements

**font-stack** allows you to apply multiple fonts, allowing you to guarantee availability of text if one font fails. separated by commas

[cssfontstack.com](cssfontsstack.com) for easy search of font family stack

**font-size** default size is 16 px

**em** equals size of parent. 1 em is same size as parent. 2 em would be twice font of parent. not really responsive, but looks to its parent element.

**vw** percent of size of screen, responsive unit. Gives us percentage of size of screen.

- doing **percentage** with fonts will be percentage of the parent it lives in, still responsive but within parent.

1. foreground color applies to text, including any other decorations to it; background color applies color to borders or element backgrounds?

2. I would add color to background of page, to sections, text, headers

3. Simplicity, readability

4. font-size changes size, font-weight= boldness, font-style= italic

5. We can use letter-spacing and word-spacing properties when font is too dense and to improve readability.

[^1]:Reference [Images In HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Images_in_HTML)

[^2]:Reference [Images Types](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types)

[^3]:Reference [Applying Colors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Applying_color)

[^4]:Reference [Styling Text](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals)

[^5]:Notes taken from Lecture [](https://github.com/arpatterson31)
  
## Things I want to know more about

I am still confused about blocks, would like to learn more.

📔[Back to Main Page](../README.md)
