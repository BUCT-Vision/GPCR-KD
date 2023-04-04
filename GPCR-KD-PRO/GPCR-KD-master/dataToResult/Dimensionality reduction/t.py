from sklearn.datasets import make_classification
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import pickle


# with open("RFE_data_rf_100","rb") as f:
#     data = pickle.load(f)
#
# print(type(data))
# data = list(data)
# print(len(data))
# print(len(data[0]))
# print(data[0])
# print(data[89])


# rbf_pca = KernelPCA(n_components = 100, kernel="rbf", gamma=0.04)
# x_reduced = rbf_pca.fit_transform(x)
# with open("kcpa_data","wb") as f:
#     pickle.dump(x_reduced,f)



# with open("kcpa_data","rb") as f:
#     x = pickle.load(f)
# print(type(x))
# print(len(x))
# print(len(x[0]))
# print(x[0][0])
# print(x[1][0])
# count = 0
# for i in range(100):
#     if x[0][i]==x[1][i]:
#         count+=1
# print(count)