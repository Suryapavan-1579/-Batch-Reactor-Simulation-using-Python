# 🔬 Batch Reactor Simulation using Python

This project simulates batch reactor performance for **1st, 2nd, and 3rd order reactions** using Python. The aim is to analyze how reactant concentration and conversion vary with time 

## ✅ Features

- Solves ODEs for:
  - First-order: (r_A = -kC_A)
  - Second-order: (r_A = -kC_A**2)
  - Third-order: ( r_A = -kC_A**3)
- Plots:
  - Concentration vs. Time
  - Conversion vs. Time
- Configurable:
  - Initial concentration ( C_A_0)
  - Rate constant (k)
  - Time range (t)

## 🧪 Tools Used

- Python
- NumPy
- SciPy (`odeint`)
- Matplotlib



## 📂 How to Run

python first_order_simulation.py
python second_order_simulation.py
python third_order_simulation.py
