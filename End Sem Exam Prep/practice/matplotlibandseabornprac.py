import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

'''LINE PLOT
Purpose

Used to show:

trends over time
continuous changes
Python Code'''

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x, y)

plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.plot(x,y,label="2024")
plt.plot(x,y,label="2025")
plt.legend()
plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/lineplot.jpg")

'''
| Function | Purpose          |
| -------- | ---------------- |
| plot()   | create line plot |
| title()  | add title        |
| xlabel() | x-axis label     |
| ylabel() | y-axis label     |
| show()   | display graph    |
'''
'''
3. SCATTER PLOT
Purpose

Used to show:

relationship between two variables
Python Code
'''
x = [1,2,3,4]
y = [10,20,15,30]
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/scatterplot.jpg")

'''4. BAR PLOT
Purpose

Used to compare categories.

Python Code
'''
students = ["Ram","Sam","John"]
marks = [80,90,75]
plt.bar(students, marks)
plt.title("Bar Plot")
plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/barplot.jpg")

'''5. HISTOGRAM

VERY IMPORTANT PYQ.

Purpose

Used to display:

frequency distribution
Python Code
'''
data = [10,20,20,30,30,30,40]

plt.hist(data, bins=5)

plt.title("Histogram")

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/histogram.jpg")

'''Important Parameter
bins

Controls number of intervals.'''

'''6. BOXPLOT

VERY IMPORTANT.

Purpose

Used for:

distribution
outlier detection
Python Code'''

data = [10,12,13,14,100]

plt.boxplot(data)

plt.title("Box Plot")

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/boxplot.jpg")

'''
7. PIE CHART
Purpose

Shows proportions.

Python Code
'''
sizes = [40,30,20,10]
labels = ["A","B","C","D"]

plt.pie(sizes, labels=labels)

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/piechart.jpg")

'''8. MULTIPLE PLOTS (SUBPLOTS)

VERY IMPORTANT PYQ.

Python Code
'''
x = [1,2,3]
y = [2,4,6]
plt.subplot(1,2,1)
plt.plot(x,y)
plt.subplot(1,2,2)
plt.bar(x,y)
plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/multipleplots.jpg")
'''
Meaning of:
subplot(rows, columns, position)

Example:

subplot(1,2,1)

means:

1 row
2 columns
first plot
'''

'''9. CONTROLLING AXES
Python Code'''

x = [1,2,3,4]
y = [10,20,30,40]

plt.plot(x,y)

plt.xlim(0,5)
plt.ylim(0,50)

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/lineplot_controlling_axes.jpg")

'''
| Function | Purpose        |
| -------- | -------------- |
| xlim()   | control x-axis |
| ylim()   | control y-axis |
'''

'''10. TICKS
Purpose

Customize axis markings.

Python Code
'''
x = [1,2,3]
y = [10,20,30]

plt.plot(x,y)

plt.xticks([1,2,3])
plt.yticks([10,20,30])

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/lineplot_ticks.jpg")

'''11. LABELS AND LEGENDS

VERY IMPORTANT.

Python Code
'''
x = [1,2,3]
y = [2,4,6]

plt.plot(x,y,label="Line")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.legend()

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/lineplot_labelsandlegends.jpg")
'''12. ANNOTATIONS

PYQ Topic.

Purpose

Add text on graph.

Python Code
'''
x = [1,2,3]
y = [10,20,15]

plt.plot(x,y)

plt.annotate(
    "Peak",
    xy=(2,20)
)

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/lineplot_annotations.jpg")
'''
13. SAVE PLOT

Repeated MCQ.

Python Code
'''
plt.plot([1,2,3],[4,5,6])

plt.savefig("simplegraph.png")

'''14. STYLING PLOTS
Change Color and Line Style
'''
plt.plot(
    [1,2,3],
    [4,5,6],
    color="red",
    linestyle="--",
    linewidth=2
)

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/lineplot_stylingplots.jpg")

'''15. SEABORN LINE PLOT
Python Code'''

df = pd.DataFrame({
    "x":[1,2,3,4],
    "y":[10,20,15,30]
})

sns.lineplot(x="x", y="y", data=df)

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/lineplot_seaborn.jpg")

'''16. SEABORN SCATTER PLOT
Python Code'''

sns.scatterplot(
    x="x",
    y="y",
    data=df
)

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/scatter_seaborn.jpg")
'''
17. SEABORN BAR PLOT
Python Code
'''
sns.barplot(
    x="x",
    y="y",
    data=df
)

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/bar_seaborn.jpg")

'''18. SEABORN HISTOGRAM
Python Code
'''
sns.histplot(df["y"])

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/histogram_seaborn.jpg")
'''19. SEABORN BOXPLOT

VERY IMPORTANT.

Python Code'''

sns.boxplot(y=df["y"])

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/boxplot_seaborn.jpg")

'''20. PAIRPLOT

VERY IMPORTANT PYQ.

Purpose

Shows pairwise relationships.

Python Code'''

sns.pairplot(df)

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/pairplot_seaborn.jpg")
'''
21. HEATMAP

Repeated PYQ sometimes.

Python Code'''

data = np.array([
    [1,2],
    [3,4]
])

sns.heatmap(data)

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/heatmap_seaborn.jpg")
'''
22. 3D SURFACE PLOT

VERY IMPORTANT LONG QUESTION.

Python Code
'''
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-5,5,1)
y = np.arange(-5,5,1)

X, Y = np.meshgrid(x,y)

Z = X**2 + Y**2

fig = plt.figure()

ax = fig.add_subplot(
    111,
    projection='3d'
)

ax.plot_surface(X,Y,Z)

plt.savefig("/home/sanjaykumars/Desktop/DS/End Sem Exam Prep/matplotlibandseabornoutputscreenshots/3dplot.jpg")

'''
| Function       | Purpose        |
| -------------- | -------------- |
| plt.plot()     | line plot      |
| plt.scatter()  | scatter plot   |
| plt.bar()      | bar plot       |
| plt.hist()     | histogram      |
| plt.boxplot()  | box plot       |
| plt.subplot()  | multiple plots |
| plt.savefig()  | save graph     |
| plt.annotate() | add text       |
| sns.pairplot() | pairwise plots |
| sns.heatmap()  | heatmap        |
'''

'''
MEMORY TRICKS
Histogram

Frequency distribution

Scatter Plot

Relationship between variables

Boxplot

Outlier detection

Pairplot

All pairwise relations

subplot()

Many graphs in one figure
'''