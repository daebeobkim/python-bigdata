from pandas import Series
import numpy as np

data = [1000,2000,3000]
index = ["메로나","구구콘","하겐다즈"]
s = Series(data,index)
print(s)