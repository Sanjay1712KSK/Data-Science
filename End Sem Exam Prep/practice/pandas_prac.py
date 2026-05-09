import pandas as pd
import random
# Series
'''a=pd.Series([10,20,30])
print(a)'''
# DataFrame
data = {"Name": ["Sanjay", "Kumar", "S"], "Age": [20, 21, 20]}  # We have normal dictionary type here
df = pd.DataFrame(data)
# print("Original DataFrame:\n", df)
# Generates synthetic data based on the original dictionary
synthetic_names = ["Sanjay", "Kumar", "S", "Priya", "Amit", "Riya"]
synthetic_ages = [18, 19, 20, 21, 22, 23, 24,'']
synd = {
    "Name": [random.choice(synthetic_names) for _ in range(10)],
    "Age": [random.choice(synthetic_ages) for _ in range(10)]
} # Used random module with fixed names and ages along with list comprehension

d=pd.DataFrame(synd) # Where we use dataframe to structure it proeprly
# Second Synthetic Data Generation
# print("Original DataFrame:\n", df)
# Generates synthetic data based on the original dictionary
synthetic_names2 = ["Sanjeev", "Singh", "A", "Jiya", "Thanu", "Kalaipuli"]
synthetic_ages2 = [58, 69, 30, 31, 32, 29, 25,'']
synd2 = {
    "Name": [random.choice(synthetic_names2) for _ in range(10)],
    "Age": [random.choice(synthetic_ages2) for _ in range(10)]
}
d5 = pd.DataFrame(synd)
d6 = pd.DataFrame(synd2)
# print("The Modified Data \n ",d)
# print("The UnModified Data \n",synd)
# DataFrame Operations
# print(d.head()) # first 5 are printed
# print(d.sort_values(by="Age"))
# print(d.drop_duplicates())
# d.dropna()
'''d.fillna(0)
print("THe one \n",d)'''
'''m=pd.merge(d5,d6,on="Age")
print(m)'''
m1=pd.concat([d5,d6])
print(m1)