
# 1、递归特征消除法
# 递归消除特征法使用一个基模型来进行多轮训练，每轮训练后，消除若干权值系数的特征，
# 再基于新的特征集进行下一轮训练。使用feature_selection库的RFE类来选择特征的代码如下：

import pickle
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import time

# 递归特征消除法，返回特征选择后的数据
# 参数estimator为基模型
# 参数n_features_to_select为选择的特征个数
data = [[2,1,4,5,3],[2,1,5,6,7],[2,1,8,9,7]]
target = [1,2,3]
with open("data","rb") as f:
    scores = pickle.load(f)
    x = pickle.load(f)
    y = pickle.load(f)
print("start",time.ctime())
# x = x[0:40]
# y = y[0:40]

model=LogisticRegression(max_iter=10000)


t = RFE(estimator=model, n_features_to_select=100,step=2).fit_transform(x,y)
with open("RFE_data","wb") as f:
    pickle.dump(t,f)
print("end",time.ctime())


