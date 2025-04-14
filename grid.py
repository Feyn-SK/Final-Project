"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import random

np.set_printoptions(threshold=np.inf)
data = np.empty((50,50)).

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = random.randint(0,5)

print(data)
cmap_to_use = colors.ListedColormap(['white',(0.8, 0.8, 1),'blue', 'red','black'])

plt.figure(figsize=(7,6))
plt.pcolor(data,cmap = cmap_to_use,edgecolors='k', linewidth=0.5, vmin=0, vmax=2)

plt.show()
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import random

np.set_printoptions(threshold=np.inf)
data = np.empty((50,50))

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = random.randint(0,4)


    'States: 0:white, 1:light_blue, 2: Dark_blue, 3: red, 4:black'

cmap_to_use = colors.ListedColormap(['white',(0, 0.8, 1),'blue', 'red','black'])

plt.figure(figsize=(7,6))
plt.imshow(data,cmap = cmap_to_use)
plt.grid(which='both', color='k', linewidth=0.5)
plt.xticks([])
plt.yticks([])
plt.show()


