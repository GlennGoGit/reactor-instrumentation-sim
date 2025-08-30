"""
control_simulation.py
Synthetic demo of reactor instrumentation and feedback control.
⚠️ NOTE: This uses fake data and is for demonstration purposes only.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Simulation parameters ---
np.random.seed(42)
time_steps = 100
temperature = []
pressure = []

# Initial conditions
temp = 300   # Kelvin
press = 1500 # psi

# Controller setpoints
temp_setpoint = 320
press_setpoint = 1600

# Control gains (tune these for realism)
temp_gain = 0.2
press_gain = 0.15

for t in range(time_steps):
    # Sensor noise
    temp_noise = np.random.normal(0, 2)
    press_noise = np.random.normal(0, 5)
    
    # Feedback control (if below setpoint, add heat/flow)
    temp += temp_gain * (temp_setpoint - temp) + temp_noise
    press += press_gain * (press_setpoint - press) + press_noise
    
    temperature.append(temp)
    pressure.append(press)

# --- Plot results ---
fig, ax = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax[0].plot(range(time_steps), temperature, color='red', label='Temperature (K)')
ax[0].axhline(y=temp_setpoint, color='black', linestyle='--', label='Setpoint')
ax[0].set_ylabel('Temperature (K)')
ax[0].legend()

ax[1].plot(range(time_steps), pressure, color='blue', label='Pressure (psi)')
ax[1].axhline(y=press_setpoint, color='black', linestyle='--', label='Setpoint')
ax[1].set_ylabel('Pressure (psi)')
ax[1].set_xlabel('Time Step')
ax[1].legend()

plt.suptitle("Synthetic Reactor Instrumentation Simulation")
plt.tight_layout()
plt.show()
