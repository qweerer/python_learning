# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False    # 步骤二（解决坐标轴负数的负号显示问题）
# sns.set_style("ticks", {"font.sans-serif": ['simhei', 'Droid Sans Fallback']})
# os.chdir('D:\\code\\2018spyder\\项目12中国城市资本流动问题探索')
os.chdir('D:\\user\\Documents\\00code\\2018spyder\\项目12中国城市资本流动问题探索')
print('导入模块成功')
# %%
data = pd.read_excel('data.xlsx', sheet_name='Sheet1')
dataCol = data.columns.tolist()
# %%Q1
dataQ11Sam = data[data['投资方所在城市'] == data['融资方所在城市']]
dataQ11Dif = data[data['投资方所在城市'] != data['融资方所在城市']]
dataQ11Sam = dataQ11Sam.groupby(['投资方所在城市', '融资方所在城市', '年份']).sum().reset_index()
dataQ11Dif = dataQ11Dif.groupby(['投资方所在城市', '融资方所在城市', '年份']).sum().reset_index()

# %%Q1.1图的数据
dataQ11SamTu = dataQ11Sam[['投资方所在城市', '融资方所在城市', '投资企业对数']].groupby(['投资方所在城市', '融资方所在城市']).sum().sort_values('投资企业对数', ascending=False).head(20)
dataQ11DifTu = dataQ11Dif[['投资方所在城市', '融资方所在城市', '投资企业对数']].groupby(['投资方所在城市', '融资方所在城市']).sum().sort_values('投资企业对数', ascending=False).head(20)
print('投资方，融资方同城TOP20为：\n', dataQ11SamTu)
print('投资方，融资方异城TOP20为：\n', dataQ11DifTu)
# %%Q1.1图
figQ1 = plt.figure(figsize=(16, 15))
plt.subplots_adjust(hspace=0.3)

ax1 = figQ1.add_subplot(2, 1, 1)
dataQ11SamTu.plot(kind='bar', ax=ax1,
                  facecolor='yellowgreen', alpha=0.8,
                  edgecolor='black', linewidth=2)
plt.grid(linestyle='--', linewidth=1, axis='y', alpha=0.5)
ax1.legend(loc='best', fontsize='xx-large')
plt.title('同城投资')


ax2 = figQ1.add_subplot(2, 1, 2)
dataQ11DifTu.plot(kind='bar', ax=ax2,
                  facecolor='lightskyblue', alpha=0.8,
                  edgecolor='black', linewidth=2)
plt.grid(linestyle='--', linewidth=1, axis='y', alpha=0.5)
ax2.legend(loc='best', fontsize='xx-large')
plt.title('异地投资')


# %%Q1.2图的数据

figQ1 = plt.figure(figsize=(14, 20))
plt.subplots_adjust(hspace=0.5)

x = 0
for i, j in dataQ11Dif.groupby('年份'):
    x = x + 2
    j = j.sort_values('投资企业对数', ascending=False).head(20)
    j.index = j['投资方所在城市'] + '-' + j['融资方所在城市']
    ax1 = figQ1.add_subplot(4, 2, x)
    j['投资企业对数'].plot(kind='bar', ax=ax1,
                          facecolor='yellowgreen', alpha=0.8,
                          edgecolor='black', linewidth=2)
    plt.grid(linestyle='--', linewidth=1, axis='y', alpha=0.5)
    ax1.legend(loc='best')
    plt.title('异城投资_%i' % i)

x = -1
for i, j in dataQ11Sam.groupby('年份'):
    x = x + 2
    j = j.sort_values('投资企业对数', ascending=False).head(20)
    j.index = j['投资方所在城市']
    ax1 = figQ1.add_subplot(4, 2, x)
    j['投资企业对数'].plot(kind='bar', ax=ax1,
                          facecolor='lightskyblue', alpha=0.8,
                          edgecolor='black', linewidth=2)
    plt.grid(linestyle='--', linewidth=1, axis='y', alpha=0.5)
    ax1.legend(loc='best')
    plt.title('同城投资_%i' % i)
del i, j, x
# %%Q1.1删除
del dataQ11SamTu, dataQ11DifTu, dataQ11Sam
# %%Q2.1
dataCity = pd.read_excel('中国城市代码对照表.xlsx', sheet_name='Sheet1')
dataQ2 = dataQ11Dif[['投资方所在城市', '融资方所在城市', '投资企业对数']].groupby(['投资方所在城市', '融资方所在城市']).sum()
dataQ2 = dataQ2.reset_index()

dataQ2 = pd.merge(dataQ2, dataCity[['城市名称', '经度', '纬度']], left_on='投资方所在城市', right_on='城市名称')
del dataQ2['城市名称']
dataQ2.rename(columns={'经度': 'tzLng', '纬度': 'tzLat'}, inplace=True)

dataQ2 = pd.merge(dataQ2, dataCity[['城市名称', '经度', '纬度']], left_on='融资方所在城市', right_on='城市名称').sort_values('投资企业对数', ascending=False)
del dataQ2['城市名称']
dataQ2.rename(columns={'经度': 'rzLng', '纬度': 'rzLat'}, inplace=True)
# %%Q2.2
dataQ22 = dataQ11Dif[['投资方所在城市', '融资方所在城市', '投资企业对数']].copy()
dataQ22.columns = ['source', 'target', 'weight']
dataQ22['weight'] = (dataQ22['weight'] - dataQ22['weight'].min()) / (dataQ22['weight'].max() - dataQ22['weight'].min())
dataQ22.to_csv('./输出/Q22Line.csv', index=0, encoding='utf_8')

