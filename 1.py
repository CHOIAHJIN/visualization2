import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define the headers for the data (assuming the first row of the Excel file doesn't contain the headers)
header = ['Temperature', 'Humidity', 'RPM', 'Vibrations', 'Pressure', 'Sensor2', 'Sensor3','Sensor4','Sensor5']

# Load the data from the Excel file
data = pd.read_excel('./data/2.elevator_failure_prediction.xlsx', names = header)

# Calculate the correlation matrix
corr = data.corr(method='pearson')

# Create a figure and a subplot
fig = plt.figure()
ax = fig.add_subplot(111)

# Plot the correlation matrix with a color map
cax = ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)

# Add a color bar to the figure
fig.colorbar(cax)

# Set up ticks and labels
ticks = np.arange(0, len(header), 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(header)
ax.set_yticklabels(header)

# Display the plot
plt.show()

# Save the plot as an image file
plt.savefig('./result/corr.png')