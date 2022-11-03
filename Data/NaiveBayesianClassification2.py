import pandas as pd

data = pd.read_csv('Car Dataset.csv')
# inp = list(map(str, input().split()))
inp = ["Red","Sports","Domestic"]
l = [x for x in data.keys()]
total = len(data.values)
totaly = data[data[f'{l[-1]}'] == "Yes"].count()[0]
proby = totaly/total
totaln = total - totaly
probn = 1 - proby
py,pn = 1,1

for i in range(len(l) - 1):
    daty = data[data[f'{l[i]}'] == f"{inp[i]}"][data[f'{l[-1]}'] == "Yes"].count()[0]
    datn = data[data[f'{l[i]}'] == f"{inp[i]}"][data[f'{l[-1]}'] == "No"].count()[0]
    py *= daty/totaly
    pn *= datn/totaln
print(py*proby)
print(pn*probn)

if py*proby > pn*probn:
    print("Yes")
else:
    print("No")
