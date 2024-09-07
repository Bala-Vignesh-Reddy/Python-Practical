# Draw histogram with random number and 2 histogram in the same plot

import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data1 = np.random.normal(0, 1, 1000)  # 1000 samples from a normal distribution with mean 0 and std deviation 1
data2 = np.random.normal(1, 1.5, 1000)  # 1000 samples from a normal distribution with mean 1 and std deviation 1.5

# Create a histogram
plt.hist(data1, bins=30, alpha=0.5, label='Data 1', color='blue')
plt.hist(data2, bins=30, alpha=0.5, label='Data 2', color='red')

# Add titles and labels
plt.title('Histogram of Two Datasets')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Add a legend
plt.legend()

# Show the plot
plt.show()

