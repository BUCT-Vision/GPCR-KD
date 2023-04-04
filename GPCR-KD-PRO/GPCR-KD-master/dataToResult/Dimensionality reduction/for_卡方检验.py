# https://blog.csdn.net/qq_39951635/article/details/114933713

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pickle
import time


# with open("Chi2_static","rb") as f:
#     scores = pickle.load(f)
# socres = list(scores)
#
# rec = []
# for i in range(len(socres)):
#     rec.append([socres[i],i])
# rec.sort(reverse=True)



# 前10%	390
# 前20%	779
# 前50%	1948
# 前80%	3116
# 前90%	3506

# 取全部特征  前90%  前80%  50%  10%  20%

# top10fea = []
# for i in range(390):
#     top10fea.append(rec[i][1])
#
# top20fea = []
# for i in range(779):
#     top20fea.append(rec[i][1])
#
# top50fea = []
# for i in range(1948):
#     top50fea.append(rec[i][1])
#
# top80fea = []
# for i in range(3116):
#     top80fea.append(rec[i][1])
#
# top90fea = []
# for i in range(3506):
#     top90fea.append(rec[i][1])


# with open("data","rb") as f:
#     family_name = pickle.load(f)
#     x = pickle.load(f)
#     y = pickle.load(f)






# for i in range(len(x)):
#     t = []
#     for index_num in top10fea:
#         t.append(x[i][index_num])
#     x[i] = t[:]
#
# with open("top10fea","wb") as f:
#     pickle.dump(x,f)
#     pickle.dump(y,f)



# for i in range(len(x)):
#     t = []
#     for index_num in top20fea:
#         t.append(x[i][index_num])
#     x[i] = t[:]
#
# with open("top20fea","wb") as f:
#     pickle.dump(x,f)
#     pickle.dump(y,f)

#
#
# for i in range(len(x)):
#     t = []
#     for index_num in top50fea:
#         t.append(x[i][index_num])
#     x[i] = t[:]
#
# with open("top50fea","wb") as f:
#     pickle.dump(x,f)
#     pickle.dump(y,f)
# #
#
# for i in range(len(x)):
#     t = []
#     for index_num in top80fea:
#         t.append(x[i][index_num])
#     x[i] = t[:]
#
# with open("top80fea","wb") as f:
#     pickle.dump(x,f)
#     pickle.dump(y,f)
#
#
#
# for i in range(len(x)):
#     t = []
#     for index_num in top90fea:
#         t.append(x[i][index_num])
#     x[i] = t[:]
#
# with open("top90fea","wb") as f:
#     pickle.dump(x,f)
#     pickle.dump(y,f)

with open("top90fea","rb") as f:
    x = pickle.load(f)
    y = pickle.load(f)





