import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('LR.csv')
n = len(data.values)
x,y,xy,xsq,p,e = [],[],[],[],[],[]

sxy = [sum(x) for x in zip(*data.values)]

for i in data.values:
    x.append(i[0])
    y.append(i[1])
    xy.append(i[0]*i[1])
    xsq.append(i[0]**2)

a = ((sxy[1]*sum(xsq)) - (sxy[0]*sum(xy)))/((n*sum(xsq)) - sxy[0]**2)
b = ((n*sum(xy)) - (sxy[0]*sxy[1]))/((n*sum(xsq)) - sxy[0]**2)

for i in range(n):
    p.append(b*data.values[i][0] + a)
    # e.append(abs(p[i]-data.values[i][1]))

newx = int(input("Enter a value of x: "))
predp = newx * b + a
print(f"Predicted y of value {newx} is {predp}")


xp = np.array(x)
yp = np.array(p)
nyp = np.array(y)

plt.plot(xp,yp)
plt.scatter(xp,nyp)
plt.show()
