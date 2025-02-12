import matplotlib.pyplot as plt
import numpy as np

def bode_magnitude(start_w, r, c, h, n):
    w = start_w
    h_coord = []
    w_coord = []
    for i in range(n):
        w_coord.append(np.log10(w))
        h_coord.append(-np.log10(np.sqrt((1 - 5 * (w * r * c)**2)**2 + (6 * w * r * c - (w * r * c)**3))))
        w += h
    return [w_coord, h_coord]

def bode_phase(start_w, r, c, h, n):
    w = start_w
    h_coord = []
    w_coord = []
    for i in range(n):
        w_coord.append(np.log10(w))
        h_coord.append(-np.arctan((6 * w * r * c - (w * r * c)**3)/(1 - 5 * (w * r * c)**2)))
        w += h
    return [w_coord, h_coord]

coord_magnitude = bode_magnitude(100*np.pi, 100, 0.00000008, 0.05, 1000000)
coord_phase = bode_phase(100*np.pi, 100, 0.00000008, 10, 1000000)

# Given data
frequencies = np.array([50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200])
H_values = np.array([0.9615, 0.96, 0.96, 0.96, 0.96, 0.92, 0.833, 0.651, 0.409, 0.203, 0.03])
delta_x = np.array([-19.8, -9.85, -5, -2.47, -1.22, -0.57, -0.282, -0.130, -0.053, -0.025, -0.0105])
phase = -np.arctan(np.tan((2*np.pi*frequencies)*delta_x * 0.001))

# Calculate w (2*pi*f)
w_values = 2 * np.pi * frequencies
w_value= np.log10(w_values)
# Calculate log(H(jw)) - assuming it's log base 10
log_H_values = np.log10(H_values)

# Now you can use w_values and log_H_values as numpy arrays



plt.figure()
plt.scatter(w_value, log_H_values)
plt.plot(coord_magnitude[0][:], coord_magnitude[1][:])
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
#plt.show()
plt.savefig("../figs/fig5.png")


plt.figure()
plt.scatter(w_value, phase)
plt.plot(coord_phase[0][:], coord_phase[1][:])
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig("../figs/fig6.png")
#plt.show()


