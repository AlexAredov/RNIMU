import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv
import numpy as np
import matplotlib.ticker as ticker
from sklearn.cluster import SpectralClustering
from sklearn.metrics import calinski_harabasz_score

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


model = SpectralClustering(n_clusters=6,gamma=0.01)
model.fit(data)
score = calinski_harabasz_score(data,model.labels_)
#SpectralClustering

data = list(zip(x,y))

pre_y = model.labels_

fig, ax = plt.subplots(figsize=(15, 6))
ax.set_xlabel(r'val', fontsize=14)
ax.set_ylabel(r'ID', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

for i in range(6):
    plt.scatter(np.array(data)[pre_y==i][:,0],np.array(data)[pre_y==i][:,1])
plt.show()