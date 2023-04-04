import pandas as pd


data = pd.read_csv("data.csv")
feas = data.corr()['target'].abs().sort_values(ascending=False)

feas.drop('target',axis=0,inplace=True)
feas.to_csv("top800feas.csv")
print(feas.index)

data1 = data[feas.index]
data1.to_csv("with_corr.csv",index=False)