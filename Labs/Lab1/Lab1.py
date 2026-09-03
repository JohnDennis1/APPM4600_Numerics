import numpy as np
import matplotlib.pyplot as plt
w = 10**(-np.linspace(1,10,10))
x = np.linspace(1,len(w),len(w))
s = 3*w


plt.semilogy(x,w)
plt.semilogy(x,s)
plt.title("Lab 1 graph")
plt.xlabel("x")
plt.ylabel("Semilogy")
plt.savefig("Lab1_figure1.jpg")
plt.show()