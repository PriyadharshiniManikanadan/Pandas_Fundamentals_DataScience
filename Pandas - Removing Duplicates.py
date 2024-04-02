 # Discovering Duplicates

"""
 Duplicate rows are rows that have been registered more than one time.
 
 By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.

To discover duplicates, we can use the duplicated() method.

The duplicated() method returns a Boolean values for each row"""

# To get the data :

import pandas as pd
df = pd.read_csv("dataset\\testdata.csv")
print(df.to_string())

"""Returns True for every row that is a duplicate, othwerwise False"""

 importpandas as pd
df = pd.read_csv("dataset\\testdata.csv")
print(df.duplicated())

# Removing Duplicates:

"""To remove duplicates, use the drop_duplicates() method."""
import pandas as pd
df = pd.read_csv("dataset\\testdata.csv")
df.drop_duplicates(inplace=True)
print(df.to_string())

"""The (inplace = True) will make sure that the method does NOT return a new DataFrame, 
but it will remove all duplicates from the original DataFrame."""
