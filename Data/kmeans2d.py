from math import sqrt

def dist(l, m1, m2):
    dm1=[]
    dm2=[]
    for i in range(len(l)):
        dis = sqrt((l[i][0]-m1[0])**2 + (l[i][1]-m1[1])**2)
        dm1.append(dis)
    for i in range(len(l)):
        dis = sqrt((l[i][0]-m2[0])**2 + (l[i][1]-m2[1])**2)
        dm2.append(dis)
    return dm1,dm2

d = {
    0: {
        'p': 'A',
        'c': [1,1]
    },
    1: {
        'p': 'B',
        'c': [1,0]
    },
    2: {
        'p': 'C',
        'c': [0,2]
    },
    3: {
        'p': 'D',
        'c': [2,4]
    },
    4: {
        'p': 'E',
        'c': [3,5]
    },
}

l = [[1,1],[1,0],[0,2],[2,4],[3,5]]
m1 = [1,1]
m2 = [1,0]
c1=[]
c2=[]
p1=[]
p2=[]
c=0

for j in range(10):
    dm1, dm2 = dist(l, m1, m2)
    for i in range(5):
        if dm1[i] < dm2[i]:
            c1.append(l[i])
        else:
            c2.append(l[i])
    nm1 = m1
    nm2 = m2
    m1 = [sum(x)/len(x) for x in zip(*c1)]
    m2 = [sum(x)/len(x) for x in zip(*c2)]

    if m1==nm1 and m2==nm2:
        print("Iterations: ",c)
        break
    c1.clear()
    c2.clear()
    c+=1

for k, v in d.items():
    if v['c'] in c1:
        p1.append(d[k]['p'])
    else:
        p2.append(d[k]['p'])

print(p1,c1)
print(p2,c2)
