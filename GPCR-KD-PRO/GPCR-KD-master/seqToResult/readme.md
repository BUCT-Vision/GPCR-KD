
#说明

1.程序构成
主要分为 seqToResult 和 dataToResult 两部分。
seqToResult 包括 读取原始数据，提取特征，生成特征向量及标签（x,y）,训练,预测所有过程。
其中根据提取的特征生成特征向量及标签占据了程序运行的绝大部分时间，为减少每次运行的时间，把生成的x,y及对应的类名称保存到data文件中。
dataToResult 部分，在main函数直接读取gds_data保存的x,y及对应的类名称,接下来和 seqToResult 部分一致。

2.程序运行
运行seqToResult的main，预测结果会写入result.txt文件中，可将生成的data文件复制到 dataToResult  中，命名为 gds_data。
seqToResult的main中的analysize.main(test_num)分析各个级别的精度，并写入result.txt文件
然后运行value_of_family,得到6个family的准确度，召回率和F1_score,运行value_of_subfamily,得到6个family的18个subfamily的准确度，召回率和F1_score
dataToResult 部分，在main函数直接读取gds_data保存的x,y及对应的类名称,接下来和 seqToResult 部分一致。
四种分类器的选择在seqToResult的main中的classifier_factory(classifier_name)列出，在训练时可以自己选择。

3.结果的偏差
训练具有随机性，每次训练结果会有差异，对于序列较少的类较明显。

