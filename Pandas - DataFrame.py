# DataFrame
"""
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table

A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns."""

# Example 1

import pandas as pd
sampledata = {    "Calories" : [420,562,265],
    "Duration" : [50,60,55]
}
myvar = pd.DataFrame(sampledata)
print(myvar)

# Example 2

import pandas as pd

Stu_details = {"ID":[123,321,456,654],"NAMES": ["Akshaya","Madhumitha","Vasanth","Cheziyan"],"Scores": [85,73,98,55]}
myvar = pd.DataFrame(Stu_details)
print(myvar)

# Local Rows :

"""Pandas use the loc attribute to return one or more specified row(s)

This example returns a Pandas Series."""

print("="* 100)


Stu_details = {"ID":[123,321,456,654],"NAMES": ["Akshaya","Madhumitha","Vasanth","Cheziyan"],"Scores": [85,73,98,55]}
myvar = pd.DataFrame(Stu_details)
print(myvar.loc[0])

Stu_details = {"ID":[123,321,456,654],"NAMES": ["Akshaya","Madhumitha","Vasanth","Cheziyan"],"Scores": [85,73,98,55]}
myvar = pd.DataFrame(Stu_details)
print(myvar.loc[2])

print("="* 100)
# Return row 0 and 1:

Stu_details = {"ID":[123,321,456,654],"NAMES": ["Akshaya","Madhumitha","Vasanth","Cheziyan"],"Scores": [85,73,98,55]}
myvar = pd.DataFrame(Stu_details)
print(myvar.loc[[0,1]])

""" 
So , when we use 
 loc attribute == the result is Series
  [[ ]] == the result is DataFrame
  
  """
print("="* 100)
# NAMED INDEX

"""With the index argument, you can name your own indexes."""

import pandas as pd

Stu_details = {"ID":[123,321,456,654],"NAMES": ["Akshaya","Madhumitha","Vasanth","Cheziyan"],"Scores": [85,73,98,55]}
data = pd.DataFrame(Stu_details, index = ["Maths","Science","Social", "Language"])
print(data)

print("="* 100)
# Locate Named Indexes

"""Use the named index in the loc attribute to return the specified row(s)."""

#Return "Maths":

import pandas as pd

Stu_details = {"ID":[123,321,456,654],"NAMES": ["Akshaya","Madhumitha","Vasanth","Cheziyan"],"Scores": [85,73,98,55]}
data = pd.DataFrame(Stu_details, index = ["Maths","Science","Social", "Language"])
print(data.loc["Maths"])

print("="* 100)
# Load Files Into a DataFrame

"""If data sets are stored in a file, Pandas can load them into a DataFrame"""

import pandas as pd
data = pd.read_csv("C:\\Users\\priya\\Documents\\Pandas\\data.csv.txt")
print(data)