dataQ22Point = dataQ22[['source', 'weight']].groupby('source').sum().sort_values('weight', ascending=False)
dataQ22Point = dataQ22Point.reset_index()
dataQ22Point.columns = ['Id', 'Label']
dataQ22Point['Label'] = dataQ22Point['Id']
dataQ22Point['Label'][20:] = np.nan
dataQ22Point.to_csv('./输出/Q22Point.csv', index=0, encoding='utf_8')

dataQ2.to_csv('./输出/Q22Qgis.csv', index=0, encoding='utf_8')
# %%Q2删除
del dataQ22, dataQ22Point
# %%Q3 过去4年投资数与融资数城市的top10
dataQ3Stake = dataQ11Dif[['投资方所在城市', '投资企业对数']].groupby('投资方所在城市').sum().sort_values('投资企业对数', ascending=False).reset_index()[:10]
dataQ3Attract = dataQ11Dif[['融资方所在城市', '投资企业对数']].groupby('融资方所在城市').sum().sort_values('投资企业对数', ascending=False).reset_index()[:10]
dataQ3Stake.columns = ['A', 'value']
dataQ3Attract.columns = ['A', 'value']

dataQ3List = pd.concat([dataQ3Stake, dataQ3Attract])
dataQ3List = dataQ3List.groupby('A').count()

dataQ3 = pd.merge(dataQ3List, dataQ2, left_on='A', right_on='投资方所在城市', how='outer')
dataQ3 = pd.merge(dataQ3List, dataQ3, left_on='A', right_on='融资方所在城市', how='outer')
dataQ3 = dataQ3[(dataQ3['value_x'] > 0) | (dataQ3['value_y'] > 0)]
del dataQ3['value_x'], dataQ3['value_y']
print('投资数Top10为：', dataQ3Stake)
print('融资数Top10为：', dataQ3Stake)

# %%
dataQ3Stake.index = dataQ3Stake['A']
dataQ3Stake.index.name = ''
dataQ3Attract.index = dataQ3Attract['A']
dataQ3Attract.index.name = ''

figQ31 = plt.figure(figsize=(8, 7))
plt.subplots_adjust(hspace=0.3)

ax1 = figQ31.add_subplot(2, 1, 1)
dataQ3Stake['value'].plot(kind='bar', ax=ax1, rot=0,
                          facecolor='yellowgreen', alpha=0.8,
                          edgecolor='black', linewidth=2)
plt.grid(linestyle='--', linewidth=1, axis='y', alpha=0.5)
plt.title('投资方所在城市')


ax2 = figQ31.add_subplot(2, 1, 2)
dataQ3Attract['value'].plot(kind='bar', ax=ax2, rot=0,
                            facecolor='lightskyblue', alpha=0.8,
                            edgecolor='black', linewidth=2)
plt.grid(linestyle='--', linewidth=1, axis='y', alpha=0.5)
plt.title('融资方所在城市')
# %%
del dataQ3Attract, dataQ3Stake, dataQ3List
# %%Q3.2
dataQ3 = pd.DataFrame()
for i, j in dataQ11Dif.groupby('融资方所在城市'):
    for x, y in j.groupby('年份'):
        z = y[y['投资企业对数'] == y['投资企业对数'].max()].copy()
        z = z.drop_duplicates(subset=['年份'], keep='first')  # 可能有两个城市投资数相同，这里选择第一个投资的
        if z['投资方所在城市'].iloc[0] in ['北京', '深圳', '上海']:
            z['阵营'] = 1
        else:
            z['阵营'] = 0
        dataQ3 = pd.concat([dataQ3, z])
    print(i)


dataQ3Pic = pd.DataFrame()
for i, j in dataQ3.groupby('年份'):
    z = j[['阵营', '年份']].groupby('阵营').count().T
    z.rename(columns={1: '北上深阵营数量', 0: '非北上深阵营数量'}, inplace=True)
    z['年份'] = i
    dataQ3Pic = pd.concat([dataQ3Pic, z])

dataQ3Pic.index = dataQ3Pic['年份']
dataQ3Pic['北上深阵营占比'] = dataQ3Pic['北上深阵营数量'] / (dataQ3Pic['北上深阵营数量'] + dataQ3Pic['非北上深阵营数量'])
del i, j, x, y, z, dataQ3Pic['年份']
print(dataQ3Pic)
dataQ3Pic.index = dataQ3Pic.index.astype(str)
# %%
figQ32 = plt.figure(figsize=(10, 5))

ax1 = figQ32.add_subplot(1, 1, 1)
dataQ3Pic[['北上深阵营数量', '非北上深阵营数量']].plot(kind='bar', stacked=True,
                                        colormap='Blues_r', edgecolor='black', linewidth=2,
                                        ax=ax1)
dataQ3Pic['北上深阵营占比'].plot(secondary_y=True,
                          style='--o', color='orange',
                          rot=0, ax=ax1, legend=True)
plt.grid(linestyle='--', linewidth=1, axis='y', alpha=0.5, color='black')

# %%Q3.3

dataQ3 = pd.merge(dataQ3, dataCity[['城市名称', '经度', '纬度']], left_on='融资方所在城市', right_on='城市名称')
del dataQ3['城市名称']
dataQ3.rename(columns={'经度': 'rzLng', '纬度': 'rzLat'}, inplace=True)

# %%
dataQ3[dataQ3['年份'] == 2013].to_csv('./输出/Q33Year2013.csv', index=0, encoding='utf_8')
dataQ3[dataQ3['年份'] == 2014].to_csv('./输出/Q33Year2014.csv', index=0, encoding='utf_8')
dataQ3[dataQ3['年份'] == 2015].to_csv('./输出/Q33Year2015.csv', index=0, encoding='utf_8')
dataQ3[dataQ3['年份'] == 2016].to_csv('./输出/Q33Year2016.csv', index=0, encoding='utf_8')
