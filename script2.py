import pandas as pd
import numpy as np
filepath="/Users/vamshibobbili/Downloads/Toyota.csv"
data_set= pd.read_csv(filepath,index_col=0)
print(data_set.head())
print(data_set.isnull().sum())
data_set["Age"]=data_set["Age"].fillna(data_set["Age"].mean())
print(data_set.isnull().sum())
data_set.dropna(axis=0,inplace=True)
print(data_set.isnull().sum())
print(data_set.info())
data_set["Price"]=data_set["Price"].astype("Float32")
uniqueness=np.unique(data_set["KM"])
print(uniqueness)
data_set = data_set.drop(data_set[data_set['KM'] == '??'].index)
