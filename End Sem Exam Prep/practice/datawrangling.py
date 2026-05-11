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
p["Name"]=p["Name"].str.strip() 
# Handling missing values
p["Age"]=p["Age"].fillna(p["Age"].mean())
p["Gender"]=p["Gender"].fillna("Unknown")
# Data transformation
''' NO NEED OF TRANSFORMATION HERE AS ALL ARE IN CORRECT TYPE'''
# String manipulation
# same for negative
p["Result"]=p["Result"].replace({"positive":"Positive", "+ve":"Positive", "pos":"Positive", "Pos":"Positive"})
