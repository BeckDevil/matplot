"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""
import numpy as np
import matplotlib.pyplot as plt
fig, (ax1, ax2, ax3) = plt.subplots(1,3, sharex = True, sharey = False, figsize = (12,6))

#read file with numbers
with open('schdq1.dat') as file:
    scalnode = np.array([[float(digit) for digit in line.split()] for line in file])
print scalnode

N = scalnode.shape[1]

M1      = scalnode[0, 0:N]#(20, 35, 30, 35, 27)
M2      = scalnode[1, 0:N]#(20, 35, 30, 35, 27)

ind = np.arange(N)  # the x locations for the groups
width = 0.30       # the width of the bars

rects1 = ax1.bar(ind, M1, width, color='g', label = 'dynamic')
rects2 = ax1.bar(ind + 1*width, M2, width, color='r', label = 'fine-grained dynamic')

# add some text for labels, title and axes ticks
ax1.set_ylabel('speedup against static-distribution')
ax1.set_title('QG1')
ax1.set_xticks(ind + 1 * width)
ax1.set_ylim(0, 70)
ax1.set_xticklabels(('WG', 'YT', 'WT', 'LJ', 'OK', 'DB'))

ax1.legend((rects1[0], rects2[0]), ('dynamic', 'fine-grained dynamic'))
ax1.legend(loc = 'upper left',frameon = True, prop = {'size':10})

#read file with numbers
with open('schdq3.dat') as file:
    scalnode = np.array([[float(digit) for digit in line.split()] for line in file])
print scalnode

N = scalnode.shape[1]

M1      = scalnode[0, 0:N]#(20, 35, 30, 35, 27)
M2      = scalnode[1, 0:N]#(20, 35, 30, 35, 27)

ind = np.arange(N)  # the x locations for the groups
width = 0.30       # the width of the bars

rects1 = ax2.bar(ind, M1, width, color='g', label = 'dynamic')
rects2 = ax2.bar(ind + 1*width, M2, width, color='r', label = 'fine-grained dynamic')

# add some text for labels, title and axes ticks
#ax2.set_ylabel('speedup against static-distribution')
ax2.set_title('QG3')
ax2.set_xticks(ind + 1 * width)
ax2.set_ylim(0, 70)
ax2.set_xticklabels(('WG', 'YT', 'WT', 'LJ', 'OK', 'DB'))

ax2.legend((rects1[0], rects2[0]), ('dynamic', 'fine-grained dynamic'))
ax2.legend(loc = 'upper left',frameon = True, prop = {'size':10})

#read file with numbers
with open('schdq5.dat') as file:
    scalnode = np.array([[float(digit) for digit in line.split()] for line in file])
print scalnode

N = scalnode.shape[1]

M1      = scalnode[0, 0:N]#(20, 35, 30, 35, 27)
M2      = scalnode[1, 0:N]#(20, 35, 30, 35, 27)

ind = np.arange(N)  # the x locations for the groups
width = 0.30       # the width of the bars

rects1 = ax3.bar(ind, M1, width, color='g', label = 'dynamic')
rects2 = ax3.bar(ind + 1*width, M2, width, color='r', label = 'fine-grained dynamic')

# add some text for labels, title and axes ticks
#ax3.set_ylabel('speedup against static-distribution')
ax3.set_title('QG5')
ax3.set_xticks(ind + 1 * width)
ax3.set_ylim(0, 70)
ax3.set_xticklabels(('WG', 'YT', 'WT', 'LJ', 'OK', 'DB'))

ax3.legend((rects1[0], rects2[0]), ('dynamic', 'fine-grained dynamic'))
ax3.legend(loc = 'upper left',frameon = True, prop = {'size':10})

plt.savefig("nte_eff.pdf", dpi = 144);
plt.show()
