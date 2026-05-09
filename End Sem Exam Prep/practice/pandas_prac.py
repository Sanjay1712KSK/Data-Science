import pandas as pd
'''a=pd.Series([10,20,30])
print(a)'''
data={"Name":["Sanjay","Kumar","S"], "Age":[20,21,20]} # We have normal dictionary type here
d=pd.DataFrame(data) # Where we use dataframe to structure it proeprly
print("The Modified Data \n ",d)
print("The UnModified Data \n",data)