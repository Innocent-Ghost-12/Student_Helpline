from math import dist
# p = [1,2,3,4,5,12,15]
# l = [[0,1,2,3,4,11,14],
#      [1,0,1,2,3,10,13],
#      [2,1,0,1,2,9,12],
#      [3,2,1,0,1,8,11],
#      [4,3,2,1,0,7,10],
#      [11,10,9,8,7,0,3],
#      [14,13,12,11,10,3,0]]


p = [[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]]
leng = len(p)
l = [[] for i in range(leng)]

for i in range(leng):
     for j in range(leng):
          l[i].append(dist(p[i],p[j]))

min=4
e=3
c=[0]*leng

for x in range(leng):
     for y in range(leng):
          if l[x][y]<=e:
               c[y]+=1

for i in range(len(c)):
     if c[i]>=min:
          print(f"{p[i]}: Core")
     elif 1 < c[i] < min:
          print(f"{p[i]}: Border")
     else:
          print(f"{p[i]}: Noise")
