import numpy as np
import matplotlib.pyplot as plt

with open('nte_effect.dat') as file:
    nte_eff = np.array([[float(digit) for digit in line.split()] for line in file])
print nte_eff

labels = ['YT', 'WG', 'WT', 'LJ', 'OK', 'DB']
legends = ['QG1', 'QG2', 'QG3', 'QG4','QG5']

plt.figure(figsize = (12, 4), dpi = 100)
#plt.tick_params(axis='both', which='major', labelsize=8)
#plt.tick_params(axis='both', which='minor', labelsize=6)
plt.ylabel('speedup with nte-index')

for i in range (0,5):
    plt.subplot(1,5, i+1)
    if (i == 0):
        plt.ylabel('speedup with nte-index')
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.tick_params(axis='both', which='minor', labelsize=6)
    y_pos = np.arange(len(labels))
    data = nte_eff[i, :]
    plt.bar(y_pos, data, align = 'center', alpha = 0.5)
    plt.xticks(y_pos, labels)
    plt.ylim(0, 3)
    plt.title(legends[i])

plt.savefig('nte_effect.pdf', dpi = 100)
plt.show()



