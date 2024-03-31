# Read CSV Files

"""
 A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

 use to_string() to print the entire DataFrame."""

import pandas as pd
# data = pd.read_csv("C:\\Users\\priya\\Documents\\Pandas\\COVID-19.csv")
data = pd.read_csv("dataset\\COVID-19.csv")
print(data.to_string())


"""If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:"""


import pandas as pd
data = pd.read_csv("dataset\\COVID-19.csv")
print(data)

print("="* 100)
# MAX rows

"""The number of rows returned is defined in Pandas option settings.

You can check your system's maximum rows with the pd.options.display.max_rows statement."""


import pandas as pd
print(pd.options.display.max_rows)

print("="* 100)

# Increase the maximum number of rows to display the entire DataFrame

"""In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement
 will return only the headers and the first and last 5 rows.

You can change the maximum rows number with the same statement."""

import pandas as pd
pd.options.display.max_rows = 197
data = pd.read_csv("dataset\\COVID-19.csv")
print(data)

print("="* 100)

import pandas as pd
pd.options.display.max_rows = 200
data = pd.read_csv("dataset\\COVID-19.csv")
print(data)
