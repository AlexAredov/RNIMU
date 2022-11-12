import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv
import matplotlib.ticker as ticker

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
            x.append(float(row[0]))
            y.append(float(row[9]))
            z.append(0)


data = list(zip(y,z))
print(data)

kmeans = KMeans(n_clusters=6)
kmeans.fit(data)

data = list(zip(x,y))

fig, ax = plt.subplots(figsize=(15, 6))
plt.scatter(x, y, c=kmeans.labels_)
ax.set_xlabel(r'Id', fontsize=14)
ax.set_ylabel(r'y', fontsize=14)
#ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))

#ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

#ax.grid(which='major',
#        color = 'gray',
#        linewidth = 0.5)

#ax.minorticks_on()
#ax.grid(which='minor',
#        color = 'gray',
#        linewidth = 0.5)

plt.show()