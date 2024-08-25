import matplotlib.pyplot as plt
import pandas as  pd
import numpy as  np

header = ['Temperature', 'Humidity', 'RPM', 'Vibrations', 'Pressure', 'Sensor2', 'Sensor3','Sensor4','Sensor5']
data = pd.read_excel('./data/2.elevator_failure_prediction.xlsx', names = header)

corr = data.corr(method='pearson')

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr, cmap = 'coolwarm', vmin = -1, vmax = 1)
fig.colorbar(cax)
ticks = np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(header)
ax.set_yticklabels(header)
plt.show()
plt.savefig('./result/corr.png')