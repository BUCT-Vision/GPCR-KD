import pandas as pd
import pickle

# 构建csv文件
# with open("data", 'rb') as f:
#     family_names = pickle.load(f)
#     x = pickle.load(f)
#     y = pickle.load(f)
# print(len(x))     # 12758
# print(len(x[0])) # 特征维度3915
# df = pd.DataFrame()
# for i in range(3895):
#     feas = []
#     for j in range(12758):
#         feas.append(x[j][i])
#
#     df['fea'+str(i+1)] = feas
# df['target'] = y
# df.to_csv("data.csv",index=False)


# 测试 csv 文件
# df = pd.read_csv("data.csv")
# print(df.columns)
# print(df['target'])

# 预定
# 选择 前20%  40%  50%  60%  80% 特征 并分别存储成文件
#  779  1558  1947   2337  3116  3895







