# 10. Audio, Video, Images

## Why is this important

Visuals are important. Learning to apply them to create a more user friendly experience and create better user engagement is key.

`<video src="source.webm" controls>`

```HTML
<video src="rabbit320.webm" controls>
  <p>
    Your browser doesn't support HTML video. Here is a
    <a href="catvid.webm">link to the video</a> instead.
  </p>
</video>

```

- *controls* adds the ability for users to control video with browsers own control interface or our own built interface.

- `<p>` tags include fallback content — this will be displayed if the browser accessing the page doesn't support the <video> element. <sup>[1]</sup>

Video Features:

- width and height: you can control the video size either with these attributes or with CSS. In both cases, videos maintain their native width-height ratio — known as the aspect ratio. If the aspect ratio is not maintained by the sizes you set, the video will grow to fill the space horizontally, and the unfilled space will just be given a solid background color by default.

- autoplay: makes the audio or video start playing right away, while the rest of the page is loading. You are advised not to use autoplaying video (or audio) on your sites, because users can find it really annoying.

- loop: makes the video (or audio) start playing again whenever it finishes. This can also be annoying, so only use if really necessary.

- muted: causes the media to play with the sound turned off by default.

- poster: URL of an image which will be displayed before the video is played. It is intended to be used for a splash screen or advertising screen.

- preload: used for buffering large files; it can take one of three values:

  - "none" does not buffer the file
  - "auto" buffers the media file
  - "metadata" buffers only the metadata for the file

`<audio>` difference between audio and video tags: no width/height  and poster attributes supported (no visuals)

```HTML
<audio controls>
  <source src="viper.mp3" type="audio/mp3" />
  <source src="viper.ogg" type="audio/ogg" />
  <p>
    Your browser doesn't support this audio file. Here is a
    <a href="viper.mp3">link to the audio</a> instead.
  </p>
</audio>

```

1. It has evolved from using plug-ins to using HTML Elements and JS APIs.

2. Controls adds the ability for users to control video with browsers own control interface or our own built interface. Src contains path to video file.

3. Fallback content allows us to display a message when our video is not supported by their web browser.

4. Audio and video are similar they only have 2 difference between them, but they are like brothers. Audio is just sound, video is sound and visuals.

## CSS Grid Layout

`display:grid;`

`grid-template-columns` set column

`grid-template-rows` row sizes

Set rows and colums sizes, place child elements into grid with `grid-column` and `grid-row`

Grid Container: element where  `display:grid` is applied to.

- direct parent of all the grid items<sup>[^2]</sup>

Grid line: dividing lines that make up the structure of the grid. Can be vertical (column) or horizontal (row).

Grid Track: space that lives between two adjacent grid lines.

Grid Area:  total space surrounded by four grid lines.

- area composed of any number of grid cells.

Grid item: direct children of grid containers.

```HTML
<!-- p tag would not be a grid item, only "item" is direct child of container >> grid item -->
<div class="container">
  <div class="item">
    <p class= "subitem"></p>
  </div>

</div>

```

Grid Cell: space between two adjacent row and column grid lines. "single unit" of grid.

```CSS
.container {
  display: grid | inline-grid;
/* optional to name lines [], lines can have more than one name */
/*if definition has repeating parts us repeat()*/

  grid-template-columns: [first] 40px [line2] 50px [line3] auto [col4-start] 50px [five] 40px [end];

  grid-template-rows: [row1-start] 25% [row1-end] 100px [third-line] auto [last-line];
}
```

`fr` unit allows you to set the size of a track as a fraction of the free space of the grid container.

```CSS
/* size of track set to 1/3 of width of grid container*/
.container {
  grid-template-columns: 1fr 1fr 1fr;
}
```

`grid-template-areas` defines grid areas which are specified in grid area property.

- Repetition of name of grid area causes content to span those cell.
- period >> empty cells. as long as periods have no spaces between them they represent single cell.
- none- no grid area defined

```CSS
.item-a {
  grid-area: header;
}
.item-b {
  grid-area: main;
}
.item-c {
  grid-area: sidebar;
}
.item-d {
  grid-area: footer;
}

.container {
  display: grid;
  grid-template-columns: 50px 50px 50px 50px;
  grid-template-rows: auto;
  grid-template-areas: 
    "header header header header"
    "main main . sidebar"
    "footer footer footer footer";
}
```

Shorthand grid template:

```CSS
.container {
  grid-template:
    [row1-start] "header header header" 25px [row1-end]
    [row2-start] "footer footer footer" 25px [row2-end]
    / auto 50px auto;
}
/* row starts, 3 header cells 25px wide? row end
row 2 start, 3 footer cells 25 px wide? row end */
```

`column-gap` and `row-gap` set grid line size >> gutter width; space between columns/rows.

- `gap`  set row and column, respectively.

`justify-items` aligns items to inline (ROW) axis.

`align-items` aligns items to block (COLUMN) axis.

1. Flexbox is one dimensional, Grid is two dimensional.

2. Grid Container is the element where  `display:grid` is applied to. Grid items are direct children of grid containers. Grid lines make up the structure of grid, rows and columns.

## Responsive Images

Browser looks at device width >> which media condition in sizes is first one to be true >> look at slot size >> load image reference in srcset that has same size as slot or the first image that is bigger than the chosen slot size.

```HTML
<img

  srcset="elva-fairy-480w.jpg 480w, elva-fairy-800w.jpg 800w"
  sizes="(max-width: 600px) 480px,
         800px"
  src="elva-fairy-800w.jpg"
  alt="Elva dressed as a fairy" />
```

`srcset` defines the set of images we will allow the browser to choose between, and what size each image is. <sup>[^3]</sup>

- each image separated by comma.

- `(filename) (width in pixels, using *w* unit)`
  - intrinsic size is real size of image.

`sizes` defines set of media conditions (screen widths), best size to choose

- `(max-width:600px)` media condition describes a possible state that the screen can be in. In this case, we are saying "when the viewport width is 600 pixels or less".

- width of slot after media slot >>> space media will fill when media condition is true

```HTML
  sizes="(max-width: 600px) 480px
  ```

1. Images should be responsive in order to not degrade quality, not waste bandwidth.

2. Browser looks at device width decides which media condition in sizes is first one to be true  then looks at slot size  then  loads image referenced in srcset that has same size as slot or the first image that is bigger than the chosen slot size.

3. Srcset allows us to add images and allow them to be more responsive to a multitude size of screen sizes.

How is srcset more helpful for responsive images than CSS or JavaScript?

## Things I want to know more about

I want to learn more about how to use grid and how it works.

[^1]: Reference [Video and Audio](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Video_and_audio_content)

[^2]: Reference [CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-introduction)

[^3]: Reference [Responsive images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)

📔[Back to Main Page](README.md)
