'''
Questions from - End Sem Exam Prep/PYQs/21CSS303T 08.07.2024.pdf
                 End Sem Exam Prep/PYQs/21CSS303T 10.12.2025 AN.pdf
                 End Sem Exam Prep/PYQs/21CSS303T 13.05.2024 AN.pdf
                 End Sem Exam Prep/PYQs/21CSS303T 14.07.2025 AN.pdf
                 End Sem Exam Prep/PYQs/21CSS303T 17.05.2025 AN.pdf

'''
import matplotlib.pyplot as plt
import seaborn as sns

Q24
Briefly Explain Line Plot, Scatter Plot, Histogram and Boxplot
Line Plot

A line plot is used to show trends or changes over continuous intervals such as time.

Example:

stock market analysis
sales growth

Python:

plt.plot(x,y)
Scatter Plot

Scatter plot displays relationship between two variables using points.

Example:

height vs weight

Python:

plt.scatter(x,y)
Histogram

Histogram represents frequency distribution of numerical data.

Example:

marks distribution

Python:

plt.hist(data,bins=5)
Boxplot

Boxplot shows distribution and identifies outliers.

Python:

plt.boxplot(data)

Q25
Formatting Options for Ticks, Labels and Legends
Ticks

Used to customize axis intervals.

plt.xticks([0,10,20])
Labels

Used to describe axes.

plt.xlabel("Months")
plt.ylabel("Sales")
Legends

Used to identify multiple plots.

plt.legend()
Applications
improves readability
improves presentation
helps identify trends clearly

Q26
Histogram Program
import matplotlib.pyplot as plt

data = [10,20,20,30,30,30,40]

plt.hist(data,bins=4)

plt.title("Histogram")

plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()
Attributes of Histogram
Bins
Frequency
Distribution shape
Range
Skewness

Q26
3D Surface Plot
Explanation

A 3D surface plot represents three-dimensional data using X, Y, and Z axes.

Applications:

terrain mapping
weather forecasting
engineering simulations
scientific analysis

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
x=np.arange(-5,5,1)
y=np.arange(-5,5,1)
X,Y=np.meshgrid(x,y)
Z=x**2+y**2
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z)
plt.savefig("3dgraph.jpg")

Q23
Financial Analyst Visualization Question
Line Plot

Shows:

revenue trends over years
Bar Plot

Compares:

regional profits
expenditures
Histogram

Displays:

frequency distribution
revenue spread
Boxplot

Identifies:

anomalies
outliers
Pairplot

Shows:

relationships between revenue, expenditure, and profit
Strategic Benefits

These visualizations help:

identify growth trends
detect anomalies
compare regions
support business decisions