import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

def moving_average(interval, windowsize):
    window = np.ones(int(windowsize)) / float(windowsize)
    re = np.convolve(interval, window, 'same')
    return re

file = open('./1.txt')
x = []
y = []

for i in file:
    x.append(float(i.split('\t')[0].replace('\n', '').replace(',', '.')))
    y.append(float(i.split('\t')[1].replace('\n', '').replace(',', '.')))

#y_av = moving_average(y, 200)

y_av = []

for i in range(len(y)-1):
    y_av.append((y[i]+y[i+1])/2)

x_av = []

for i in range(len(x)-1):
    x_av.append((x[i]+x[i+1])/2)

plt.plot(x_av,y_av)

plt.plot(x,y)


plt.show()