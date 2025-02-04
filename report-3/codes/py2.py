import matplotlib.pyplot as plt
import numpy as np

def bode_magnitude(start_w, r, c, h, n):
    w = start_w
    h_coord = []
    w_coord = []
    for i in range(n):
        w_coord.append(np.log(w))
        h_coord.append(-np.log(np.sqrt((1 - (w * r * c)**2)**2 + (3 * w * r * c)**2)))
        w += h
    return [w_coord, h_coord]

def bode_phase(start_w, r, c, h, n):
    w = start_w
    h_coord = []
    w_coord = []
    for i in range(n):
        w_coord.append(np.log(w))
        h_coord.append(-np.arctan((3 * w * r * c)/(1 - (w * r * c)**2)))
        w += h
    return [w_coord, h_coord]

coord_magnitude = bode_magnitude(0.001, 0.1, 10, 0.001, 100000)
coord_phase = bode_phase(0.001, 0.1, 10, 0.001, 100000)

plt.figure()
plt.plot(coord_magnitude[0][:], coord_magnitude[1][:])
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig("../figs/fig3.png")

plt.figure()
plt.plot(coord_phase[0][:], coord_phase[1][:])
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig("../figs/fig4.png")
plt.show()
