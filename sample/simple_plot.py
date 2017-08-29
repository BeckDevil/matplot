import numpy as np
import matplotlib.pyplot as plt

#create figure with 8x6 points, 100 dots per inch
plt.figure(figsize = (8,6), dpi = 100)

#create new subplot from a grid of 1x1
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256, endpoint = True)
C,S = np.cos(X), np.sin(X)

#Plot cosine with blue color line of width 1
plt.plot(X,C, color = "blue", linewidth = 1.0, linestyle = "-", label = "cosine")

#Plot cosine with blue color line of width 1
plt.plot(X,S, color = "red", linewidth = 1.0, linestyle = "-", label = "sine")

plt.legend(loc = 'upper left', frameon = True)
#set x limits
#plt.xlim(-4.0, 4.0)
plt.xlim(X.min()*1.1, X.max()*1.1);

#set xtics
#plt.xticks(np.linspace(-4, 4, 9, endpoint = True))
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], 
        [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

#set y limits
#plt.ylim(-1.0, 1.0)
plt.ylim(C.min()*1.1, C.max()*1.1)

#set ytics
#plt.yticks(np.linspace(-1, 1, 5, endpoint = True))
plt.yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$+1$'])

#save figure using 72 dots per inch
plt.savefig("sine.pdf", dpi = 72)

plt.show()
