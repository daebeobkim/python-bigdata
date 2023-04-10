import numpy as np
import matplotlib.pyplot as plt
import seaborn
import pandas as pd

d1 = np.loadtxt("C:/Users/rlaeo/Downloads/1D/example_1.txt")
d2 = np.loadtxt("C:/Users/rlaeo/Downloads/1D/example_2.txt")
bins = np.linspace(min(d1.min(),d2.min()),max(d1.max(),d2.max()),50)#순서대로 구간시작점, 구간끝점, 구간 내 숫자 갯수
plt.hist([d1,d2], bins=bins, label="Stacked",density = True,alpha=0.5)
plt.hist(d1,bins=bins,label="D1", density = True,histtype = "step", lw = 3)# density = True 사용시 %로 출력
plt.hist(d2, bins=bins, label="D2",density = True,histtype = "step",ls=":")
plt.legend()
plt.ylabel("Probability")
plt.show()