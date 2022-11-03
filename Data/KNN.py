import numpy as np
import pandas as pd
import math
import statistics
from statistics import mode
from collections import OrderedDict

df = pd.read_csv('/content/KNND1.csv')
print(df)
 

x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))



dist={}

for i in range(df.shape[0]):
  a=(int)(df.iloc[i][0])
  b = (int)(df.iloc[i][1])
  c = (x-a)*(x-a)
  d = (y-b)*(y-b)
  temp = math.sqrt(c+d)
  dist[temp] = df.iloc[i][2]


dist1 = OrderedDict(sorted(dist.items()))


k=int(input("Enter the value of k : "))
list1=[*dist1.values()]

print(list1)

list2 =[]
for i in range(k):
  list2.insert(i,list1[i])
print(list2)
print("The unknown observation is classified as",mode(list2))

