import matplotlib.pyplot as plt
import numpy as np
from math import log
from scipy import integrate
import ipywidgets as ipw

alpha = 1. 
beta = 1.
delta = 1.
gamma = 1.
x0 = 4.
y0 = 2.

def derivative(X, t, alpha, beta, delta, gamma):
    x, y = X
    dotx = x * (alpha - beta * y)
    doty = y * (-delta + gamma * x)
    return np.array([dotx, doty])

Nt = 1000
tmax = 30.
t = np.linspace(0.,tmax, Nt)
X0 = [x0, y0]
res = integrate.odeint(derivative, X0, t, args = (alpha, beta, delta, gamma))
x, y = res.T

plt.figure()
plt.grid()
plt.title("odeint method")
plt.plot(t, x, label = 'Deer')
plt.plot(t, y, label = "Wolves")
plt.xlabel('Time t, [days]')
plt.ylabel('Population')
plt.legend()

plt.show()

# rabbit_count = 10 # икс
# rabbit_birth_rate = 1.5 # альфа
# rabbit_death_rate = 5 # бета

# fox_count = 10 # игрек
# fox_birth_rate = 10 # дельта
# fox_death_rate = 1 # гамма

# rabbits = [rabbit_count]
# foxes = [fox_count]

# x, y = symbols('x t')
# print(diff(rabbit_birth_rate*x))