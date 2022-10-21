# 9. Forms and JS Events

## Why this is important

HTML allow us capture user data that we might find useful. Events allows us to make our website more interactive and dynamic.

## HTML Forms

Web forms are one of the main points of interaction between a user and a web site or application. Forms allow users to enter data, which is generally sent to a web server for processing and storage.<sup>[^1]</sup>

HTML is made up of more than one form control (widgets), with additional elements to help with structure of the form.

- controls can be single or multi-line text fields
- ```<input>```
  - dropdown boxes
  - buttons
  - checkboxes
  - radio buttons

**Keep forms simple!**

### Creating Forms

```<form>``` defines element as a form. container like section or footer. Include following tags:

- ```<action>``` url where form data collected should be sent

- ```<method>``` defines what HTTP method used: get or post

```HTML
<form action="/my-handling-form-page" method="post">…</form>
```

Form data entry:

- ```<label>``` What the data entered is for; "name", "age"
- ```<input>``` User input, single-line; empty tag, no closing tag
  - ```type``` attribute allows us to define way
  input appears and behaves
  
- ```<textarea>``` Input field for message, multi-line

```HTML
<form action="/my-handling-form-page" method="post">
  <ul>
    <li>
      <label for="name">Name:</label>
      <input type="text" id="name" name="user_name" />
    </li>
    <li>
      <label for="msg">Message:</label>
      <textarea id="msg" name="user_message"></textarea>
    </li>
  </ul>
</form>
```

```<button>``` allows user to send/submit data, accepts type and following attributes:

- ```submit``` sends info to web page defined by action attribute in form element.
- ```reset``` resets all form values, avoid
- ```button``` does nothing!

1. They are important because they allow our website to become interactive with our user.

2. Keep things simple.

3.

- ```<form>``` defines element as a form. container like section or footer.
- ```<action>``` url where form data collected should be sent
- ```<label>``` What the data entered is for; "name", "age"
- ```<input>``` User input, single-line

- ```<textarea>``` Input field for message, multi-line

## JS Events

Events are actions or occurrences that happen in the system you are programming — the system produces (or "fires") a signal of some kind when an event occurs, and provides a mechanism by which an action can be automatically taken (that is, some code running) when the event occurs. <sup>[^2]</sup>

- web events are fired within browser window are attached to specific items that resides in it. Ex:
  - users click, hovers cursors over certain element.
  - resizing of browser window
  - form submission

Event Handlers: block of code that runs when even fires

Registering event handler: defining block of code defined to run in response to event.

```addEventListener()``` method is applied to objects that can fire events.
  
- takes in at least 2 parameters:
  - name of event and a function

```JavaScript
//returns first element within document that matches specified selector: button
const btn = document.querySelector('button');

//random number function
function random(number) {
  return Math.floor(Math.random() * (number+1));
}
/// defining and registering event handler: when clicked, code block below runs
btn.addEventListener('click', () => {
  const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
  document.body.style.backgroundColor = rndCol;
});

```

Capturing phase: opposite of bubbling, starts from outermost element traversing down until it finds element that triggered the event.

Target phase: The event reaches the target element, and runs the event listener attached to it, if any.

Bubbling: event is in an element inside another element, and both elements have registered a handle to that event. Starts with the element triggered and then bubbles up the containing elements.

- by default event listeners called in this phase

1. Events are things that happen as a consequences of a users actions?

2. You need to provide an event name and a function.

3. Event objects  are automatically passed to event handlers to provide extra features and information, all event objects have access to the Event object properties and methods.

4. Capturing starts from the outermost element and bubbling does the opposite, inward looking out.

## Things I want to know more about

I want to know more about event listeners and more about all of the things they can do aside from a click.

[^1]: Reference [HTML Forms](https://developer.mozilla.org/en-US/docs/Learn/Forms/Your_first_form)

[^2]: Reference [JS Events](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events)

📔[Back to Main Page](../README.md)
