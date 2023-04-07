import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
d1 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_1d.txt")
d2 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_2d.txt")
d3 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_curve.txt")
xs,ys = d3.T #T를 붙혀 치환할 수 있도록 만듦
p = np.polyfit(xs,ys,deg=5)  #np.polyfit을 입력해 다항식을 얻음, 5차 다항식이 되도록 deg=5를 입력, 이걸로 x값,x제곱값,x세제곱 등을 구할 수 있음
#y값을 다시 얻고자 하거나 다항식을 표본으로 추출하고자 한다면 np.polyval을 사용
ps = np.polyval(p,xs)#을 입력하고 p,xs를 전달

x,y = xs.copy(), ys.copy()
for i in range(5):
    p = np.polyfit(x,y,deg=5)
    ps = np.polyval(p,x)
    good = y - ps < 3 #거리는 3미만, 데이터 물리학에서는 음수가 없기때문에 음수는 가정x

    x_bad, y_bad = x[~good],y[~good]
    x,y = x[good],y[good]

    plt.plot(x,y,".",label = "Used Data")
    plt.plot(x,np.polyval(p,x),label = f"poly fit{i}")
    plt.plot(x_bad,y_bad,".",label="Not used Data")
    plt.legend()
    plt.show()

    if (~good).sum() == 0:
        break