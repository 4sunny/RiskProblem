import numpy
import matplotlib.pylab as plt
'''
m = [[41.6, 25.4, 17.4, 12.6, 9.49, 7.33, 5.76, 4.59, 3.7, 3.0],
[57.9, 38.9, 25.3, 17.7, 12.9, 9.78, 7.6, 6.01, 4.81, 3.88],
[66.0, 54.0, 36.9, 25.0, 17.8, 13.2, 10.0, 7.83, 6.22, 5.0],
[70.7, 62.5, 50.9, 35.2, 24.7, 17.8, 13.3, 10.3, 8.03, 6.38],
[73.9, 67.8, 59.6, 48.2, 33.8, 24.2, 17.8, 13.5, 10.4, 8.19],
[76.1, 71.4, 65.3, 57.0, 46.0, 32.6, 23.9, 17.7, 13.5, 10.5],
[77.6, 73.9, 69.2, 62.9, 54.8, 44.0, 31.5, 23.5, 17.7, 13.6],
[78.7, 75.8, 72.0, 67.1, 60.9, 52.8, 42.3, 30.6, 23.1, 17.6],
[79.6, 77.2, 74.1, 70.2, 65.3, 59.0, 50.9, 40.7, 29.7, 22.7],
[80.4, 78.3, 75.7, 72.6, 68.6, 63.6, 57.3, 49.2, 39.3, 29.0]]'''
m = [[58.4, 42.1, 34.0, 29.3, 26.1, 24.0, 22.5, 21.3, 20.4, 19.6], [74.6, 44.8, 29.3, 20.9, 16.0, 12.8, 10.6, 9.09, 7.93, 7.03], [82.6, 62.0, 38.3, 24.0, 16.1, 11.4, 8.53, 6.59, 5.24, 4.28], [87.4, 72.2, 54.4, 34.5, 21.3, 13.6, 9.23, 6.52, 4.8, 3.63], [90.5, 79.0, 65.3, 49.4, 32.1, 19.7, 12.2, 7.98, 5.45, 3.83], [92.7, 83.7, 73.0, 60.4, 45.8, 30.3, 18.7, 11.4, 7.26, 4.78], [94.2, 87.1, 78.5, 68.3, 56.6, 43.1, 29.1, 18.0, 11.0, 6.77], [95.4, 89.7, 82.7, 74.4, 64.7, 53.5, 41.0, 28.1, 17.6, 10.6], [96.3, 91.6, 85.9, 79.0, 71.0, 61.7, 51.1, 39.3, 27.2, 17.3], [97.0, 93.2, 88.4, 82.7, 75.9, 68.1, 59.2, 49.1, 37.9, 26.6]]

matrix = numpy.array(m)

plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)
ax.set_aspect('equal')
plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.cool, extent=(0.5, 10.5, 10.5, 0.5))
plt.colorbar()
plt.xticks(numpy.arange(1,11))
plt.yticks(numpy.arange(1,11))
plt.clim(100,0)
ax.xaxis.set_label_position('top')
plt.title('Likelihood of Attacker Taking Territory in a Risk Dice Battle')
plt.ylabel('Attacker Dice Count')
plt.xlabel('Defender Dice Count')
for i in range(10):
    for j in range(10):
        plt.text(j + 1, i + 1, str(matrix[i][j]) + "%", va='center', ha='center')
plt.savefig('mygraph.png')
plt.show()

