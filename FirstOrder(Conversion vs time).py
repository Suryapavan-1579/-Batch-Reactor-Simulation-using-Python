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

C_A = odeint(Batch_reactor,C_A_0,t).flatten()

x = ((1-C_A)/C_A_0)   #conversion



plt.figure(figsize=(10,5))



plt.subplot(1, 2, 1)
plt.plot(t, C_A, 'b-', label='C_A(t)', linewidth=2)
plt.xlabel('Time [min]')
plt.ylabel('Concentration [mol/L]')
plt.title('Concentration vs. Time')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t, x, 'g-', label='X(t)', linewidth=2)
plt.xlabel('Time [min]')
plt.ylabel('Conversion')
plt.title('Conversion vs. Time')
plt.grid(True)
plt.legend()


plt.tight_layout()
plt.show()