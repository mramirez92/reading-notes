# 6. Ten Thousand Game 1

## This is important because:

The python random methods can be very powerful. They can generate basically anything depending on the arguments that are passed in.

## Random Module

Random module generates random numbers withing a given range, random element from list, anything random passed in as a argument. 
- `import random`

`randint()`:
- create random strings within a range. 
- 2 numbers as arguments `randint(startRange, endRange)`
  - first number is not inclusive?

`random()`
- generates random numbers between 0 and 1 , returning float point (decimal) between 0 and 1
- for larger numbers, multiply by number ex: `random.random() * 100`, returns number between 0 and 100

`choice()`
- random selection from collection object like list, set, tuple, etc. 
  - `choice(collectionObject)`
```python
#passing in list as argument 
random.choice( ['red', 'black', 'green'] )
```
```python
#passing in a list name as argumet
random.choice(myList)
```

`shuffle()`
- takes in list object as argument, elements are shuffled in random order
```python
x = [[i] for i in range(10)]
shuffle(x)
Output:
# print x  gives  [[9], [2], [7], [0], [4], [5], [3], [1], [8], [6]]
# of course your results will vary
```

`randomrange()`
- `randomrange(start, stop,step)`
- like a combination of `choice()` and `range()`

## Risk Analysis

## Things I want to know more about 
I dont understand fully how shuffle works or random range, need to practice in replit. 

## Resources

[Random Methods](https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python)

[Risk Analysis](https://www.edureka.co/blog/risk-analysis-in-software-testing/)