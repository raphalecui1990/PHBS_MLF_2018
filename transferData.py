import numpy as np
import pandas as pd
# 用pd导入xlsx数据
df = pd.DataFrame(pd.read_excel('20180926data(tab).xlsx'))
# print(df)

# 数据表清洗
# 用数字0填充空值
df.fillna(value=0)

#计算相对稳定：限售+高管持股/流通股  一季度
#df['first_holders_s1'] = df.apply(lambda x: x['RS_of_AS(10,000)'] + x['RS/EH(10,000)'], axis=1)
# print(df['first_holders_s1'])
#df['rational_stady_s1'] = df.apply(lambda x: x['first_holders_s1'] / x['CAS(10,000)'], axis=1)
#print("每一股对应的相对稳定结果：")
#print(df['rational_stady_s1'])

#计算一定性稳定:第一部分+国家持股+社保持股/流通股   一季度
#df['second_holders_s1'] = df.apply(lambda x: x['RS_of_AS(10,000)'] + x['RS/EH(10,000)']+x['first_holders_s1']
#                                             + x['RS/SH(10,000)'] + x['Total_stock_SS_S1(10,000)'], axis=1)
# print(df['second_holders_s1'])
#df['proper1_stady_s1'] = df.apply(lambda x: x['second_holders_s1'] / x['CAS(10,000)'], axis=1)
#print("每一股对应的定性稳定结果：")
#print(df['proper1_stady_s1'])


#计算全面性稳定:第二部分+其他基金/流通股   一季度
df['third_holders_s1'] = df.apply(lambda x: x['RS_of_AS(10,000)'] + x['RS/EH(10,000)']+x['first_holders_s1']
                     + x['RS/SH(10,000)'] + x['Total_stock_SS_S1(10,000)'] + x['Total_stock_Other_S1(10,000)'], axis=1)
print(df['second_holders_s1'])
df['proper2_stady_s1'] = df.apply(lambda x: x['third_holders_s1'] / x['CAS(10,000)'], axis=1)
print("每一股对应的全面性稳定结果：")
print(df['proper2_stady_s1'])

df.to_csv('transferData.csv')


