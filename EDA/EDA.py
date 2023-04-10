import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

d1 = np.loadtxt("C:/Users/rlaeo/Downloads/1D/example_1.txt")
d2 = np.loadtxt("C:/Users/rlaeo/Downloads/1D/example_2.txt")

cdf = np.linspace(1/d1.size,1,d1.size) #cdf는 누적 분포 함수
sd1 = np.sort(d1)
sd2 = np.sort(d2)
plt.plot(sd1,cdf,label="D1 CDF")
plt.plot(sd2,cdf,label="D2 CDF")
plt.hist(d1,histtype="step",density=True,alpha=0.3)
plt.hist(d2,histtype="step",density=True,alpha=0.3)
plt.legend()
plt.show()