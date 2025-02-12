import matplotlib.pyplot as plt
import numpy as np

def bode_magnitude(start_w, r, c, h, n):
    w = start_w
    h_coord = []
    w_coord = []
    for i in range(n):
        w_coord.append(np.log10(w))
        h_coord.append(-20*np.log10(np.sqrt(1 +( w * r * c)**2 )))
        w += h
    return [w_coord, h_coord]

def bode_phase(start_w, r, c, h, n):
    w = start_w
    h_coord = []
    w_coord = []
    for i in range(n):
        w_coord.append(np.log10(w))
        h_coord.append(-np.arctan(w * c * r))
        w += h
    return [w_coord, h_coord]

coord_magnitude = bode_magnitude(100*np.pi, 100, 0.00000008, 0.5, 1000000)
coord_phase = bode_phase(100 * np.pi, 100, 0.00000008, 10, 1000000)


# Given data
frequencies = np.array([50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200])
H_values = np.array([0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.94, 0.88, 0.77, 0.55, 0.34])
delta_x = np.array([0, 0, 0, 0, 0, 3, 4, 8, 6.4 ,5.6, 3.6])
phase = -(2*np.pi)*frequencies*delta_x*(10**(-6))
'''phase = []
for i in range (0, 11):
    phase.append(-2000000*(2*np.pi)*frequencies[i]*delta_x[i])'''

# Calculate w (2*pi*f)
w_values = 2 * np.pi * frequencies
w_value= np.log10(w_values)
# Calculate log(H(jw)) - assuming it's log base 10
log_H_values = 20*np.log10(H_values)

plt.figure()
plt.scatter(w_value, log_H_values)
plt.plot(coord_magnitude[0][:], coord_magnitude[1][:])
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig("../figs/fig1.png")


plt.figure()
plt.scatter(w_value, phase)
plt.plot(coord_phase[0][:], coord_phase[1][:])
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
#plt.ylim(-2, 1)
plt.savefig("../figs/fig2.png")
plt.show()


