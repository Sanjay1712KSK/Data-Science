import matplotlib.pyplot as plt
import seaborn as sns

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
plt.show()

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
plt.show()

'''4. BAR PLOT
Purpose

Used to compare categories.

Python Code
'''
students = ["Ram","Sam","John"]
marks = [80,90,75]
plt.bar(students, marks)
plt.title("Bar Plot")
plt.show()

'''5. HISTOGRAM

VERY IMPORTANT PYQ.

Purpose

Used to display:

frequency distribution
Python Code
'''
data = [10,20,20,30,30,30,40]

plt.hist(data, bins=4)

plt.title("Histogram")

plt.show()

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

plt.show()

'''
7. PIE CHART
Purpose

Shows proportions.

Python Code
'''
sizes = [40,30,20,10]
labels = ["A","B","C","D"]

plt.pie(sizes, labels=labels)

plt.show()

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
plt.show()
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
'''8. MULTIPLE PLOTS (SUBPLOTS)

VERY IMPORTANT PYQ.

Python Code
x = [1,2,3]
y = [2,4,6]
'''
plt.subplot(1,2,1)
plt.plot(x,y)

plt.subplot(1,2,2)
plt.bar(x,y)

plt.show()
'''
Meaning of:
subplot(rows, columns, position)

Example:

subplot(1,2,1)

means:

1 row
2 columns
first plot'''

'''9. CONTROLLING AXES
Python Code'''

x = [1,2,3,4]
y = [10,20,30,40]

plt.plot(x,y)

plt.xlim(0,5)
plt.ylim(0,50)

plt.show()

'''
| Function | Purpose        |
| -------- | -------------- |
| xlim()   | control x-axis |
| ylim()   | control y-axis |
'''