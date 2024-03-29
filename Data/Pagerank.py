import networkx as nx 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import operator 
import random as rd
graph=nx.gnp_random_graph(25,0.6,directed=True)
nx.draw(graph,with_labels=True,font_color='red',font_size=10,node_color='yellow')
plt.show()

count=graph.number_of_nodes()
print(list(graph.neighbors(1)))

rank_dict={}
x=rd.randint(0,25)
for j in range(0,25):
  rank_dict[j]=0
rank_dict[x]=rank_dict[x]+1
for i in range(600000):
  list_n=list(graph.neighbors(x))
  counter = 0
  for z in list_n:
    counter = counter + 1
  if(counter==0):
    x=rd.randint(0,25)
    rank_dict[x]=rank_dict[x]+1
  else:
    x=rd.choice(list_n)
    rank_dict[x]=rank_dict[x]+1

print("Random Walk Score Updated")

for j in range(0,25):
  rank_dict[j]=rank_dict[j]/600000

pagerank=nx.pagerank(graph)

pagerank_sorted=sorted(pagerank.items(),key=lambda v:(v[1],v[0]),reverse=True)

pagerank_sorted

rank_dict_sorted=sorted(rank_dict.items(),key=lambda
v:(v[1],v[0]),reverse=True)

rank_dict_sorted

print("The order generated by our implementation algorithm is\n")

for i in rank_dict_sorted:
  print(i[0],end="")
print("\n\nThe order generated by networkx library is\n")

for i in pagerank_sorted:
  print(i[0],end="")