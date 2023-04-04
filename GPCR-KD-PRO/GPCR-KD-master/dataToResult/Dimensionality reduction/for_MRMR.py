# https://blog.csdn.net/qlkaicx/article/details/127884395


import pymrmr
import pandas as pd
import pymrmr
import pickle




#读入数据
df = pd.read_csv("mrmr.csv")

# 选取十个特征

# 5个值
num = 390
num = 779
num = 1948
num = 3116
num = 3506
mr = pymrmr.mRMR(df, 'MIQ', num)
with open("mrmr"+str(num),"wb") as f:
    pickle.dump(mr,f)






