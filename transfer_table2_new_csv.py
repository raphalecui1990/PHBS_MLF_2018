import csv
import quandl
import pandas as pd
# cross_validation 0.2开始废除
import math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import time

df = pd.read_csv('000001.csv')
df1 = pd.read_csv('transferData.csv')
# outfile = pd.merge(df1, df, how='left', left_on='Code',right_on='date')
# outfile.to_csv('outfile.csv')

# # 将transferData.csv 中的计算相对稳定性：rational_stady_s1中的第一个值取出，即平安银行那一股的相对稳定性值取出
# table1_out = df1.loc[0][211]
# #print(df1.astype)
#
# # 在0000001.csv 文件中将 volume_new 一列 加上 （rational_stady_s1中的第一个值取出，即平安银行那一股的相对稳定性值）得到一个新的 Volume_new值
# df['volume_new'] = df.apply(lambda x: x['volume'] +table1_out, axis=1)
# print(df)

# 
i = 0
while i < 99:
    talbe_1_out = df1.loc[i][211]
    # print(talbe_1_out)

    # 将transferData.csv中计算相对稳定性的列： rational_stady_s1 中的每一个值 依次取出 分别依次与 0000001.csv 文件中
    #  volume列 的每个元素相加，生成一组新的列，形如 volume_new_0,volume_new_1,...,volume_new_98
    volume_name = "volume_new_" + str(i)
    df[volume_name] = df.apply(lambda x: x['volume'] + talbe_1_out, axis=1)
    i += 1
    # print(df)
# 将计算出的结果以new_000001.csv 文件格式保存
outfile = pd.merge(df, df1, how='left', left_on='date',right_on='Code')
outfile.to_csv('new_000001.csv')





