import re


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

A_Aminergic = [0,0,0]
A_Peptide = [0,0,0]
A_Protein = [0,0,0]
A_Lipid = [0,0,0]
A_Orphan = [0,0,0]
A_Sensory = [0,0,0]
A_Nucleotide = [0,0,0]
A_Melatonin = [0,0,0]
A_Alicarboxylic = [0,0,0]
A_Steroid = [0,0,0]

C_Amino = [0,0,0]
C_Ion = [0,0,0]
C_Sensory = [0,0,0]
C_Orphan = [0,0,0]

B1 = [0,0,0]
B2 = [0,0,0]
F = [0,0,0]
Taste2 = [0,0,0]





A_Aminergic = [0,0,0]
A_Peptide = [0,0,0]
A_Protein = [0,0,0]
A_Lipid = [0,0,0]
A_Orphan = [0,0,0]
A_Sensory = [0,0,0]
A_Nucleotide = [0,0,0]
A_Melatonin = [0,0,0]
A_Alicarboxylic = [0,0,0]
A_Steroid = [0,0,0]




C_Amino = [0,0,0]
C_Ion = [0,0,0]
C_Sensory = [0,0,0]
C_Orphan = [0,0,0]

A_name = ["A_Aminergic","A_Peptide","A_Protein","A_Lipid","A_Orphan","A_Sensory","A_Nucleotide","A_Melatonin","A_Alicarboxylic","A_Steroid"]

C_name = ["C_Amino","C_Ion","C_Sensory","C_Orphan"]

B1 = [0,0,0]
B2 = [0,0,0]
F = [0,0,0]
Taste2 = [0,0,0]
#TP  FP  FN
with open("result_solved_Taste","r") as f:
    for row in f.readlines():
        sequ = row.strip("\n")
        t = re.split(r" +",sequ)

        if t[0] == t[2]:

            if t[0] == 'A':
                if t[1] == "Aminergic":
                    A_Aminergic[0]+=1
                elif t[1] == 'Peptide':
                    A_Peptide[0]+=1
                elif t[1] == 'Protein':
                    A_Protein[0]+=1
                elif t[1] == 'Lipid':
                    A_Lipid[0]+=1
                elif t[1] == 'Orphan':
                    A_Orphan[0]+=1
                elif t[1] == 'Sensory':
                    A_Sensory[0]+=1
                elif t[1] == 'Nucleotide':
                    A_Nucleotide[0]+=1
                elif t[1] == 'Melatonin':
                    A_Melatonin[0]+=1
                elif t[1] == 'Alicarboxylic':
                    A_Alicarboxylic[0]+=1
                else:
                    A_Steroid[0]+=1
                    #Steroid


            if t[0] == 'B1':
                B1[0] +=1

            if t[0] == 'B2':
                B2[0]+=1

            if t[0] == 'C':

                if t[1] == "Orphan":
                    C_Orphan[0]+=1
                elif t[1] == "Sensory":
                    C_Sensory[0]+=1
                elif t[1] == "Ion":
                    C_Ion[0] +=1
                else:
                    C_Amino[0]+=1



            if t[0] == 'Taste':
                Taste2[0]+=1

            if t[0] == 'F':
                F[0]+=1

        #当预测错误时，计算 FP FN
        if t[0] != t[2]:

            #FN 2
            if t[0] == 'A':
                if t[1] == "Aminergic":
                    A_Aminergic[2]+=1
                elif t[1] == 'Peptide':
                    A_Peptide[2]+=1
                elif t[1] == 'Protein':
                    A_Protein[2]+=1
                elif t[1] == 'Lipid':
                    A_Lipid[2]+=1
                elif t[1] == 'Orphan':
                    A_Orphan[2]+=1
                elif t[1] == 'Sensory':
                    A_Sensory[2]+=1
                elif t[1] == 'Nucleotide':
                    A_Nucleotide[2]+=1
                elif t[1] == 'Melatonin':
                    A_Melatonin[2]+=1
                elif t[1] == 'Alicarboxylic':
                    A_Alicarboxylic[2]+=1
                else:
                    A_Steroid[2]+=1

            if t[0] == 'B1':
                B1[2]+=1

            if t[0] == 'B2':
                B2[2]+=1

            if t[0] == 'C':

                if t[1] == "Orphan":
                    C_Orphan[2]+=1
                elif t[1] == "Sensory":
                    C_Sensory[2]+=1
                elif t[1] == "Ion":
                    C_Ion[2] +=1
                else:
                    C_Amino[2]+=1

            if t[0] == 'Taste':
                Taste2[2] +=1

            if t[0] == 'F':
                F[2] +=1



            # 计算FP ， 1
            if t[2] == 'A':
                if t[1] == "Aminergic":
                    A_Aminergic[1]+=1
                elif t[1] == 'Peptide':
                    A_Peptide[1]+=1
                elif t[1] == 'Protein':
                    A_Protein[1]+=1
                elif t[1] == 'Lipid':
                    A_Lipid[1]+=1
                elif t[1] == 'Orphan':
                    A_Orphan[1]+=1
                elif t[1] == 'Sensory':
                    A_Sensory[1]+=1
                elif t[1] == 'Nucleotide':
                    A_Nucleotide[1]+=1
                elif t[1] == 'Melatonin':
                    A_Melatonin[1]+=1
                elif t[1] == 'Alicarboxylic':
                    A_Alicarboxylic[1]+=1
                else:
                    A_Steroid[1]+=1

            if t[2] == 'B1':
                B1[1]+=1

            if t[2] == 'B2':
                B2[1]+=1

            if t[2] == 'C':
                if t[1] == "Orphan":
                    C_Orphan[1]+=1
                elif t[1] == "Sensory":
                    C_Sensory[1]+=1
                elif t[1] == "Ion":
                    C_Ion[1] +=1
                else:
                    C_Amino[1]+=1

            if t[2] == 'Taste':
                Taste2[1]+=1

            if t[2] == 'F':
                F[1]+=1


