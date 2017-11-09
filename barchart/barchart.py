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
plt.tick_params(axis = 'both', which = 'major', labelsize = 12)
plt.tick_params(axis = 'both', which = 'minor', labelsize = 12)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12,6), dpi = 100)
rects1 = ax1.bar(ind, M1, width, bottom = -100, color='g', label = '2', hatch='//')
rects2 = ax1.bar(ind + 1*width, M2, width, bottom = -100, color='r', label = '4', hatch='//')
rects3 = ax1.bar(ind + 2*width, M4, width, bottom = -100, color='c', label = '6', hatch='//')
rects4 = ax1.bar(ind + 3*width, M8, width, bottom = -100, color='m', label = '8', hatch='//')
rects5 = ax1.bar(ind + 4*width, M16, width, bottom = -100, color='y', label = '10', hatch='//')
rects6 = ax1.bar(ind + 5*width, M32, width, bottom = -100, color='k', label = '12', hatch='//')
rects7 = ax1.bar(ind + 6*width, M64, width, bottom = -100, color='w', label = '14', hatch='//')
rects8 = ax1.bar(ind + 7*width, M128, width, bottom = -100, color='b', label = '16', hatch='//')

# add some text for labels, title and axes ticks
ax1.set_ylabel('relative increase in runtime',fontsize = 18 )
ax1.set_ylim(-100, 500)
ax1.set_title('Scalability on avg degree', fontsize = 18)
ax1.set_xticks(ind + 4 * width)
ax1.set_xticklabels(('QG1', 'QG2', 'QG3', 'QG4', 'QG5'))

ax1.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], rects6[0], rects7[0], rects8[0]), ('2', '4', '6', '8', '10', '12', '14', '16'))
ax1.legend(loc = 'upper left',frameon = True, prop = {'size':10})

with open('scalnode.dat') as file:
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


rects1 = ax2.bar(ind, M1, width, color='b', label = '1M')
rects2 = ax2.bar(ind + 1*width, M2, width, color='g', label = '2M')
rects3 = ax2.bar(ind + 2*width, M4, width, color='r', label = '4M')
rects4 = ax2.bar(ind + 3*width, M8, width, color='c', label = '8M')
rects5 = ax2.bar(ind + 4*width, M16, width, color='m', label = '16M')
rects6 = ax2.bar(ind + 5*width, M32, width, color='y', label = '32M')
rects7 = ax2.bar(ind + 6*width, M64, width, color='k', label = '64M')
rects8 = ax2.bar(ind + 7*width, M128, width, color='w', label = '128M')

# add some text for labels, title and axes ticks
ax2.set_ylim(-100, 2500)
ax2.set_title('Scalability with |Vg|', fontsize = 18)
ax2.set_xticks(ind + 4.5 * width)
ax2.set_xticklabels(('QG1', 'QG2', 'QG3', 'QG4', 'QG5'))

ax2.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], rects6[0], rects7[0], rects8[0]), ('1M', '2M', '4M', '8M', '16M', '32M', '64M', '128M', '256M'))
ax2.legend(loc = 'upper left',frameon = True, prop = {'size':10})

plt.savefig("scaldeg.pdf", dpi = 144);
plt.show()
