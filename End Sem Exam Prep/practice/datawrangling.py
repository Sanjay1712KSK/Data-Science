'''questions from - End Sem Exam Prep/PYQs/21CSS303T 08.07.2024.pdf (15 marks)
                    End Sem Exam Prep/PYQs/21CSS303T 10.12.2025 AN.pdf
                    End Sem Exam Prep/PYQs/21CSS303T 13.05.2024 AN.pdf (String manipulation)
                    End Sem Exam Prep/PYQs/21CSS303T 14.07.2025 AN.pdf
                    End Sem Exam Prep/PYQs/21CSS303T 17.05.2025 AN.pdf'''

''' Healthcare organization question
They maintain : 
    1. Electronic medical records
    2. missing values in crtical fields such as age and 
        inconsistent categorical entries in diagnosis 
        and extreme outliers in test scores

To-Do:
    1. Structured data wrangling and cleaning process
    2. strategies for handling missing data
    3. correction of inconsistencies
    4. managing outlier (by IQR , Z-Score)
'''
import pandas as pd
import numpy as np
p=pd.read_csv("healthcare.csv")
# Data cleaning
p=p.drop_duplicates()
p["Name"]=p["Name"].str.strip() 
# Handling missing values
p["Age"]=p["Age"].fillna(p["Age"].mean())
p["Gender"]=p["Gender"].fillna("Unknown")
# Data transformation
''' NO NEED OF TRANSFORMATION HERE AS ALL ARE IN CORRECT TYPE'''
# String manipulation
# same for negative
p["Result"]=p["Result"].replace({"positive":"Positive", "+ve":"Positive", "pos":"Positive", "Pos":"Positive"})
p["City"]=p["City"].str.strip().str.title()
# binning and classing
# No need of categorical need here
# Data Standardization
from sklearn.preprocessing import StandardScaler as ss
scaler=ss()
p["Test_Score"]=scaler.fit_transform(p[["Test_Score"]])
print(p)
# IQR Outlier correction
Q1=p["Age"].quantile(0.25)
Q3=p["Age"].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
p=p[(p("Age")>=lower)&(p("Age")<=upper)]
print(p)
# Data summarization
print(p.summarise())

# Covid Data-set
'''
Data Quality Issues
    Missing values in age and gender
    Misspelled city names
    Inconsistent test results:
    Positive
    POS
    +ve
    Unrealistic outliers:
        Age > 200
        Duplicate records
'''
c=pd.read_csv("covid_data.csv")
c=c.drop_duplicates()
c["Age"]=c["Age"].fillna(c["Age"].mean())
c["Gender"]=c["Gender"].fillna("Unknown")
c["Test_Result"]=c["Test_Result"].replace({"positive":"Positive", "+ve":"Positive", "pos":"Positive", "Pos":"Positive"})
c["City"]=c["City"].str.strip().str.title()
Q1=c["Age"].quantile(0.25)
Q3=c["Age"].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*(IQR)
upper=Q3+1.5*(IQR)
p=p[(p["Age"]>=lower)&(p["Age"]<=upper)]
print(p)
print(p.summarise())
print(c.summarise())
# Binning sample snippet