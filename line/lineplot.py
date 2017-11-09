import numpy as np
import matplotlib.pyplot as plt

with open('scalquery.dat') as file:
    scalquery = np.array([[float(digit) for digit in line.split()] for line in file])
print scalquery

plt.figure(figsize = (10, 5), dpi = 100)
plt.subplot(111)

shapes = ['v', '8', 's' , 'p', 'o','^']
label = ['HU', 'WG', 'YT', 'WT', 'LJ']

m, n = scalquery.shape[0], scalquery.shape[1]
x_axis = scalquery[0, :]
for i in range(1, m):
    y_axis = scalquery[i, :]
    s,l = shapes[i-1], label[i-1]
    plt.plot(x_axis, y_axis, marker = s , linestyle = '-', label = l)

plt.xlim(5, 25)
#plt.xticks(5, 25, 1)
plt.ylim(0, 10)
plt.tick_params(axis = 'both', which = 'major', labelsize = 10)
plt.xlabel('|Vq|- size of query graph')
plt.ylabel('Total enumeration time')
plt.title('Scalability with query graph size|Vq|')

plt.legend(loc = 'upper left', frameon = True)

plt.savefig('scaq.pdf', dpi = 100)
plt.show()

