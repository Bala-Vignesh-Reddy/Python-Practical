# Draw scatter plot of exponential increasing, exponential decrease and linear with legend and different marker and colour and change the location

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

# Exponential increase
y_exp_inc = np.exp(x)

# Exponential decrease
y_exp_dec = np.exp(-x)

# Linear data
y_linear = x

# Create the plot
fig, axs = plt.subplots(1,2, figsize=(15,5))

# Plot exponential increase
axs[0].scatter(x, y_exp_inc, color='blue', marker='o', label='Exponential Increase')

# Plot linear data
axs[0].scatter(x, y_linear, color='green', marker='s', label='Linear')
axs[0].set_title('Scaler Plot')
axs[0].set_xlabel('X-axis')
axs[0].set_ylabel('Y-axis')

# Add legend
axs[0].legend(loc='best')

# Add titles and labels
axs[1].scatter(x, y_exp_dec, color='red', marker='x', label='Exponential Decrease')
plt.legend(loc='best')
plt.title('Scater Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

