import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
d1 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_1d.txt")
d2 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_2d.txt")
d3 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_curve.txt")

xs,ys = d3.T

x,y = xs.copy(), ys.copy()
for i in range(5):
    p = np.polyfit(x,y,deg=5)
    ps = np.polyval(p,x)
    good = y - ps < 7 #거리는 3미만, 데이터 물리학에서는 음수가 없기때문에 음수는 가정x

    x_bad, y_bad = x[~good],y[~good]
    x,y = x[good],y[good]

    plt.plot(x,y,".",label = "Used Data")
    plt.plot(x,np.polyval(p,x),label = f"poly fit{i}")
    plt.plot(x_bad,y_bad,".",label="Not used Data")
    plt.legend()
    plt.show()

    if (~good).sum() == 0:
        break
