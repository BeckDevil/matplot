import numpy as np
import matplotlib.pyplot as plt

labels = ['YT', 'WG', 'WT', 'LJ', 'OK', 'DB']
legends = ['QG1', 'QG3', 'QG5']
plt.figure(figsize = (12,6), dpi = 100)

plt.subplot(111)
with open('schdq1.dat') as file:
    dist = np.array([[float(digit) for digit in line.split()] for line in file])
print dist
n = dist.shape[0]
print n

plt.ylabel('relative speed up against static-distribution')
ind = np.arange(n-1)
width = 0.10

M1 = np.array(dist[:, 0])
print M1
M2 = np.array(dist[:, 1])
print M2
fig, ax = plt.subplots()
rects1 = ax.bar(ind, M1, width, color = 'r', label = 'dynamic over static')
rects2 = ax.bar(ind, M2, width, color = 'b', label = 'finer dynamic over static')

plt.show()
