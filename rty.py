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

with open('./titanic.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row[0])
        if is_number(row[1]) and is_number(row[2]):
            x.append(float(row[9]))
            y.append(float(row[0]))


data = list(zip(x,y))
print(data) 
inertias = []

kmeans = KMeans(n_clusters=6)
kmeans.fit(data)

fig, ax = plt.subplots(figsize=(90, 6))
plt.scatter(x, y, c=kmeans.labels_)
ax.set_xlabel(r'x', fontsize=14)
ax.set_ylabel(r'y', fontsize=14)
#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

ax.grid(which='major',
        color = 'gray',
        linewidth = 0.5)

ax.minorticks_on()
ax.grid(which='minor',
        color = 'gray',
        linewidth = 0.1)

plt.show()