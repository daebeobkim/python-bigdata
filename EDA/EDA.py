import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

d1 = np.loadtxt("C:/Users/rlaeo/Downloads/1D/example_1.txt")
d2 = np.loadtxt("C:/Users/rlaeo/Downloads/1D/example_2.txt")

dataset = pd.DataFrame({
    "value":np.concatenate((d1,d2)),
    "type":np.concatenate((np.ones(d1.shape),np.zeros(d2.shape)))
})
dataset.info()

sns.swarmplot(dataset["value"])
sns.set()