import pandas as pd
import pickle

data = pd.read_csv("with_corr.csv")
# print(data.columns)
# feas - list(data[''])
selected = pd.read_csv("top800feas.csv")
# print(selected['fea_id'])
feas_sel = list(selected['fea_id'])
# print(len(feas_sel))
# print(feas_sel)

data = data[feas_sel]
data.to_csv("with_corr_top800.csv",index=False)
x = []

# print(len(x))     # 12758
# print(len(x[0])) # 特征维度3915
for fea in feas_sel:
    x.append(list(data[fea]))

#x  1000行  12758列
now_x = []
for i in range(12758):
    t = []
    for j in range(799):
        t.append(x[j][i])
    now_x.append(t)
print(len(now_x))
print(len(now_x[0]))

with open("data", 'rb') as f:
    family_names = pickle.load(f)
    x = pickle.load(f)
    y = pickle.load(f)


