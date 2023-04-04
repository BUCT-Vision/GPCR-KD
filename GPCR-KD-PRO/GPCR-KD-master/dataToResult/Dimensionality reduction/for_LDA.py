#!/user/bin/env python3
# -*- coding: utf-8 -*-

# https://blog.csdn.net/qq_47281915/article/details/121165837


from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
import time


# with open("lda_data", 'rb') as f:
#     lda_data = pickle.load(f)
# print(len(lda_data))
# print(type(lda_data))
# for i in range(len(lda_data)):
#     print(lda_data[i])



with open("data", 'rb') as f:
    lda_data = pickle.load(f)
    x = pickle.load(f)
    y = pickle.load(f)



# 降维后LDA维度
num = 50
num = 100
# num = 150
# num = 200
# num = 250
lda = LDA(n_components=num)
print("start")
print(time.ctime())

new_data = lda.fit_transform(x,y)
with open("lda"+str(num),"wb") as f:
    pickle.dump(new_data,f)

print("finish")
print(time.ctime())




