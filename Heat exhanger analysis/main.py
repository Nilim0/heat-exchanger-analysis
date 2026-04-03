import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Sample Data (you can replace this with CSV)
# -----------------------------

df = pd.read_csv("data.csv")

# -----------------------------
# Constants
# -----------------------------
Cp = 4180  # J/kg.K (for water)

# -----------------------------
# Heat Transfer Calculation
# Q = m * Cp * ΔT
# -----------------------------
df['Q_hot'] = df['m_hot'] * Cp * (df['Th_in'] - df['Th_out'])
df['Q_cold'] = df['m_cold'] * Cp * (df['Tc_out'] - df['Tc_in'])

# Take average heat transfer
df['Q_avg'] = (df['Q_hot'] + df['Q_cold']) / 2

# -----------------------------
# Effectiveness Calculation
# ε = Q_actual / Q_max
# Q_max = C_min * (Th_in - Tc_in)
# -----------------------------
C_hot = df['m_hot'] * Cp
C_cold = df['m_cold'] * Cp

C_min = np.minimum(C_hot, C_cold)

df['Q_max'] = C_min * (df['Th_in'] - df['Tc_in'])
df['Effectiveness'] = df['Q_avg'] / df['Q_max']

# -----------------------------
# Display Results
# -----------------------------
print(df[['Q_avg', 'Effectiveness']])

# -----------------------------
# Plot Graphs
# -----------------------------
plt.figure()
plt.plot(df.index, df['Q_avg'], marker='o')
plt.title("Heat Transfer Rate vs Data Point")
plt.xlabel("Experiment Number")
plt.ylabel("Q (Watts)")
plt.grid()
plt.show()

plt.figure()
plt.plot(df.index, df['Effectiveness'], marker='o')
plt.title("Effectiveness vs Data Point")
plt.xlabel("Experiment Number")
plt.ylabel("Effectiveness")
plt.grid()
plt.show()