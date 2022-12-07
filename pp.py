import matplotlib.pyplot as plt
import numpy as np

    # формированиe numpy-массива из форматированного текстового файла
data = np.genfromtxt('./1.txt', delimiter='\t', dtype=[('time', '<f8'), ('temp', '<f8')])
    # отображение в виде графика исходного набор экспериментальных точек отобража-ется в виде графика.
plt.plot(data['time'], data['temp'], 'o', markersize=3)

win = 100
filt = np.ones(win)/win
mov = win//2
win = 16
filt = np.ones(win)/win
mov = win//2
res = np.convolve(data['temp'], filt, mode='same')
plt.plot(data['time'][mov:-mov], res[mov:-mov], 'b')
res = np.convolve(data['temp'], filt, mode='same')
plt.plot(data['time'][mov:-mov], res[mov:-mov], 'r')

plt.show()
