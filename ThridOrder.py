#Third order ==> conc vs time and conversion vs time

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#rate Constant

k = float(input("Enter the rate constant:"))

#Initial Concentration

C_A_0 = float(input("Enter the initial concentration:"))

t= np.linspace(0,50,100)

def batch_batch_reactor_3rd_order(C_A, t):
  return -k*(C_A**3)

C_A = odeint(batch_batch_reactor_3rd_order,C_A_0,t).flatten()

x = (1-(C_A/C_A_0))

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.plot(t,C_A,"b-", linewidth=2, label="C_A(t)")
plt.xlabel("Time[min]")
plt.ylabel("Concentration[mol/L]")
plt.title("Batch Reactor: Third Order Reaction")
plt.grid(True)
plt.legend()


plt.subplot(1,2,2)
plt.plot(t,x,"g-", linewidth=2, label="X(t)")
plt.xlabel("Time[min]")
plt.ylabel("Conversion")
plt.title("Conversion vs. Time")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()