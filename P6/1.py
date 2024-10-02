# Draw Pie chart, line chart, sin wave, square wave, triangular wave &amp; cos wave using Mathplot.

import numpy as np
import matplotlib.pyplot as plt 
from scipy import signal

# Pie chart
labels = ['Apples','Banana','Grapes']
sizes = [30,50,20]
colors = ['red', 'yellow', 'green']

plt.pie(sizes, labels=labels, colors=colors)
plt.axis('equal')
plt.title('Pie Chart')
plt.show()


# Line chart
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y, marker='o')
plt.title("Line chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()


# sine wave
x = np.linspace(0, 2 * np.pi, 100)  # X values from 0 to 2pi
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('Angle [radians]')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()


# square wave
x = np.linspace(0, 2 * np.pi, 100)  # X values
y = signal.square(x)

plt.plot(x, y)
plt.title('Square Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


# triangular wave
x = np.linspace(0, 2 * np.pi, 1000)
y = signal.sawtooth(x, 0.5)  # 0.5 gives a triangular wave

plt.plot(x, y)
plt.title('Triangular Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


# cosine wave
x = np.linspace(0, 2 * np.pi, 100)  # X values from 0 to 2pi
y = np.cos(x)

plt.plot(x, y)
plt.title('Cosine Wave')
plt.xlabel('Angle [radians]')
plt.ylabel('cos(x)')
plt.grid(True)
plt.show()


