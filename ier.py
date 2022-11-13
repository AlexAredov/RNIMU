import matplotlib.pyplot as plt
import csv
import numpy as np
import matplotlib.ticker as ticker
from sklearn.cluster import AgglomerativeClustering


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

x = []
y = []
z = []

with open('./titanic.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row[0])
        if is_number(row[1]) and is_number(row[2]):
            x.append(float(row[9]))
            y.append(float(row[0]))
            z.append(0)


data = list(zip(x,z))
#print(data)

cluster = AgglomerativeClustering(n_clusters=6, affinity='euclidean', linkage='ward')
cluster.fit_predict(data)

data = list(zip(x,y))

fig, ax = plt.subplots(figsize=(15, 6))
plt.scatter(np.array(data)[:,0],np.array(data)[:,1], c=cluster.labels_, cmap='rainbow')
ax.set_xlabel(r'val', fontsize=14)
ax.set_ylabel(r'ID', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.show()