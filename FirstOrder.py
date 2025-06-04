import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint



#rate Constant

k = float(input("Enter the Rate Constant :"))


#Initial Concentration

C_A_0 = float(input("Enter the Initial Concentration of A :"))


t = np.linspace(0,50,100)

#equation dca/dt = -k*ca


def Batch_reactor(C_A,t):
    return -k*C_A

C_A = odeint(Batch_reactor,C_A_0,t)



plt.figure(figsize=(8,5))
plt.plot(t, C_A, "r-", linewidth=2, label='C_A(t)')
plt.xlabel('Time [min]')
plt.ylabel('Concentration of A [mol/L]')
plt.title('Batch Reactor: First-Order Reaction')
plt.grid(True)
plt.legend()
plt.show()