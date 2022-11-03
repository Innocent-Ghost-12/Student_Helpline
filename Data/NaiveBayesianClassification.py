import pandas as pd
import numpy as np

data = pd.read_csv('Fruit.csv')
l = dict()
val = [1]*(len(data.values) - 1)
ran = len(data.values[0]) - 1
for i in range(len(val)):
    for j in range(1,ran):
        val[i] *= (data.values[i][j])/(data.values[i][4])
    l[f"{data.values[i][0]}"] = val[i]

# print(max(val))
# print(data.values[val.index(max(val))][0])

print(l)
