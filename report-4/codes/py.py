import matplotlib.pyplot as plt
import math


#function to plot the voltage across capacitor as a function of time in the LC circuit
def lc(r, l, C, h, n):
    t_coord = []
    v_coord = []
    t = 0
    v = 0
    d = (r/l)**2 - (4/(l * C))
    c = -r/l
    b = -2.5 * d
    for i in range(n):
        t_coord.append(t)
        v_coord.append(v)
        v = 2 * b * math.exp(c * t) * math.sin(d * t)
        t += h
    return [t_coord, v_coord]

#first case is where RC = T, where T is the time period of the input wave
coord = lc(1, 0.0022, 500e-12, 0.0001, 100000)
plt.figure()
plt.plot(coord[0][:], coord[1][:])
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-5, 5)
plt.grid(True)
plt.savefig("../figs/fig1.png")

plt.show()
