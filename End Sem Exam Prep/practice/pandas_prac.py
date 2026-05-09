import pandas as pd
import random
# Series
'''a=pd.Series([10,20,30])
print(a)'''
# DataFrame
data = {"Name": ["Sanjay", "Kumar", "S"], "Age": [20, 21, 20]}  # We have normal dictionary type here
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# Generates synthetic data based on the original dictionary
synthetic_names = ["Sanjay", "Kumar", "S", "Priya", "Amit", "Riya"]
synthetic_ages = [18, 19, 20, 21, 22, 23, 24]
synd = {
    "Name": [random.choice(synthetic_names) for _ in range(10)],
    "Age": [random.choice(synthetic_ages) for _ in range(10)]
}

'''d=pd.DataFrame(synd) # Where we use dataframe to structure it proeprly
print("The Modified Data \n ",d)
print("The UnModified Data \n",synd)'''
