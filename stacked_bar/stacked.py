import numpy as np
import matplotlib.pyplot as plt

with open('stages.dat') as file:
    stages = np.array([[float(digit) for digit in line.split()] for line in file])
print stages

stage1 = stages[:, 0]
stage2 = stages[:, 1]

N = stages.shape[0]
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind+0.35, stage1, width, color='r')
p2 = plt.bar(ind+0.35, stage2, width, bottom=stage1, color = 'b' )

plt.ylabel('Scores')
plt.title('Portions of time spent on different section')
plt.xticks(ind, ('QG1', 'QG2', 'QG3', 'QG4', 'QG5'))
plt.ylim(0.8, 1)
plt.yticks(np.arange(0.8, 1, 0.02))
plt.legend((p1[0], p2[0]), ('LWEI creation', 'Embedding enumeration'), loc = 'lower right')

plt.show()
