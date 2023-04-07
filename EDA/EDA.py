import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
d1 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_1d.txt")
d2 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_2d.txt")
d3 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_curve.txt")
mean, std = np.mean(d1), np.std(d1)
z_score = np.abs((d1-mean)/std)
threshold = 3
good = z_score < threshold
print(f"Rejection {(~good).sum()} points")# ~: 결과값 뒤집기
from scipy.stats import norm
print(f"z-score of 3 corresponds to a prob of {100 * 2 * norm.sf(threshold):0.2f}%")
visual_scatter = np.random.normal(size=d1.size)
plt.scatter(d1[good], visual_scatter[good], s=2, label="Good", color = "#4CAF50")
plt.scatter(d1[~good], visual_scatter[~good], s=2, label='Bad', color = '#F44336')
plt.legend()

plt.show()
plt.plot