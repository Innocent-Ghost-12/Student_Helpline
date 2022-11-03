import math

def distn(l,k,m):
    dl=[[] for x in range(k)]
    for i in range(k):
        for j in range(len(l)):
            dis = math.dist(m[i],l[j])
            dl[i].append(dis)
    return dl


# k = int(input("Enter number of clusters: "))
k=5
nm = 0
d = [[185,70],[170,56],[168,60],[179,68],[182,72],[188,77],[180,71],[183,84],[180,88],[180,67],[172,70]]
m = [d[i] for i in range(k)]
c = [[] for x in range(k)]


while nm != m:
    dis = distn(d, k, m)
    c = [[] for x in range(k)]
    for i in range(11):
        minl=min(dis,key=lambda x:x[i])
        ind = dis.index(minl)
        c[ind].append(d[i])
    nm = m
    for j in range(k):
        m1 = [sum(x) / len(x) for x in zip(*c[j])]
        m.append(m1)
    if nm == m:
        break
for i in range(len(c)):
    print("Cluster",i+1," -",c[i])
