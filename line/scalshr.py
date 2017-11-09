import numpy as np
import matplotlib.pyplot as plt

with open('scalshrd1.dat') as file:
    scalquery = np.array([[float(digit) for digit in line.split()] for line in file])
print scalquery

plt.figure(figsize = (12, 5), dpi = 100)
plt.subplot(121)

shapes = ['o', 'x', '^' , 'v', 's','8']
label = ['WG', 'YT', 'WT', 'LJ', 'OK']

m, n = scalquery.shape[0], scalquery.shape[1]
x_axis = scalquery[0, :]
for i in range(1, m):
    y_axis = scalquery[i, :]
    s,l = shapes[i-1], label[i-1]
    plt.plot(x_axis, y_axis, marker = s , linestyle = '-', label = l)

plt.xlim(0, 70)
plt.ylim(0, 45)
plt.xlabel('# of workers')
plt.ylabel('relative increase in total time')
plt.title('Scalability on QG1')
plt.legend(loc = 'upper left', frameon = True, prop = {'size':12})
#plt.show()

with open('scalshrd4.dat') as file:
    scalquery = np.array([[float(digit) for digit in line.split()] for line in file])
print scalquery

plt.subplot(122)

shapes = ['o', 'x', '^' , 'v', 's','8']
label = ['WG', 'YT', 'WT', 'LJ', 'OK']

m, n = scalquery.shape[0], scalquery.shape[1]
x_axis = scalquery[0, :]
for i in range(1, m):
    y_axis = scalquery[i, :]
    s,l = shapes[i-1], label[i-1]
    plt.plot(x_axis, y_axis, marker = s , linestyle = '-', label = l)

plt.xlim(0, 70)
plt.ylim(0, 45)
plt.xlabel('# of workers')
plt.ylabel('relative increase in total time')
plt.title('Scalability on QG3')
plt.legend(loc = 'upper left', frameon = True, prop = {'size':12})

plt.savefig('scaws.pdf', dpi = 144)
plt.show()

