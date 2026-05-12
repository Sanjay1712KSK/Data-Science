
import numpy as np

arr = np.array([1,2,3,4,5,6])

reshaped = arr.reshape(2,3)

print(reshaped)

import pandas as pd

df = pd.DataFrame({
    "Name":["Ram","Ram","Sam","Sam"],
    "Subject":["Math","Science","Math","Science"],
    "Marks":[80,90,75,85]
})

pivot_df = df.pivot(
    index="Name",
    columns="Subject",
    values="Marks"
)

print(pivot_df)