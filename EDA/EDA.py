import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
d1 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_1d.txt")
d2 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_2d.txt")
d3 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_curve.txt")
print(d1.shape,d2.shape)

plt.scatter(d1,np.random.normal(7,0.2,size=d1.size), s=1, alpha=0.5)
#  random.normal 함수를 이용해 7을 평균값으로 하고 0.2를 표준편차로 하는 정규분포를 따르는 난수를 생성
plt.scatter(d2[:,0],d2[:,1])
plt.show()