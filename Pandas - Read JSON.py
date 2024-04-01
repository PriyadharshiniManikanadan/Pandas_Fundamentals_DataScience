# Read JSON

"""
Big data sets are often stored, or extracted as JSON.

JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

In our examples we will be using a JSON file called 'data.json'.
"""


# Load the JSON file into a DataFrame

# use to_string() to print the entire DataFrame

import pandas as pd
data = pd.read_json("dataset\\Data.json")
print(data.to_string())

print("="* 100)

import pandas as pd
data = pd.read_json("dataset\\Data.json")
print(data)

print("="* 100)

# Dictionary as JSON

"""
JSON = Python Dictionary

JSON objects have the same format as Python dictionaries.

If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly
"""

import pandas as pd

data = {
    "Names":{
        "0":"Saravanan",
        "1":"Shanthy",
        "2":"Shanthi",
        "3":"Manikandan",
        "4":"Priyadharshini",
        "5":"Utsav",
        "6":"Inbav",
        "7":"Deekshith"
    },
    "Age":{
        "0":65,
        "1":54,
        "2":54,
        "3":34,
        "4":31,
        "5":7,
        "6":2,
        "7":3
    },
    "Gender":{
        "0":"Male",
        "1":"Female",
        "2":"Female",
        "3":"Male",
        "4":"Female",
        "5":"Male",
        "6":"Male",
        "7":"Male"
    },
    "Weight":{
        "0":74.1,
        "1":68,
        "2":65.8,
        "3":80,
        "4":52.3,
        "5":22.5,
        "6":12.1,
        "7":15.4
    }
}
df = pd.DataFrame(data)
print(df.to_string())


