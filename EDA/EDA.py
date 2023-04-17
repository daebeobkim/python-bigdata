import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
d1 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_1d.txt")
d2 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_2d.txt")
d3 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_curve.txt")

fig = plt.figure()
x = [0,1,2,3,4]
y = [10,25,30,8,30]
fig, plt.plot(x,y,label='Test')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Main Title')
plt.legend()
plt.show()
