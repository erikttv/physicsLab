# Vi importerer nødvendige biblioteker:
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

# Horisontal avstand mellom festepunktene er 200 mm
h = 200
xfast=np.asarray([0,h,2*h,3*h,4*h,5*h,6*h,7*h])
# Vi begrenser starthøyden (og samtidig den maksimale høyden) til
# å ligge mellom 250 og 300 mm
# yfast: tabell med 8 heltall mellom 50 og 300 (mm); representerer
# høyden i de 8 festepunktene
height = [0.276, 0.207, 0.187, 0.224, 0.167, 0.087, 0.055, 0.108]
yfast=np.asarray(height)


# banens stigningstall beregnet med utgangspunkt i de 8 festepunktene.
inttan = np.diff(yfast)/h

# Omregning fra mm til m:
xfast = xfast/1000
#yfast = yfast/1000

#Programmet beregner deretter de 7 tredjegradspolynomene, et
#for hvert intervall mellom to nabofestepunkter.

#Med scipy.interpolate-funksjonen CubicSpline:
cs = CubicSpline(xfast, yfast, bc_type='natural')
xmin = 0.000
xmax = 1.401
dx = 0.001
x = np.arange(xmin, xmax, dx)
Nx = len(x)
y = cs(x)
dy = cs(x,1)
d2y = cs(x,2)

#Plotting velocity
c = 2/5
g = 9.81
v = np.sqrt((2*g*(y[0]-y))/(1+c))


f = open("Experimental data/007new2", "r")
lines = f.readlines();
values = []
elements = []
for line in lines:
    line = line.split("\t")
    values.append(line)
f.close()
for index in range(len(values)):
    values[index][-1] = values[index][-1][:-1]

exper_x = []
exper_v = []
for index in range(len(values)):
    if (index != 0 and index != 1 and index != len(values)-1):
        exper_x.append(abs(float(values[index][1])))
        exper_v.append(float(values[index][3]))

relative_x = [0]
for index in range(len(exper_x)-1):
    difference = abs(exper_x[index+1] - exper_x[index])
    relative_x.append(difference + relative_x[index])



print("siste verdi i fart: ", v[-1])

baneform = plt.figure('y(x)',figsize=(12,3))
plt.plot(x,v)
plt.plot(relative_x, exper_v)
plt.title('Banens fart med posisjon')
plt.xlabel('$x$ (m)',fontsize=20)
plt.ylabel('$v(x)$ (m/s)',fontsize=20)
plt.grid()
plt.show()