"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""
import numpy as np
import matplotlib.pyplot as plt

#read file with numbers
with open('scaldeg.dat') as file:
    scalnode = np.array([[float(digit) for digit in line.split()] for line in file])
print scalnode

N = scalnode.shape[1]

M1      = scalnode[0, 1:N]#(20, 35, 30, 35, 27)
M2      = scalnode[1, 1:N]#(20, 35, 30, 35, 27)
M4      = scalnode[2, 1:N]#(20, 35, 30, 35, 27)
M8      = scalnode[3, 1:N]#(20, 35, 30, 35, 27)
M16     = scalnode[4, 1:N]#(20, 35, 30, 35, 27)
M32     = scalnode[5, 1:N]#(20, 35, 30, 35, 27)
M64     = scalnode[6, 1:N]#(20, 35, 30, 35, 27)
M128    = scalnode[7, 1:N]#(20, 35, 30, 35, 27)


ind = np.arange(N-1)  # the x locations for the groups
width = 0.10       # the width of the bars

fig, ax = plt.subplots(figsize = (8,6), dpi = 100)
rects1 = ax.bar(ind, M1, width, color='g', label = '2')
rects2 = ax.bar(ind + 1*width, M2, width, color='r', label = '4')
rects3 = ax.bar(ind + 2*width, M4, width, color='c', label = '6')
rects4 = ax.bar(ind + 3*width, M8, width, color='m', label = '8')
rects5 = ax.bar(ind + 4*width, M16, width, color='y', label = '10')
rects6 = ax.bar(ind + 5*width, M32, width, color='k', label = '12')
rects7 = ax.bar(ind + 6*width, M64, width, color='w', label = '14')
rects8 = ax.bar(ind + 7*width, M128, width, color='b', label = '16')

# add some text for labels, title and axes ticks
ax.set_ylabel('relative increase in runtime')
ax.set_title('Scalability with increasing average degree')
ax.set_xticks(ind + 4 * width)
ax.set_xticklabels(('QG1', 'QG2', 'QG3', 'QG4', 'QG5'))

ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], rects6[0], rects7[0], rects8[0]), ('2', '4', '6', '8', '10', '12', '14', '16'))
ax.legend(loc = 'upper left',frameon = True, prop = {'size':6})
'''
#read file with numbers
with open('scaldeg.dat') as file:
    scaldeg = np.array([[float(digit) for digit in line.split()] for line in file])
print scaldeg

N = scaldeg.shape[1]

M1      = scaldeg[0, 1:N]#(20, 35, 30, 35, 27)
M2      = scaldeg[1, 1:N]#(20, 35, 30, 35, 27)
M4      = scaldeg[2, 1:N]#(20, 35, 30, 35, 27)
M8      = scaldeg[3, 1:N]#(20, 35, 30, 35, 27)
M16     = scaldeg[4, 1:N]#(20, 35, 30, 35, 27)
M32     = scaldeg[5, 1:N]#(20, 35, 30, 35, 27)
M64     = scaldeg[6, 1:N]#(20, 35, 30, 35, 27)
M128    = scaldeg[7, 1:N]#(20, 35, 30, 35, 27)


ind = np.arange(N-1)  # the x locations for the groups
width = 0.10       # the width of the bars

fig, ax = plt.subplots(122, figsize = (8,6), dpi = 100)
rects1 = ax.bar(ind, M1, width, color='b', label = '1M')
rects2 = ax.bar(ind + 1*width, M2, width, color='g', label = '2M')
rects3 = ax.bar(ind + 2*width, M4, width, color='r', label = '4M')
rects4 = ax.bar(ind + 3*width, M8, width, color='c', label = '8M')
rects5 = ax.bar(ind + 4*width, M16, width, color='m', label = '16M')
rects6 = ax.bar(ind + 5*width, M32, width, color='y', label = '32M')
rects7 = ax.bar(ind + 6*width, M64, width, color='k', label = '64M')
rects8 = ax.bar(ind + 7*width, M128, width, color='w', label = '128M')

# add some text for labels, title and axes ticks
ax.set_ylabel('relative increase in runtime')
ax.set_title('Scalability with increasing graph size')
ax.set_xticks(ind + 4.5 * width)
ax.set_xticklabels(('QG1', 'QG2', 'QG3', 'QG4', 'QG5'))

ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], rects6[0], rects7[0], rects8[0]), ('1M', '2M', '4M', '8M', '16M', '32M', '64M', '128M', '256M'))
ax.legend(loc = 'upper left',frameon = True, prop = {'size':6})
'''
'''def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%d' % int(height),ha='center', va='bottom')
   '     
autolabel(rects1)
autolabel(rects2)
'''
plt.savefig("scaldeg.pdf", dpi = 144);
plt.show()
