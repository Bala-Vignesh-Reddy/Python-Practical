#Plot Linear, Scatter and Bar chat of the same data using subplot

import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(1,11)
y = np.random.randint(1, 100, size=10)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Line plot
axs[0].plot(x, y, marker='o', linestyle='-')
axs[0].set_title('Linear Plot')
axs[0].set_xlabel('X Axis')
axs[0].set_ylabel('Y Axis')

# Scatter Plot
axs[1].scatter(x, y, color='r')
axs[1].set_title('Scatter Plot')
axs[1].set_xlabel('X Axis')
axs[1].set_ylabel('Y Axis')

# Bar Plot
axs[2].bar(x, y, color='g')
axs[2].set_title('Bar Plot')
axs[2].set_xlabel('X Axis')
axs[2].set_ylabel('Y Axis')

plt.tight_layout()
plt.show()
