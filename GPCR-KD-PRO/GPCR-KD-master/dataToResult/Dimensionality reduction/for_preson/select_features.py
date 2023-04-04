import pandas as pd
import pickle

featureSelect = []
corr = [] # 计算相关系数
train = pd.read_csv("test1.csv")
for fea in featureSelect:
    corr.append(abs(train[[fea,'target']].fillna(0).corr().values[0][1]))

# # 构建csv文件
# with open("data_added2", 'rb') as f:
#     family_names = pickle.load(f)
#     x = pickle.load(f)
#     y = pickle.load(f)
# print(len(x))     # 12758
# print(len(x[0])) # 特征维度3915
# df = pd.DataFrame()
# for i in range(3915):
#     feas = []
#     for j in range(12758):
#         feas.append(x[j][i])
#
#     df['fea'+str(i+1)] = feas
# df['target'] = y
# df.to_csv("data.csv",index=False)

data = pd.read_csv("data.csv")
feas = data.corr()['target'].abs().sort_values(ascending=False)[:800]

feas.drop('target',axis=0,inplace=True)
feas.to_csv("top800feas.csv")
print(feas.index)

data1 = data[feas.index]
data1.to_csv("with_corr.csv",index=False)


