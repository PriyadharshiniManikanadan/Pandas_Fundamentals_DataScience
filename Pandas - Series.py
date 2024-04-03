# Import Pandas

"""
Pandas is a Python library used for working with data sets.

It has functions for analyzing, cleaning, exploring, and manipulating data.

The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.
"""

"""Pandas is usually imported under the pd alias."""

import pandas as pd

dataset1 = {
          'NAMES': ["Mani","Priya","Utsav","Inbav"],
            'AGE' : [34,31,7,2]
           }
mytable = pd.DataFrame(dataset1)

print(mytable)


#Version check

print(pd.__version__)


# Pandas Series
"""
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type."""

import pandas as pd
GENDER = ("Male", "Female", "Male", "Male")
myvar = pd.Series(GENDER)
print(myvar)

import pandas as pd
a = [1,2,3,4]
myvar = pd.Series(a)
print(myvar)

# Labels

"""
If nothing else is specified, the values are labeled with their index number. First value has index 0, 
second value has index 1 etc.

This label can be used to access a specified value."""

a = [1,2,3,4]
myvar = pd.Series(a)
print(myvar[0])

print("=" * 100)

b = [5,10,15,20,25,30]
var = pd.Series(b)
print(var[2])

print("=" * 100)

# Create Labels

""" With the index argument, you can name your own labels"""

a = [1,2,3,4]
myvar = pd.Series(a, index = ['A','B','C','D'])
print(myvar)

b = [5,10,15,20,25,30]
var = pd.Series(b,index = ["A","B","C","D","E","F"])
print(var)

# When you have created labels, you can access an item by referring to the label.

print(var['B'])

# Key/Value Objects as Series

"""can also use a key/value object, like a dictionary, when creating a Series
 
 The keys of the dictionary become the labels."""

import pandas as pd

calories = {"Day1" : 420, "Day2" : 580, "Day3" : 265}
myvar = pd.Series(calories)
print(myvar)

print("="*100)

series = pd.Series(list('123456789'))
print(series)
series.name = 'Numbers'
print(series)

