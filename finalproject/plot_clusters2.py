#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator 

datapoints = pd.read_csv('output.txt', sep='\t', names=['X', 'Y', 'Cluster'], skiprows=1)
centers = pd.read_csv('centers.txt', sep='\t', header=None, names=['CenterX', 'CenterY'])

plt.rcParams['font.family'] = 'sans-serif'

fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.grid(color='gray', linestyle='--', linewidth=0.5) 

scatter = ax.scatter(datapoints['X'], datapoints['Y'], c=datapoints['Cluster'].astype(int), cmap='rainbow', alpha=0.7) 

ax.scatter(centers['CenterX'], centers['CenterY'], marker='o', s=200, c='white', label='Centers') 

ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

ax.tick_params(axis='both', colors='white')


legend = ax.legend()
for text in legend.get_texts():
	text.set_color('gray')


ax.set_title('iCluster Output', color='white')

ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

 
plt.savefig('cluster_plot.png', bbox_inches='tight', pad_inches=0.1, facecolor=fig.get_facecolor())


