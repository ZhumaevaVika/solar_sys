from matplotlib import pyplot as plt
import numpy as np


betta0 = np.array([0.7875, 0.767, 0.769, 1.454, 1.381, 1.436, 0.4940, 0.4945, 0.4986, 1.639, 1.667, 1.643])
betta0arr = betta0.reshape(4, 3)
betta0y = np.array([np.sum(i)/3 for i in betta0arr])
betta0y = 0.010305637/betta0y
pogrbettastat = np.array([(betta0[i] - betta0y[i // 3])**2 for i in range(12)])
pogrbettastat = pogrbettastat.reshape(4, 3)
pogrbettastat = np.array([(np.sum(i)/3)**0.5 for i in pogrbettastat])

pogrbetta0 = np.array([0.0037, 0.0054, 0.0054, 0.0094, 0.0072, 0.011, 0.0016, 0.00051, 0.0016, 0.0088, 0.011, 0.010])
pogrbetta0arr = pogrbetta0.reshape(4, 3)
pogrbettax = np.array([(np.sum(i**2)/3)**0.5 for i in pogrbetta0arr])

mR2 = np.array([0.00144*4, 0.00129, 0.0122, 0.000494])

yyerr = np.array([(pogrbettastat[i]**2 + pogrbettax[i]**2)**0.5 for i in range(4)])

plt.errorbar(mR2, betta0y, xerr = 0, yerr = 0, fmt='.', label='Cross')
plt.ylabel(r'$I, kg{*}m^{2}$')
plt.xlabel(r'$4mR^{2}, kg{*}m^{2}$')
plt.legend()
b, a = np.polyfit(mR2, betta0y, deg=1)
print(a, b)
plt.plot(np.array([0, 0.012]), np.array([a + b*(0), a + 0.012*b]))
plt.grid(which='major', axis='both', alpha=1)
plt.plot(0, 0)

plt.title("Зависимость момента инерции от расстояния до грузиков")

plt.show()

sry2 = sum(betta0y*betta0y)/len(betta0y)
sry = sum(betta0y)/len(betta0y)
srx2 = sum(mR2*mR2)/len(mR2)
srx = sum(mR2)/len(mR2)

sigmab = 1/(4**0.5)*(((sry2-sry**2)/(srx2 - srx**2) - b**2)**0.5)
sigmaa = sigmab*((srx2 - srx**2)**0.5)
print(sigmaa, sigmab)