list_of_C = []
list_of_C.append(C_Amino)
list_of_C.append(C_Ion)
list_of_C.append(C_Sensory)
list_of_C.append(C_Orphan)

list_of_A = []
list_of_A.append(A_Aminergic)
list_of_A.append(A_Peptide)
list_of_A.append(A_Protein)
list_of_A.append(A_Lipid)
list_of_A.append(A_Orphan)
list_of_A.append(A_Sensory)
list_of_A.append(A_Nucleotide)
list_of_A.append(A_Melatonin)
list_of_A.append(A_Alicarboxylic)
list_of_A.append(A_Steroid)


# TP FP FN

# A

print("class","        ","TP"," ","FP"," ","FN"," ","pre"," ","recall"," ","F1_score")

for index in range(10):
    t = list_of_A[index]
    tp = t[0]
    fp = t[1]
    fn = t[2]
    pre = tp/(tp+fp)*100
    recall = tp/(tp+fn)*100
    f1_score = 2*pre*recall/(pre+recall)

    print(A_name[index], " ", tp, " ", fp, " ", fn, " ", pre, " ", recall, " ", f1_score)

# C
for index in range(4):
    t = list_of_C[index]
    tp = t[0]
    fp = t[1]
    fn = t[2]
    pre = tp/(tp+fp)*100
    recall = tp/(tp+fn)*100
    f1_score = 2*pre*recall/(pre+recall)

    print(C_name[index]," ",tp," ",fp," ",fn," ",pre," ",recall," ",f1_score)

# B1

pre = B1[0]/(B1[0]+B1[1])*100
recall = B1[0]/(B1[0]+B1[2])*100
F1_score = 2*pre*recall/(pre+recall)
print("B1"," ",B1[0]," ",B1[1]," ",B1[2]," ",pre," ",recall," ",F1_score)

# B2

pre = B2[0]/(B2[0]+B2[1])*100
recall = B2[0]/(B2[0]+B2[2])*100
F1_score = 2*pre*recall/(pre+recall)
print("B2"," ",B2[0]," ",B2[1]," ",B2[2]," ",pre," ",recall," ",F1_score)

# F

pre = F[0]/(F[0]+F[1])*100
recall = F[0]/(F[0]+F[2])*100
F1_score = 2*pre*recall/(pre+recall)
print("F"," ",F[0]," ",F[1]," ",F[2]," ",pre," ",recall," ",F1_score)

# Taste2

pre = Taste2[0]/(Taste2[0]+Taste2[1])*100
recall = Taste2[0]/(Taste2[0]+Taste2[2])*100
F1_score = 2*pre*recall/(pre+recall)
print("Taste2"," ",Taste2[0]," ",Taste2[1]," ",Taste2[2]," ",pre," ",recall," ",F1_score)

# 统计结果输出到控制台，复制到文件，再输入到Excel表格
with open("now_result.txt","w") as f:
    f.seek(0)
with open("result_solved_Taste","w") as f:
    f.seek(0)
