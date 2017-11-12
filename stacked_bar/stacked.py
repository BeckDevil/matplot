import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize = (6,2), dpi = 144)
with open('stages.dat') as file:
    stages = np.array([[float(digit) for digit in line.split()] for line in file])
print stages
plt.gcf().subplots_adjust(bottom=0.15)
plt.rcParams.update({'font.size': 16})
stage1 = stages[:, 0]
stage2 = stages[:, 1]

N = stages.shape[0]
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind+0.35, stage1, width, color='gray')
p2 = plt.bar(ind+0.35, stage2, width, bottom=stage1, color = 'gainsboro' )

plt.ylabel('Percentage (%)')
#plt.title('Percentages of time spent on different section')
plt.xticks(ind+0.5, ('WG', 'YT', 'WT', 'LJ', 'OK', 'FR'))

plt.ylim(0, 100)
plt.yticks(np.arange(0, 101, 20))

ax = plt.gca()
yticks = ax.yaxis.get_major_ticks()
#for i in range(2,9):
#    yticks[i].label1.set_visible(False)
#yticks[-1].label1.set_visible(False)

plt.legend(( p2[0], p1[0]), ('CECI creation','Circle completion'), loc = 'upper right')

plt.savefig('stages.pdf', dpi = 144)
plt.show()
