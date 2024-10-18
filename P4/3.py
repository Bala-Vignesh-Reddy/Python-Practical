# Draw sine wave using dashed line, range of y axis should be limited in range (-1,1) and draw a line of y=5, text annotate value at x=1.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)

y = np.sin(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Sine Wave', color='blue')

# Add title and labels
plt.title('Sine Wave')
plt.xlabel('x (radians)')
plt.ylabel('sin(x)')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

plt.show()
