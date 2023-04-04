import time
import pickle

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
import sklearn.naive_bayes as nb
import numpy as np
from collections import defaultdict
import analysize
from sklearn.neighbors import KNeighborsClassifier


def preprocess(x):
    X_train = preprocessing.scale(np.array(x))
    return X_train


def classifier(x, y):
    clf = SVC()

    clf.fit(x, y)
    return clf

print(time.ctime(), ":" ,'开始读取数据!')
with open("data", 'rb') as f:
    family_names = pickle.load(f)
    x = pickle.load(f)
    y = pickle.load(f)

# with open("top10fea","rb") as f:
#     x = pickle.load(f)
#     y = pickle.load(f)

# with open("top20fea","rb") as f:
#     x = pickle.load(f)
#     y = pickle.load(f)
#
# with open("top50fea","rb") as f:
#     x = pickle.load(f)
#     y = pickle.load(f)
#
# with open("top80fea","rb") as f:
#     x = pickle.load(f)
#     y = pickle.load(f)


# with open("top90fea","rb") as f:
#     x = pickle.load(f)
#     y = pickle.load(f)


# with open("lda50","rb") as f:
#     x = pickle.load(f)

# with open("lda100","rb") as f:
#     x = pickle.load(f)

# with open("lda150","rb") as f:
#     x = pickle.load(f)

# with open("lda200","rb") as f:
#     x = pickle.load(f)
#

#
# with open("lda250","rb") as f:
#     x = pickle.load(f)


# #

#


# with open("pca_data50","rb") as f:
#     x = pickle.load(f)
# with open("pca_data100","rb") as f:
#     x = pickle.load(f)
# # #
# with open("pca_data300","rb") as f:
#     x = pickle.load(f)
# with open("pca_data500","rb") as f:
#     x = pickle.load(f)
# with open("pca_data700","rb") as f:
#     x = pickle.load(f)
#


# 1000  1500  2000
with open("data_corr_top_1000","rb") as f:
    ff = pickle.load(f)
    x = pickle.load(f)
    y = pickle.load(f)

with open("data_corr_top_1500","rb") as f:
    ff = pickle.load(f)
    x = pickle.load(f)
    y = pickle.load(f)

with open("data_corr_top_2000","rb") as f:
    ff = pickle.load(f)
    x = pickle.load(f)
    y = pickle.load(f)

print(x[0])
x_max_val = 0
for i in range(len(x)):
    for v in x[i]:
        if v>x_max_val:
            x_max_val = v
print("x-max= ",x_max_val)



print(time.ctime(), ":" ,'读取完毕, 开始预处理!')


print("before")
print(len(x[0]))
print(x[0])

x = preprocess(x)
print("after")
print(len(x[0]))
print(x[0])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
print(len(x_train[0]))
print(x_train[0])
print(len(x_train[1]))
print(x_train[1])


try:
    print(time.ctime(), ":","训练数据数量：", len(x_train))
    print(time.ctime(), ":","预测数据数量：", len(x_test))
except Exception as e:
    print(time.ctime(), ":","读取长度失败：", e)

test_num = len(x_test)

print(time.ctime(), ":" ,"开始训练!")


classifier_factory = ["MLPClassifier(hidden_layer_sizes=(2000,2000), max_iter=1000)","RandomForestClassifier()","SVC()","GaussianNB()"]







clf = MLPClassifier(hidden_layer_sizes=(2000,2000), max_iter=1000)
# clf = KNeighborsClassifier()
#
# clf = SVC()
# clf = RandomForestClassifier()
clf.fit(x_train, y_train)


print(time.ctime(), ":" ,"开始预测!")
result = clf.predict(x_test)
print(time.ctime(), ":" ,"预测完毕, 开始写入结果!")
count = 0

with open('./resultknn.txt', 'w') as f:
    for y, r in zip(y_test, result):

        if y != r:
            f.write("应分到{}, 结果{}\n".format(family_names[y], family_names[r]))

            count += 1
    print(1 - count / len(result), file=f, end='\n')

analysize.main(test_num)



