# 3. FileIO & Exceptions

## Why is this important
It is important to know how to access files and when to have to ability to access them. 
## Files

`..` double dot can be use to traverse multiple directories 
 - `.` "here"
-  `.. "one up" 

Opening and Closing File in Python:

```
variable = open(filePath)

try: 
    #file processing
finally:
    variable.close()
```

open file as statement:

```
with open(filepath) as reader:
    # Further file processing goes here
```

optional arguments for `open()`:
- `r` reading
- `w` writing, overwriting file first
- `rb` or `wb` binary mode (read/write using byte data)

Reading:

read(size=-1)	This reads from the file based on the number of size bytes. If no argument is passed or None or -1 is passed, then the entire file is read.
.readline(size=-1)	This reads at most size number of characters from the line. This continues to the end of the line and then wraps back around. If no argument is passed or None or -1 is passed, then the entire line (or rest of the line) is read.
.readlines()	This reads the remaining lines from the file object and returns them as a list.

## Exceptions 

exception error occurs when syntactically correct Python code results in an error.
- use raise to throw an exception if a condition occurs. The statement can be complemented with a custom exception

AssertionError exception:
- assert that when condition is met keep running
- if is false, throw assertion error

Try and Except block
- catches an handles exception 

```
try:
    # run this code 
except:
    #execute when theres an exception
else:
   # no exceptions? run this code
finally:
    # always run this code 
```

## Things I want to know more about

I want to work with more exceptions. 

## Resources

[Read, Write Files](https://realpython.com/read-write-files-python/)

[Python Exceptions](https://realpython.com/python-exceptions/)

📔[Back to Main Page](README.md)