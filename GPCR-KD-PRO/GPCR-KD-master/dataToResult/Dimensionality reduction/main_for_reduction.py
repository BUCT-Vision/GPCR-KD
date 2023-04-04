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

from sklearn.neighbors import KNeighborsClassifier


def preprocess(x):
    X_train = preprocessing.scale(np.array(x))
    return X_train


def classifier(x, y):
    clf = SVC()
    # clf = SVC()
    #clf = RandomForestClassifier()
    # clf = GaussianNB()
    clf.fit(x, y)
    return clf

print(time.ctime(), ":" ,'开始读取数据!')
with open("top90fea", 'rb') as f:

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

# random_state  7
# 0.9521943573667712
# family level:         0.9937304075235109
# subfamily level:      0.9725705329153606
# sub-subfamily level:  0.966692789968652

# random_state  6
# 0.9561128526645768
# family level:         0.9945141065830722
# subfamily level:      0.9760971786833856
# sub-subfamily level:  0.9698275862068966


# random_state  1
# 0.9612068965517241
# family level:         0.9945141065830722
# subfamily level:      0.9804075235109718
# sub-subfamily level:  0.9749216300940439
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

clf = KNeighborsClassifier()
clf = RandomForestClassifier()
# clf = MLPClassifier(hidden_layer_sizes=(2000,2000), max_iter=1000)
clf.fit(x_train, y_train)

print(time.ctime(), ":" ,"开始预测!")
result = clf.predict(x_test)
print(time.ctime(), ":" ,"预测完毕, 开始写入结果!")
count = 0

with open('./resultknn.txt', 'w') as f:
    for y, r in zip(y_test, result):

        if y != r:


            count += 1
    print(1 - count / len(result), file=f, end='\n')




# 不同精度
# 不同分类器
# 不同类别
# 不同替换矩阵
# family level:         0.9902037617554859
# subfamily level:      0.9678683385579937
# sub-subfamily level:  0.9623824451410659

# family level:         0.9917711598746082
# subfamily level:      0.9678683385579937
# sub-subfamily level:  0.963166144200627


# 0.9525862068965517
# family level:         0.9886363636363636
# subfamily level:      0.9690438871473355
# sub-subfamily level:  0.9643416927899686



# 0.9467084639498433
# family level:         0.9898119122257053
# subfamily level:      0.9670846394984326
# sub-subfamily level:  0.9619905956112853

# added
# 0.9553291536050157
# family level:         0.9921630094043887
# subfamily level:      0.9733542319749217
# sub-subfamily level:  0.9678683385579937

# 0.9537617554858934
# family level:         0.9925548589341693
# subfamily level:      0.9713949843260188
# sub-subfamily level:  0.9663009404388715

# add 20
# 0.9553291536050157
# family level:         0.9921630094043887
# subfamily level:      0.9721786833855799
# sub-subfamily level:  0.9686520376175549


# MLP add 20
# 0.9533699059561128
# family level:         0.9925548589341693
# subfamily level:      0.9741379310344828
# sub-subfamily level:  0.9690438871473355

# 筛选一下特征再建模

# corr_top_800
# 0.9592476489028213
# family level:         0.9917711598746082
# subfamily level:      0.975705329153605
# sub-subfamily level:  0.9717868338557993

# corr_top_1000
# 0.9596394984326019
# family level:         0.9945141065830722
# subfamily level:      0.9776645768025078
# sub-subfamily level:  0.9737460815047022

# corr_top_1000
# 0.9600313479623824
# family level:         0.9933385579937304
# subfamily level:      0.97923197492163
# sub-subfamily level:  0.9745297805642633

# corr_top_1000  MLP
# 0.9737460815047022
# family level:         0.9964733542319749
# subfamily level:      0.9862852664576802
# sub-subfamily level:  0.9827586206896551

# 0.9427899686520376
# family level:         0.9902037617554859
# subfamily level:      0.9627742946708464
# sub-subfamily level:  0.9561128526645768

# corr_top_1000
# 0.9623824451410659
# family level:         0.9925548589341693
# subfamily level:      0.9796238244514106
# sub-subfamily level:  0.9764890282131662


# corr_top_2000
# 0.9529780564263323
# family level:         0.9909874608150471
# subfamily level:      0.9710031347962382
# sub-subfamily level:  0.9655172413793104


# corr_top_1500
# 0.9561128526645768
# family level:         0.9941222570532915
# subfamily level:      0.9749216300940439
# sub-subfamily level:  0.9717868338557993

