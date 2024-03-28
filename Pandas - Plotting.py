# plotting :

"""
Pandas uses the plot() method to create diagrams.

We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
"""
# Import pyplot from Matplotlib and visualize our DataFrame

# import matplotlib

import matplotlib

print(matplotlib.__version__)

# import sys
# import matplotlib
# matplotlib.use('Agg')

# Import pyplot from Matplotlib and visualize our DataFrame

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset\\corr_data.csv")
df.plot()
plt.show()

# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()

# Scatter Plot

"""
Specify that you want a scatter plot with the kind argument:

kind = 'scatter'

A scatter plot needs an x- and a y-axis.

In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.

Include the x and y arguments like this

x = 'Duration', y = 'Calories'"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset\\corr_data.csv")
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()

#Remember:
 #       In the previous example, we learned that the correlation between "Duration" and "Calories" was 0.922721,
#  and we concluded with the fact that higher duration means more calories burned.

 # Let's create another scatterplot, where there is a bad relationship between the columns,
 # like "Duration" and "Maxpulse", with the correlation 0.009403:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset\\corr_data.csv")
df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()

# Histogram

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset\\corr_data.csv")
df["Duration"].plot(kind = 'hist')
plt.show()

# The histogram tells us that there were over 100 workouts that lasted between 50 and 60 minutes.
