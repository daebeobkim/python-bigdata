import numpy as np
import matplotlib.pyplot as plt
import seaborn
import pandas as pd

d1 = np.loadtxt("C:/Users/rlaeo/Downloads/1D/example_1.txt")
d2 = np.loadtxt("C:/Users/rlaeo/Downloads/1D/example_2.txt")
print(d1.shape,d2.shape)

plt.hist(d1,label="D1")
plt.hist(d2,label="D2")
plt.show()