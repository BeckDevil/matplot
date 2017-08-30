"""
========================================================
Building histograms using Rectangles and PolyCollections
========================================================

This example shows how to use a path patch to draw a bunch of
rectangles.  The technique of using lots of Rectangle instances, or
the faster method of using PolyCollections, were implemented before we
had proper paths with moveto/lineto, closepoly etc in mpl.  Now that
we have them, we can draw collections of regularly shaped objects with
homogeneous properties more efficiently with a PathCollection.  This
example makes a histogram -- its more work to set up the vertex arrays
at the outset, but it should be much faster for large numbers of
objects
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

with open('deg_dist.txt') as file:
    scalnode = np.array([[float(digit) for digit in line.split()] for line in file])
#print scalnode

plt.figure(figsize = (8,6), dpi = 100)
plt.subplot(111)

# histogram our data with numpy
data = scalnode[:, 0]
bins = 10 ** np.linspace(0, 19, 20)
#print bins

plt.hist(data, bins = bins)

plt.xscale('log')
plt.xlim(bins[0]/10, bins[19]*10)
plt.xlabel('Cardinality of cluster')


plt.ylim(0, 1000000)
plt.ylabel('Frequency')

plt.title('Frequency Distribution of cardinality on each cluster');

plt.savefig('card_dist.pdf', dpi = 144)
plt.show()
