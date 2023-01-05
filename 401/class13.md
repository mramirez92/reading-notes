# 13. Linear Regression

Scikit-learn is a Python package that simplifies the implementation of a wide range of Machine Learning (ML) methods for predictive data analysis, including linear regression.

Linear regression can be thought of as finding the straight line that best fits a set of scattered data points
- project line to predict new data points. 

- Best Fit – the straight line in a plot that minimizes the deviation between related scattered data points.
- Coefficient – also known as a parameter, is the factor a variable is multiplied by. In linear regression, a coefficient represents changes in a Response Variable (see below).
- Coefficient of Determination – the correlation coefficient denoted as 𝑅². Used to describe the precision or degree of fit in a regression. 
- Correlation – the relationship between two variables in terms of quantifiable strength and degree, often referred to as the ‘degree of correlation’.  Values range between -1.0 and 1.0. 
- Dependent Feature – a variable denoted as y in the slope equation y=ax+b. Also known as an Output, or a Response. 
- Estimated Regression Line – the straight line that best fits a set of scattered data points.
- Independent Feature – a variable denoted as x in the slope equation y=ax+b. Also known as an Input, or a predictor. 
- Intercept – the location where the Slope intercepts the Y-axis denoted b in the slope equation y=ax+b. 
- Least Squares – a method of estimating a Best Fit to data, by minimizing the sum of the squares of the differences between observed and estimated values.
- Mean – an average of a set of numbers, but in linear regression, Mean is modeled by a linear function.
- Ordinary Least Squares Regression (OLS) – more commonly known as Linear Regression. 
- Residual – vertical distance between a data point and the line of regression (see Residual in Figure 1 below).
- Regression – estimate of predictive change in a variable in relation to changes in other variables (see Predicted Response in Figure 1 below).
- Regression Model – the ideal formula for approximating a regression.
- Response Variables – includes both the Predicted Response (the value predicted by the regression) and the Actual Response, which is the actual value of the data point (see Figure 1 below).
- Slope – the steepness of a line of regression. Slope and Intercept can be used to define the linear relationship between two variables: y=ax+b.
- Simple Linear Regression – a linear regression that has a single independent variable.

create linear regression model
```python
# Create an instance of a linear regression model and fit it to the data with the fit() function:
model = LinearRegression().fit(x, y) 

# The following section will get results by interpreting the created instance: 

# Obtain the coefficient of determination by calling the model with the score() function, then print the coefficient:
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

# Print the Intercept:
print('intercept:', model.intercept_)

# Print the Slope:
print('slope:', model.coef_) 

# Predict a Response and print it:
y_pred = model.predict(x)
print('Predicted response:', y_pred, sep='\n')
```

create linear regression model and display it
```python
# Import the packages and classes needed for this example:
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create random data with numpy, and plot it with matplotlib:
rnstate = np.random.RandomState(1)
x = 10 * rnstate.rand(50)
y = 2 * x - 5 + rnstate.randn(50)
plt.scatter(x, y);
plt.show()

# Create a linear regression model based the positioning of the data and Intercept, and predict a Best Fit:
model = LinearRegression(fit_intercept=True)
model.fit(x[:, np.newaxis], y)
xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])

# Plot the estimated linear regression line with matplotlib:
plt.scatter(x, y)
plt.plot(xfit, yfit);
plt.show()
```

## Resources: 
[linear regression](https://www.activestate.com/resources/quick-reads/how-to-run-linear-regressions-in-python-scikit-learn/)

Command Line Heroes, S2: Ep.4 Fail better
Failing is part of the process. Failing push us to adapt and leads to learning. At google failures are given a post-mortem reports. These reports contain actions to prevent, detect and mitigate similar incidents or issues in the future. 
- blamelessness allows for less fear of failure, allowing failures to be a learning opportunity.
"Failure is inevitable, but you never want to fail the same way twice. To err is human, but to err repeatedly is something that would be better avoided" - Jennifer Petoff
The popular Grand Theft Auto was product of its initial concept failure. The algorithm was not working as intended, in order to tweak it to work correctly it was deciced to put the game in front of test players. The "failures" in their algorithm was what the players enjoyed the most. The concept was shifted from a racing game, to Grand Theft Auto. 
It exists because they failed to get the algorithm right and decided to try it out anyway.

Our mistakes nudge us toward bigger things. They make up most of our journey. 

https://www.redhat.com/en/command-line-heroes/season-2/fail-better

Command Line Heroes , S3: Ep: Pythons Tail:

Guido Van Rossum saw a need for a new program language when working with C. Key to Python's attractiveness was its extensibility. In 2018, more people did Google searches for Python than for Kim Kardashian. All that excitement has it jostling for the title of most-used language against options like Java, C, and C++.
A lot of machine learning libraries are Pyton. Data science! You can build simple and complex things. Python because of its creator opened the door for diversity in this field.They brought in the concept of codes of conduct for conferences, diversity scholarships, all of that sort of stuff. By bringing in different voices, this allows more people to be able to understand in a way that is more familiar to them. Its creator stepping down and handing down the reigns, allowing for community development and growth. 