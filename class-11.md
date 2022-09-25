# 10. Audio, Video, Images

`<video src="source.webm" controls>`

```HTML
<video src="rabbit320.webm" controls>
  <p>
    Your browser doesn't support HTML video. Here is a
    <a href="catvid.webm">link to the video</a> instead.
  </p>
</video>

```

- *controls* adds the abilty for users to control video with browsers own control interface or our own built interface.

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

📔[Back to Main Page](README.md)
