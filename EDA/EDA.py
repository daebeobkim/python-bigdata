import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

X = np.linspace(0, 2*np.pi)
Y = np.sin(X)

fig, ax = plt.subplots()
ax.plot(X, Y)
plt.show()