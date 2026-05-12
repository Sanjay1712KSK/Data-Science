1. HOW TO DRAW VISUALIZATIONS IN EXAM

These rough sketches are enough in theory papers.

LINE PLOT
Purpose

Shows trend over time.

Example:

sales growth
stock price
temperature change
Rough Exam Sketch
Sales
 ^
 |                *
 |            *
 |        *
 |    *
 | *
 +--------------------> Time

Points connected by lines.

Interpretation

If line goes upward:

increasing trend

Downward:

decreasing trend
SCATTER PLOT
Purpose

Shows relationship between two variables.

Example:

height vs weight
study hours vs marks
Rough Exam Sketch
Weight
 ^
 |         *      *
 |    *  
 |              *
 |  *      *
 +--------------------> Height

Points are NOT connected.

Interpretation

If points move upward diagonally:

positive correlation
BAR PLOT
Purpose

Compare categories.

Rough Exam Sketch
Marks
 ^
 |        ████
 |   ████ ████
 |   ████ ████
 |   ████ ████
 +--------------------> Students
      A    B
HISTOGRAM
Purpose

Frequency distribution.

Looks similar to bar graph BUT:

bars touch each other
represents intervals
Rough Exam Sketch
Frequency
 ^
 |        ████
 |    ████████
 | ███████████
 +--------------------> Values
BOXPLOT
Purpose

Outlier detection + distribution.

Rough Exam Sketch
          *
 --------|----|--------
        [____]

Where:

box = middle 50%
line = median
star/dot = outlier
PIE CHART
Purpose

Show proportions.

Rough Exam Sketch
      ______
    /   |    \\
   /____|_____\\

Circle divided into sectors.

2. WHAT ARE BINS IN HISTOGRAM?

This is VERY important.

Layman Meaning

Bins are:

interval groups

Histogram groups data into ranges.

Example

Suppose marks:

[10,20,25,30,40,45,50]

If:

bins=5

then histogram creates:

5 intervals

Like:

0-10
10-20
20-30
30-40
40-50

and counts how many values fall inside each interval.

Visual Meaning

More bins:

more detailed graph

Fewer bins:

smoother graph
Example Code
plt.hist(data, bins=5)
If bins are too small

Graph becomes:

too noisy
If bins are too large

Graph hides patterns.

3. WHAT ARE SUBPLOTS?

VERY IMPORTANT PYQ.

Why Use Subplots?

Suppose company wants:

sales graph
profit graph
customer graph

in ONE figure.

Instead of opening 3 windows:

we divide one figure into sections

That is:

subplot
Real-Life Analogy

Like newspaper:

many images in one page.
Syntax
plt.subplot(rows, columns, position)

Example:

plt.subplot(2,2,1)

means:

2 rows
2 columns
first graph position
Visual Output
+---------+---------+
| Plot 1  | Plot 2  |
+---------+---------+
| Plot 3  | Plot 4  |
+---------+---------+
Can We Use Any Plot in Subplots?

YES.

VERY IMPORTANT.

You can use:

line plot
histogram
scatter plot
pie chart
boxplot
seaborn plots

Anything.

Example
plt.subplot(2,2,1)
plt.plot(x,y)

plt.subplot(2,2,2)
plt.scatter(x,y)

plt.subplot(2,2,3)
plt.hist(data)

plt.subplot(2,2,4)
plt.bar(x,y)

plt.show()
4. WHAT DOES xlim() AND ylim() DO?

These control:

visible axis range
Example Without xlim

Suppose x-axis:

0 to 100
Using:
plt.xlim(20,60)

Now graph only shows:

20 to 60

range.

Visual Understanding

Without xlim:

0------------------------100

With xlim(20,60):

20-----------60

Zoomed portion.

ylim()

Same idea for y-axis.

Why Use Them?

To:

zoom graph
focus on important region
remove unnecessary empty space
5. WHAT ARE TICKS / AXIS MARKINGS?

Ticks are:

numbers shown on axes

Example:

0  10  20  30

on x-axis.

Yes — We ARE Changing Intervals

Exactly.

Example
plt.xticks([0,10,20,30])

Now axis markings appear only at:

0,10,20,30
Why Useful?

Helps:

readability
highlighting important values
custom scales
Example

Without custom ticks:

automatic intervals

With custom ticks:

manual intervals
6. BETTER EXPLANATION OF STYLING + EDITING

Now let’s deeply understand visualization customization.

TITLE
plt.title("Sales Report")

Adds heading.

LABELS
plt.xlabel("Months")
plt.ylabel("Revenue")

Explains axes.

LEGEND

Suppose multiple lines:

plt.plot(x,y1,label="2024")
plt.plot(x,y2,label="2025")

plt.legend()

Legend tells:

which line represents what
ANNOTATIONS

Used to highlight important point.

Example
plt.annotate(
    "Highest Sales",
    xy=(5,100)
)

Adds note on graph.

STYLING LINES
color
color="red"

Changes line color.

linestyle
linestyle="--"

Makes dashed line.

linewidth
linewidth=3

Makes thicker line.

marker
marker="o"

Adds circular points.

Example Combined
plt.plot(
    x,
    y,
    color="red",
    linestyle="--",
    linewidth=2,
    marker="o"
)
SEABORN BETTER EXPLANATION

Seaborn is:

advanced statistical visualization library

built on:

Matplotlib
Why Use Seaborn?

Because:

prettier graphs
less code
better statistical plots
Example

Matplotlib scatter:

plt.scatter(x,y)

Seaborn scatter:

sns.scatterplot(x=x,y=y)

Cleaner and more attractive.

PAIRPLOT

Very important.

Automatically creates:

all pairwise relationships
Visual Idea

Suppose columns:

Age
Salary
Experience

Pairplot automatically creates:

Age vs Salary
Age vs Experience
Salary vs Experience

all together.

HEATMAP

Used for:

correlation visualization

Darker color:

strong relationship