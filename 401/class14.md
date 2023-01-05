# 14. Matplotlib

Matplotlib is a popular python package that helps us visualize data.
-  can customize data visuals by figure size and dpi, line width, color and style, axes, axis and grid properties, text and font properties

Simple plot
draw the cosine and sine functions on the same plot. 

get the data for the sine and cosine functions:

```python
import numpy as np

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
```
X is now a NumPy array with 256 values ranging from -π to +π (included). C is the cosine (256 values) and S is the sine (256 values).

customize line width: 
```python
...
plt.figure(figsize=(10,6), dpi=80)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-")
...
```

set limits:
```python
...
plt.xlim(X.min()*1.1, X.max()*1.1)
plt.ylim(C.min()*1.1, C.max()*1.1)
...
```

add legend:
```python
...
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")

plt.legend(loc='upper left', frameon=False)
...
```

## Things I want to know more about:
I want to know what exactly im looking at and how to animate my data. 
## Resources
[Matplotlib](https://github.com/rougier/matplotlib-tutorial)

