# 11. Data Analysis

JupyterLab is a user interface for Project Jupyter that allows users to work with a range of documents and activities, including Jupyter notebooks, text editors, and terminals in a flexible and extensible manner. It enables users to arrange multiple documents and activities side by side and offers customizable keyboard shortcuts and the ability to use key maps from other text editors. JupyterLab also has the ability to display and handle a variety of data formats, and can be customized or enhanced through the use of extensions. It is intended to eventually replace the classic Jupyter Notebook, but will continue to support the same notebook document format.

# NumPy

NumPy is a numerical computing library for Python
- used for working with arrays and matrices of numerical data
- perform mathematical and statistical operations on large amounts of data efficiently
NumPy arrays are similar to lists in Python, but they are more efficient and require less code

CREATING ARRAYS
- `np.array([1,2,3])` - One dimensional array
- `np.array([(1,2,3),(4,5,6)])` - Two dimensional array
- `np.zeros(3)` - 1D array of length 3 all values 0
- `np.ones((3,4))` - 3x4 array with all values 1

ADDING/REMOVING ELEMENTS
- `np.append(arr,values)` - Appends values to end of arr
- `np.insert(arr,2,values)` - Inserts values into arr before index 2
- `np.delete(arr,3,axis=0)` - Deletes row on index 3 of arr
- `np.delete(arr,4,axis=1)` - Deletes column on index 4 of arr

You can create NumPy arrays using the numpy module and various functions, such as array, zeros, and ones

You can also create NumPy arrays from existing data, such as lists and tuples

NumPy arrays have attributes such as shape, ndim, and dtype that allow you to understand the structure and data type of the array . NumPy arrays support indexing and slicing, just like Python lists
You can perform element-wise operations on NumPy arrays using arithmetic operators and NumPy functions . You can also perform operations between arrays, such as dot products and matrix multiplication
NumPy provides many useful functions for working with arrays, such as min, max, mean, and std
NumPy also has functions for working with linear algebra, random numbers, and statistical tests

## Resources: 

[NumPy](https://www.dataquest.io/blog/numpy-tutorial-python/)

[NumPy Cheatsheet](https://s3.amazonaws.com/dq-blog-files/numpy-cheat-sheet.pdf)

[Jupyter](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)