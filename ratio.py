# Vi importerer nødvendige biblioteker:
from math import sin

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

#Finding velocity dependent on time
vinkel = np.arctan(dy)
vx = np.cos(vinkel)*v

u = 0.5*(vx[1:] + vx[:-1])
dt = dx/u

t = [0]
for d in dt:
    t.append(t[-1] + d)

#need only mass for friction
m = 1
f = (c*m*g*np.sin(vinkel))/(1+c)

#Normal force
krum = ((d2y/((1+dy**2)**(3/2))))

N = m*(g*np.cos(vinkel) + v**2*krum)


baneform = plt.figure('y(x)',figsize=(12,3))
plt.plot(x,np.abs(f/N))
plt.title('Forhold mellom f og N')
plt.xlabel('$x$ (m)',fontsize=20)
plt.ylabel('$f/N$ (N)',fontsize=20)
plt.grid()
plt.show()