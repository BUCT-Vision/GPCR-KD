# https://blog.csdn.net/hh1357102/article/details/127045257

from sklearn.decomposition import PCA
import time
import pickle
import numpy as np


with open("data", 'rb') as f:
    family_names = pickle.load(f)
    x = pickle.load(f)
    y = pickle.load(f)

print("start",time.ctime())

num = 50
num = 100

num = 500

num = 300

num = 700


rbf_pca = PCA(n_components = num)
x_reduced = rbf_pca.fit_transform(x)
with open("pca_data"+str(num),"wb") as f:
    pickle.dump(x_reduced,f)

print("end",time.ctime())
