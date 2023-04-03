import numpy as np
import pickle
import pandas as pd
filename = pd.read_csv('C:/Users/rlaeo/OneDrive/바탕 화면/LoadingDatasets/load.csv')
cols = None
data = []
with open(filename) as f:
    for line in f.readlines():
        vals = line.replace("\n","").split(",")
        print(vals)
        