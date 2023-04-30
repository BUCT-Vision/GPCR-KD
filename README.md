# GPCR-KD

这个代码是GPCR-KD方法的程序。

## 摘要

### 动机

由于新发现的和增量的大规模GPCRs的功能预测一直是生物学研究中的一个热点，大量基于机器学习的算法已经被开发出来用于G-蛋白偶联受体（GPCRs）的分类。 这些前期研究的高准确率揭示了提取有价值的特征和过滤掉冗余是决定整体准确率的关键挑战。为了得到一个更有效的模型，本研究进一步考虑了特征同义词的情况，提出了一种基于功能词聚类和整合的新方法。 该方法背后的本质是新颖的特征知识挖掘策略。与之前的研究不同，所提出的策略在提取的特征和分类器之间增加了一层，利用基于残余物替换矩阵的进化假设来评估每个候选特征的独立性，对候选特征进行聚类，并通过选择主要的功能词来整合它们。这些词是最终的特征，并被用来组成一个特征知识库。然后，GPCR序列被知识库转变成特征向量并被分类器使用。

### 结果

该研究对12,731个GPCR序列进行了分类。采用了四种经典的机器学习算法--奈夫贝叶斯算法（NB）、随机森林算法（SF）、支持向量机算法（SVM）和多层感知算法（MLP）--对所有GPCR等级进行分类。令人惊讶的是，新颖的特征知识挖掘策略帮助所有的分类器在所有的测试案例中都取得了显著的改善。 与之前使用相同数据集的方法相比，分类误差降低了。


### 用户指南
如果你是第一次使用这个程序，请下载代码并按如下操作。
###用户手册


1.	实施的先决条件

	操作系统：64位Win10

	软件环境：
        python 3.9 (https://www.python.org/getit/)  
	pycharm (https://www.jetbrains.com/pycharm/)

	其他第三方软件包： sklearn, numpy
        
	实验数据再data文件夹里，因为不是很大， 所以直接上传了方便复用。
        
	
 
            


请到相应的网站下载python 3.9和pycharm，并默认安装它们。如果没有安装第三方软件包，在导入的位置会报告一个错误。只需将鼠标移到顶部，点击安装相应的软件包，如下图（图1）。

![输入图片说明](https://images.gitee.com/uploads/images/2021/0906/183517_988cf9e9_7791951.png "1.png")
 
图1. 缺乏第三方软件包时的错误处理方法。

2.	实施的组成
实现的主要程序是seqToResult（图2），它实现了原始数据集的读取、特征提取、特征向量和标签（x, y）的生成、数据集的训练和预测。由于seqToResult的主要步骤占据了实现的大部分运行时间，为了减少时间成本，每次运行seqToResult时，核心的临时数据会被保存到一个文件中，即'data'。dataToResult（图2）可以使用'data'文件来进行快速预测。

![输入图片说明](https://images.gitee.com/uploads/images/2021/0906/183633_78481388_7791951.png "2.png")
 
图2. 程序结构布局。


3 .运行seqToResult
为了得到三级类别的预测结果，只需右击seqToResult文件夹中的main.py，并点击运行'main'，如图3。结果将被写入seqToResult目录下的result.txt文件。对于实验数据集，这个过程将需要12个小时。为了得到家庭层面的分类预测，只需右击value_of_family.py并点击运行'value_of_family'，你将得到家庭层面的准确性、召回率和F1_score。同样地，当运行value_of_subfamily时，你可以得到家族级别I类别的预测结果。对于dataToResult，程序是一样的，请注意，在运行dataToResult中的相关文件之前，你需要将'data'文件移到dataToResult文件夹中。

![输入图片说明](https://images.gitee.com/uploads/images/2021/0906/183648_d3a101bd_7791951.png "3.png")
 
图3.  运行seqToResult的方法

4 .用不同的机器学习算法运行分类器 

这四种算法被列在seqToResult和dataToResult的主文件中，只需在训练前选择一种算法。对于seqToResult，分类器选项包含在main.py第102行的classifier_factory中。你可以复制一个选项并粘贴到图4所示的 "CLF ="后面。
对于dataToResult，分类器选项包含在main.py第50行的 classifier_factory 中。其他操作与上述相同。

![输入图片说明](https://images.gitee.com/uploads/images/2021/0906/183658_0920b997_7791951.png "4.png")

![输入图片说明](https://images.gitee.com/uploads/images/2021/0906/183711_40ab79fb_7791951.png "44.png")
 
 
图4. 选择不同分类器的方法。

5.文件夹 "seqToResult "从头开始执行整个实验。文件夹 "dataToResult "使用文件夹 "seqToResult "产生的中间结果来完成实验，这样可以节省时间。文件夹 "dataToResult "中的 "Dimensionality reduction "实现了特征选择和降维，以达到更好的实验效果。



