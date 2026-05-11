import pandas as pd
import numpy as np

data = {
    "Name": ["Ram ", "Sam", "John", "Ram "],
    "Age": [20, np.nan, 22, 20],
    "Marks": [85, 90, 500, 85]
}

df = pd.DataFrame(data)

print(df)

'''STEP 1 — Data Cleaning

Data cleaning removes:

duplicates
unwanted spaces
inconsistent values
Remove Duplicates'''

df = df.drop_duplicates()

# Remove Extra Spaces
df["Name"] = df["Name"].str.strip()

'''STEP 2 — Handling Missing Values

Missing values are represented as:

NaN
Fill Missing Values'''

df["Age"] = df["Age"].fillna(df["Age"].mean())

'''STEP 3 — Data Transformation

Transformation converts data into suitable format.

Convert Data Type'''

df["Age"] = df["Age"].astype(int)

'''STEP 4 — String Manipulation

Used to modify text data.

Convert Names to Uppercase'''

df["Name"] = df["Name"].str.upper()

'''STEP 5 — Data Summarization

Used to generate statistical summary.'''

print(df.describe())
'''STEP 6 — Binning / Classing
Binning groups numerical data into categories.'''


df["Category"] = pd.cut(
    df["Marks"],
    bins=[0,50,100,600],
    labels=["Low","Medium","High"]
)
print(df)

'''STEP 7 — Standardization

Standardization scales data so that:

mean = 0
standard deviation = 1'''
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

df["Marks"] = scaler.fit_transform(df[["Marks"]])

print(df)