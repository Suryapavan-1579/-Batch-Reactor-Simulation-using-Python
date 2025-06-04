#second order conc vs time and conversion vs time

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#rate constant
k = float(input("Enter the rate constant:"))

#initial concentration
C_A_0 = float(input("Enter the initial concentration:"))

t = np.linspace(0,50,100)

def batch_reactor_2nd_order(C_A,t):
  return -k*(C_A**2)

C_A = odeint(batch_reactor_2nd_order,C_A_0,t).flatten()

x = (1-(C_A/C_A_0))

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.plot(t,C_A,"b-",linewidth=3,label="C_A(t)")
plt.xlabel("Time[min]")
plt.ylabel("Concentration[mol/L]")
plt.title("Concnentration vs Time")
plt.grid(True)
plt.legend()

plt.subplot(1,2,2)
plt.plot(t,x, "g-" ,linewidth=3, label="X(t)")
plt.xlabel("Time[min]")
plt.ylabel("Conversion")
plt.title("Conversion vs. Time")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
