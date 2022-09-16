# Class 05 Notes

## "Why is this important"

This is important for aesthetics and readability of a page.

## HTML Media <sup>[^1]</sup>

**<img>** element is an *empty element* (no text or closing tag) req. min. one attribute to be useful.

- uses **src** source attribute
- correct path required for source
- best practice to have images in file/ same server as HTML code.

**<alt>** attribute is a text description for image. helps deliver a usable experience when images cant be seen.

- used when image cant be seen/displayed or computer connection lags, description in alt attribute will show.
- images not supported, will display alt description
- help search engine matching
- leave alt when image is for background

**<figure>** semantic creates containerfor figures

- doesn't have to be image
- can go in several places on page
- provides essential info supporting main text?
- could be images, code snippet, audio, video, table etc

**<figcaption>** links figure to caption

```
<figure>
  <img src="images/cat.jpg" alt="picture of cat crying">
  
  <figcaption>
    Cat of white cat crying
  </figcaption>
</figure>
```

### Using Images in HTML<sup>[^2]</sup>

|Type| File Format| MIME type| file extensions| Summary|
|----|--------|----|----|--------|
|AVIF|AV1 Image File Format|image/avif|.avif| high perfomance, better compression than png and jpeg|
|GIF|Graphics Interchange Format|image/gif|.gif| simple images, animations|
|JPEG|Joint Photographic Expert Group image| image/jpeg| .jpg, .jpeg, .jfif, .pjpeg, .pjp| quality loss w/ compression |
|PNG|Portable Network Graphics|image/png|.png|PNG is preferred over JPEG for more precise reproduction|
|SVG|Scalable Vector Graphics|image/svg+xml|.svg| Vector image format; ideal for user interface elements, icons, diagrams, etc., that must be drawn accurately at different sizes|

1. If image can't load or connection is lagging alt description will be displayed in place of image.

2. Accessability can be improved by using alt attribute within image tag.

3. Can be useful for placing video or audio

4. A gif is not a static picture, more like a short snippet of a video, like an animation that runs on a loop with no sound. Svg is an image that when zoomed in is smooth isnt made up of pixel(tiny squares).

5. Lossless WebP or PNG when compressed dont lose image quality

## CSS

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

**font-family** specify font/list of fonts for browser to apply to selected elements

**font-stack** allows you to apply multiple fonts, allowing you to guarantee availability of text if one font fails. seperated by commas

1. foreground color applies to text, including any other decorations to it; background color applies color to borders or element backgrounds?

3. I would add color to background of page, to sections, text, headers

4. Simplicity, readabilty

5. font-size changes size, font-weight= boldness, font-style= italic

6. We can use letter-spacing and word-spacing properties when font is too dense and to improve readability.

[^1]:Reference [](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Images_in_HTML)

[^2]:Reference [](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types)

[^3]:Reference [](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Applying_color)
  
[^4:]Reference[](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals)

## Things I want to know more about

I am still confused about blocks, would like to learn more.

📔[Back to Main Page](README.md)
