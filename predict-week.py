
# coding: utf-8

# In[1]:



#周预测
import csv
import pandas as pd
import math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
from sklearn.svm import LinearSVR
from sklearn.ensemble import RandomForestRegressor

import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import time
import os
from sklearn.metrics import mean_squared_error #均方误差
from sklearn.metrics import mean_absolute_error #平方绝对误差
from sklearn.metrics import r2_score#R square


# In[2]:


#读取数据清单(此处已删除了文件夹里的DS_STORE文件)
file_path =u"G:\\software\\anaconda\\project\\demo\stockdata\\" #此处加u为了识别中文路径编码
stockdata_list = os.listdir(file_path)# os.listdir(file)会历遍文件夹内的文件并返回一个列表
stockdata_list.sort()# 对stockdata 文件夹中的数据进行升序排序


# In[3]:


#获取数据
filedata=[]
newfiledata=[]

for i in range(97):
    filedata.append(pd.read_csv(os.path.join(u"G:\\software\\anaconda\\project\\demo\stockdata\\", stockdata_list[i])))
    #构造5天平均volume列
    
    ave_volume=[]
    for j in range(len(filedata[i])-5):
        ave_volume.append(sum(filedata[i].loc[j+1:j+5]['volume'])/5)
    newfiledata.append(filedata[i].loc[0:len(filedata[i])-6]) #剔除了最前面的5天
    newfiledata[i]['ave_volume']=ave_volume


# In[70]:


#用前五天volume平均值做第六天close的预测
Result1=[]#用于存储预测的结果集

for i in range(97):
    #28分测试集、样本集
    #X = preprocessing.scale(newfiledata[i]['ave_volume'])
    #Y=newfiledata[i]['close']
    X_train=newfiledata[i].loc[0:int(0.8*len(newfiledata[i]))]['ave_volume']
    y_train=newfiledata[i].loc[0:int(0.8*len(newfiledata[i]))]['close']
    X_test=newfiledata[i].loc[int(0.8*len(newfiledata[i]))+1:]['ave_volume']
    y_test=newfiledata[i].loc[int(0.8*len(newfiledata[i]))+1:]['close']
    
    #线性回归
    clf = LinearRegression(n_jobs=-1)
    clf.fit(X_train.reshape(-1, 1), y_train.reshape(-1, 1) )
    y_predict= clf.predict(X_test.reshape(-1, 1))
    
    #支持向量机
    clf = LinearSVR()
    clf.fit(X_train.reshape(-1, 1), y_train.reshape(-1, 1) )
    y_predict_2= clf.predict(X_test.reshape(-1, 1))
    
    #随机森林
    clf = RandomForestRegressor(n_estimators =10)
    clf.fit(X_train.reshape(-1, 1), y_train.reshape(-1, 1) )
    y_predict_3= clf.predict(X_test.reshape(-1, 1))
    
    #将结果存入结果集
    new_y_predict=y_predict.reshape(1,-1)[0]#y_predict的数据形式与y_test不一样，需要变换
    date=newfiledata[i].loc[int(0.8*len(newfiledata[i]))+1:]['date']
    df=pd.DataFrame({'stock_num':i,'test':np.array(y_test),'predict':new_y_predict,'date':date}).ix[:,['stock_num','date','test','predict']]#创建第i只股票的结果集
    Result1.append(df)
    
    #查看预测结果拟合程度
    MSE=mean_squared_error(y_test,y_predict_3)
    MAE=mean_absolute_error(y_test,y_predict_3)
    R2=r2_score(y_test,y_predict_3)
    
    
    print('第' + str(i) + '只股票的预测结果MSE为'+str(MSE)+',MAE为'+str(MAE)+',R2为'+str(R2))


# In[71]:


pd.concat(Result1).to_csv('weekly_predict_Result.csv')


# In[65]:


plt.scatter(X_train.values,y_train.values,label='train')
plt.scatter(X_test.values,y_test.values,label='test')
plt.scatter(X_test.values,y_predict,label='LR_predict')
#plt.scatter(X_test.values,y_predict_2,label='SVR_predict')#支持向量机效果太差，在此隐去
plt.scatter(X_test.values,y_predict_3,label='RF_predict')
plt.legend(loc='best')
plt.xlabel('5pre_day_ave_volume')
plt.ylabel('6th_close')

