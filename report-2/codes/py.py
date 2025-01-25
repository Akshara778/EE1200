import matplotlib.pyplot as plt
import math

#function to plot the voltage across capacitor as a function of time in the RC circuit
def rc(r, c, phase, amplitude, w, h, n):
    t_coord = []
    v_coord = []
    t = 0
    v = 0
    for i in range(n):
        t_coord.append(t)
        v_coord.append(v)
        temp = math.sin((w * t) + phase)
        if(temp > 0):
            temp = amplitude
        else:
            temp = 0
        #difference equation is v(n+1) = v(n) + h(V_in - v(n))/RC
        v = v + (h * ((temp - v)/float(r * c)))
        t += h
    return [t_coord, v_coord]

#first case is where RC = T, where T is the time period of the input wave
coord = rc(10, 0.1, 0, 5, 2 * math.pi, 0.0003, 100000)
plt.figure()
plt.plot(coord[0][:], coord[1][:])
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-2,35)
plt.ylim(-2,8)
plt.grid(True)
plt.savefig("../figs/fig1.png")

#second case is where RC >> T
coord = rc(10, 0.1, 0, 5, 200 * math.pi, 0.0001, 250000)
plt.figure()
plt.plot(coord[0][:], coord[1][:])
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-2,27)
plt.ylim(-2,6)
plt.grid(True)
plt.savefig("../figs/fig2.png")

#third case is where RC << T
coord = rc(10, 0.1, 0, 5, 0.02 * math.pi, 0.01, 100000)
plt.figure()
plt.plot(coord[0][:], coord[1][:])
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-20,1000)
plt.ylim(-2,8)
plt.grid(True)
plt.savefig("../figs/fig3.png")
