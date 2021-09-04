

# 1. 每行按两级分割为两组
import re

with open("result.txt","r") as f:
    for row in f.readlines():
        sequ = row.strip("\n")
        if sequ.__contains__(','):
            strings = sequ.split(",")
            str1 = strings[0].split(" ")
            str2 = strings[1].split(" ")
            class1 = str1[1]
            class11 = str1[2].split("_")[1]
            class2 = str2[2]
            class22 = str2[3].split("_")[1]
            with open("now_result.txt","a") as ff:
                if class1=="2_Sensory":
                    print("Taste 2  Sensory",file=ff,end=" ")
                else:
                    print(class1,"  ",class11,file=ff,end=" ")

                if class2=="2_Sensory":
                    print("Taste 2  Sensory",file=ff,end="\n")
                else:
                    print(class2,"  ",class22,file=ff,end="\n")


# 2. 去掉 "taste 2"之间的空格

classes = set()
with open("now_result.txt","r") as f:
    for row in f.readlines():
        sequ = row.strip("\n")
        t = re.split(r" +",sequ)
        with open("result_solved_Taste","a") as ff:

            if len(t)==5:
                for i in range(5):
                    if t[i]!='2':
                        ff.write(t[i])
                        ff.write("  ")
                ff.write("\n")

            elif len(t) ==6:
                for i in range(6):
                    if t[i]!='2':
                        ff.write(t[i])
                        ff.write("  ")
                ff.write("\n")

            else:
                ff.write(sequ)
                ff.write("\n")





# 3. 各个类的数量  TP FP FN

record_of_classes = dict()
record_of_tp = dict()
record_of_fp = dict()
record_of_fn = dict()

with open("result_solved_Taste","r") as f:
    for row in f.readlines():
        sequ = row.strip("\n")
        t = re.split(r" +",sequ)
        class_name = t[0]
        if record_of_classes.keys().__contains__(class_name) == False:
            record_of_classes[class_name] = 1
        else:
            record_of_classes[class_name] += 1
        if t[0]==t[2]: # 主要由相等与否判断
            key = t[0]
            if record_of_tp.keys().__contains__(key) == False:
                record_of_tp[key] = 1
            else:
                record_of_tp[key] +=1
        else:
            key_fp = t[2]
            if record_of_fp.keys().__contains__(key_fp) == False:
                record_of_fp[key_fp] = 1
            else:
                record_of_fp[key_fp] +=1


            key_fn = t[0]
            if record_of_fn.keys().__contains__(key_fn) == False:
                record_of_fn[key_fn] = 1
            else:
                record_of_fn[key_fn] +=1

# print(record_of_tp)
# print(record_of_fp)
# print(record_of_fn)


# {'A': 2009, 'B1': 150, 'C': 207, 'Taste': 118, 'B2': 34, 'F': 8}  TP
# {'C': 6, 'A': 9,  'Taste': 9, 'B1': 1}  FP
# {'A': 17, 'Taste': 4,  'F': 1, 'B1': 2, 'C': 1}  FN
#->
# {'A': 2009, 'B1': 150, 'C': 207, 'Taste': 118, 'B2': 34, 'F': 8}  TP
# { 'A': 9, 'B1': 1,'C': 6,'Taste': 9, 'B2': 0, 'F': 0 }  FP
# {'A': 17,'B1': 2, 'C': 1,'Taste': 4, 'B2': 0, 'F': 1 }  FN


# 4. 各个类的pre，recall，F1_score

#pre = TP/(TP+FP)  recall = TP/(TP+FN)  F1_score = 2*pre*recall / (pre+recall)

dic_tp = {'A': 2009, 'B1': 150, 'C': 207, 'Taste': 118, 'B2': 34, 'F': 8}
dic_fp = { 'A': 9, 'B1': 1,'C': 6,'Taste': 9, 'B2': 0, 'F': 0 }
dic_fn = {'A': 17,'B1': 2, 'C': 1,'Taste': 4, 'B2': 0, 'F': 1 }

strs_of_key = ['A','B1','C','Taste','B2','F']

print("class"," ","TP"," ","FP"," ","FN"," ","pre"," ","recall"," ","F1_score")

for index in range(6):
    key = strs_of_key[index]
    if record_of_tp.keys().__contains__(key):
        tp = record_of_tp[key]
    else:
        tp = 0

    if record_of_fp.keys().__contains__(key):
        fp = record_of_fp[key]
    else:
        fp = 0

    if record_of_fn.keys().__contains__(key):
        fn = record_of_fn[key]
    else:
        fn = 0
    # tp = dic_tp[key]
    # fp = dic_fp[key]
    # fn = dic_fn[key]
    pre = tp/(tp+fp)*100
    recall = tp/(tp+fn)*100
    F1_score = 2*pre*recall/(pre+recall)

    print(key," ",tp," ",fp," ",fn," ","%.2f"%pre," ","%.2f"%recall," ","%.2f"%F1_score)




# A   2009   9   17   99.55   99.16   99.36
# B1   150   1   2   99.34   98.68   99.01
# C   207   6   1   97.18   99.52   98.34
# Taste   118   9   4   92.91   96.72   94.78
# B2   34   0   0   100.00   100.00   100.00
# F   8   0   1   100.00   88.89   94.12

with open("now_result.txt","w") as f:
    f.seek(0)
with open("result_solved_Taste","w") as f:
    f.seek(0)

