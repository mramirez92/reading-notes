# 10. Debugging

## Why is this important

It's important to know this so we can problem solve our code.

## Troubleshootig JavaScript

Syntax errors: spelling errors, missing semicolon, open curly brackets/parenthesis, missing colon. <sup>[^1]</sup>

Logic errors: correct syntax, wrong code. Gives incorrect results.

Use Developer tools console are great way to spot errors.

- google chrome>inspect>console

1. Logic errors can still allow your code to run even if the code doesn't produce the result you want. Syntax errors will not let your code run.

2.The most common error I make is the spelling and missing curly bracket on functions. Before I move on to the next piece of code, I try to check spellings and I make sure I put my closing curly bracket and semicolons.

3.This will remind me to be more strict with the way I write my code. Check continuously and constantly with every block of I write.

## JavaScript Debugger

The JavaScript debugger allows you to watch the value of variables and set breakpoints, places in your code that you want to pause execution and identify the problems that prevent your code from executing properly.<sup>[^2]</sup>

Dev tools in Chrome >>> **sources** tab.

- Select file
- Set breakpoints on the left, breakpoints set where you want to pause execution.
- Call Stack shows what code was executed to get to the current line.
- Scopes shows what values are visible from various points within your code.

1. It allows you to run the code and create a stopping point to see how it works up until that point.

2. Breakpoint pause execution of code when debugging.

3. Call Stack shows what code was executed to get to the current line.

## Things I want to know more about

I want to learn how to use the debugging tool on Chrome more efficiently for JS.

[^1]: Reference [Troubleshooting JS](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)

[^2]: Reference [JS Debugger](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools#the_javascript_debugger)

📔[Back to Main Page](README.md)
