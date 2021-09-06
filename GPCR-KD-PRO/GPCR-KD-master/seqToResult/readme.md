### User Manual


1.	Implementation Prerequisites

	OS: 64-bit Win10

	Software Environment：
        python 3.9  (https://www.python.org/getit/)  
	pycharm   (https://www.jetbrains.com/pycharm/)

	Additional third-party packages: sklearn, numpy


            


Please go to the corresponding websites to download python 3.9 and pycharm, and install them by default. If the third-party packages are not installed, an error will be reported at the location of the import. Simply move the mouse to the top and click to install the corresponding package as below (Fig.1).

![输入图片说明](https://images.gitee.com/uploads/images/2021/0906/183517_988cf9e9_7791951.png "1.png")
 
Fig.1. Error handing method when lack of third-party packages.

2.	The composition of the Implementation
The main program of the implementation is seqToResult (Fig. 2), which realizes the reading of original data sets, feature extraction, generation of feature vectors and labels (x, y), training and predicting of data sets. Since the major steps in seqToResult take up most of the running time of the implementation, in order to reduce the time cost, each time we run seqToResult,  the core temporary data will be saved into a file, namely ‘data’. The ‘data’ file can be used by dataToResult (Fig.2) for a quick prediction.

![输入图片说明](https://images.gitee.com/uploads/images/2021/0906/183633_78481388_7791951.png "2.png")
 
Fig.2. The program structure layout.


3 .Run seqToResult
For getting the predictions of level III categories, just right click main.py in seqToResult folder and click Run ‘main’ as Fig.3. The results will be written into result.txt file in the directory of the seqToResult. For the experimental data set, the process will take 12 hours. For getting the predictions of family level categories, just right click value_of_family.py and click Run ‘value_of_family’, you will get the accuracy, recall and F1_score of family level. Similarly, you can get the predictions of family level I categories when running value_of_subfamily. For dataToResult, the procedures is the same, please note that you need to move the ‘data’ file to dataToResult folder before running the relevant files in dataToResult.

![输入图片说明](https://images.gitee.com/uploads/images/2021/0906/183648_d3a101bd_7791951.png "3.png")
 
Fig.3.  The method of running seqToResult

4 .Run the classifier with different machine learning algorithms 

The four algorithms are listed in main files in seqToResult and dataToResult, simply select one before training. For seqToResult, the classifier options are included in classifier_factory in line 102 of main.py. you can copy a option and paste it behind "CLF =" shown in Fig.4. 
For dataToResult, the classifier options are included in classifier_factory in line 50 of main.py. The other operations are the same as above.

![输入图片说明](https://images.gitee.com/uploads/images/2021/0906/183658_0920b997_7791951.png "4.png")

![输入图片说明](https://images.gitee.com/uploads/images/2021/0906/183711_40ab79fb_7791951.png "44.png")
 
 
Fig.4. The method of choosing different classifiers.



