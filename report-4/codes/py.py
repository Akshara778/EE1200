import numpy as np
import matplotlib.pyplot as plt
import math

# Values of R, L, C 
R = 55 # ohm
L = 2.2e-3 # henry
C = 4600e-12 # farad

h = 1e-9 # stepsize
tmax = 2e-4 # max time 

size = int(tmax/h)

z = R * np.sqrt(C/L) /2
w_n = 1/np.sqrt(L*C) 
w_d = w_n*np.sqrt(1 - (z * z))

Vc0 = 5

t = np.linspace(0, tmax, size)

Vc = Vc0 * (np.exp(-z*w_n*t)) * (np.cos(w_d*t) + ((w_n*z/w_d)*np.sin(w_d*t)) )

plt.grid(True)
plt.plot(t, Vc)
plt.savefig("../figs/fig2.png")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (Vc)")
plt.show()
