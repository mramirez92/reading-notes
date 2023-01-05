open()
files in python  need to be closed when they are not in use

best way to do file `with` statement

## jupyter notebook 

jupyter notebooks lets you run cells of code and see changes quickly 
install jupyter dependencies in directory 

`touch file_io.ipynb`
jupyter allows us to add markdown and python in one file
all cells are connected

run cell button to run code

create a directory that containst txt file

# file i/o
**** create text file, with text lol 


***read text file in our python file 

``` python
with open(file_path.txt)` as f:
    contents = f. read()

print(contents)

# help command, view documentation
help (f) 

#documentation help
print(dir(f))

```

```python
with open(file_path.txt)` as f:
    contents = f. read()

question ="this string"
print(dir(question))

# prints out all the things you can do with question variable 
```

read
```python

with open(file_path.txt, 'r')` as f:
    contents = f. read()

print(contents)

```

write
```python

with open(file_path.txt, 'w')` as f:
    f.write('more text')

```

append
```python

with open(file_path.txt, 'a')` as f:
     contents= f.write('this text')
    
print (contents)

```

## bytes 

adding images or other files that arent text, come as bytes. non read characters
-`rb` read as bytes, in our terminal returned as string starts with `b'`

```python
with open("pic-1.jpg", mode = 'rb') as f:
    contents =f.read()
print(contents)
#print bytes

print(contents[:128])
#print me these bytes as list 


```

take previous image make duplicate
```python
with open("pic-2.jpg", "wb") as f2:
    f2.write(contents)

```





lab

print madlib cli edition

user input print enter adjective 
enter another adj
enter another noun 

keep function contain, one thing well!!!!!!!!
