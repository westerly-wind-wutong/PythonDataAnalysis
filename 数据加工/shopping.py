# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
    
'''
读数据文件，返回为字符串。
'''
def readFile(path):
   data=pd.read_csv(path,engine='python',encoding='gbk')
   return data


def saveData(df1,df2,df3,df4):
    df1.to_csv('./results3.csv',encoding='gbk')  #此处不可修改
    df2.to_csv('./results4.csv',encoding='gbk')  #此处不可修改
    df3.to_csv('./results5.csv',encoding='gbk')  #此处不可修改
    df4.to_csv('./results6.csv',encoding='gbk')  #此处不可修改
    
'''
task1 数据预处理
'''
def task1(df):
    df = df.dropna(axis=0, how='any')               # 处理缺失值
    df['销售日期'] = pd.to_datetime(df['销售日期'], format='%Y%m%d', errors='coerce')   # 销售日期设置为datetime格式
    df = df.dropna(axis=0, how='any')               # 删除日期异常的值
    df = df[df['销售数量'] > 0]             # 删除销售数量和销售金额为负的数值
    # df = df[df['销售金额'] > 0]             # 执行后与题图不符
    return df.describe(),df

'''
Task2根据大类名称，统计每个大类商品的销售总额
'''
def task2(df):
    df2 = df.groupby('大类名称')['销售金额'].sum()      # 过于简单，不做注释
    return df2
'''
Task3统计每个中类商品的促销销售金额和非促销总销售额
'''
def task3(df):
    df_promotional = df[df['是否促销'] == '是'].groupby('中类名称')['销售金额'].sum()    # 统计每个中类商品的促销销售金额
    df_promotional.name = '促销总销售额'      # 修改列名称
    df_Non_promotional = df[df['是否促销'] == '否'].groupby('中类名称')['销售金额'].sum()    # 统计每个中类商品的非促销总销售额
    df_Non_promotional.name = '非促销总销售额'     # 修改列名称
    df3 = pd.merge(df_promotional, df_Non_promotional, left_on='中类名称', right_on='中类名称')     # 结果合并
    return df3
    
    
'''
Task4 统计4月总计消费金额前20的顾客，并显示其销售金额和消费次数
'''
def task4(df):
    df_201504 = df[df['销售月份'] == 201504]    # 提取2015年4月的数据
    df_201504_sum = df_201504.groupby('顾客编号')['销售金额'].sum()   # 统计金额
    df_201504_sum.name = '销售金额'       # 修改列名称
    df_201504_count = df_201504.groupby('顾客编号')['销售金额'].count()     # 统计销售次数
    df_201504_count.name = '销售次数'       # 修改列名称
    df_201504_sum_count = pd.merge(df_201504_sum, df_201504_count, left_on='顾客编号', right_on='顾客编号')  # 合并结果
    df_201504_sum_count_Sorting = df_201504_sum_count.sort_values(by='销售金额', ascending=False)     # 按'销售金额'排序
    df4 = df_201504_sum_count_Sorting[0:20]     # 选择前20
    return df4

def main():
       path='./超市购物.csv'  #此处不可修改
       try:
           data=readFile(path)
           df1,data=task1(data)
           df2=task2(data)
           df3=task3(data)
           df4=task4(data)
           saveData(df1,df2,df3,df4)
       except:
           pass
                 
if __name__=='__main__':
    main()
    
    

    