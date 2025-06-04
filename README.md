# -Batch-Reactor-Simulation-using-Python

# 🧪 Batch Reactor Simulation using Python

This project simulates chemical reactions in a **batch reactor** for different reaction orders (1st, 2nd, and 3rd order) using Python.

It includes concentration and conversion vs time plots using **ODE solvers** and visualizations with **Matplotlib**.

## ✅ Features

- Simulates:
  - First-order reaction: `dC_A/dt = -k * C_A`
  - Second-order reaction: `dC_A/dt = -k * C_A^2`
  - Third-order reaction: `dC_A/dt = -k * C_A^3`
- Calculates **conversion**: `X(t) = 1 - C_A/C_A0`
- Plots:
  - Concentration vs Time
  - Conversion vs Time
- Easy to modify rate constant `k`, initial concentration `C_A0`, and time range

## 🔧 Tools & Libraries

- Python
- NumPy
- SciPy (`odeint`)
- Matplotlib



