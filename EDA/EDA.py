import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
d1 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_1d.txt")
d2 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_2d.txt")
d3 = np.loadtxt("C:/Users/rlaeo/Downloads/Outliers (1)/outlier_curve.txt")


xs,ys = d3.T #T를 붙혀 치환할 수 있도록 만듦
p = np.polyval(xs,ys,deg=5)  #np.polyfit을 입력해 다항식을 얻음, 5차 다항식이 되도록 deg=5를 입력, 이걸로 x값,x제곱값,x세제곱 등을 구할 수 있음
#y값을 다시 얻고자 하거나 다항식을 표본으로 추출하고자 한다면 np.polyval을 사용
print(p)
