# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from bs4 import BeautifulSoup

'''
读数据文件，返回为字符串。
'''


def readFile(path):
    with open(path, 'r', encoding='utf-8') as fp:
        data = fp.read()
        return data


'''
将文件保存为csv文件，文件名为'results2.csv
'''


def savaData(results):
    df = pd.DataFrame(results)
    df.to_csv('./results2.csv')  # 此处不可修改


'''
解析数据文件，提取，返回一个字典列表。
'''


def getInfo(data):
    soup = BeautifulSoup(data, 'lxml')      # 使用BeautifulSoup解析获取到的数据
    result = []     # 创建字典列表
    for i in range(8, 296, 2):
        name = soup.find_all('td')[i].text      # 获取name
        description = soup.find_all('td')[i + 1].text       # 获取description
        dict = {'description': description, 'name': name}       # 创建字典，并将description和name插入字典
        result.append(dict)     # 将字典插入列表
    return result       # 输出字典列表


def main():
    path = './cve.html'  # 此处不可修改
    try:
        data = readFile(path)
        result = getInfo(data)
        savaData(result)
    except:
        print('无法打开文件cve.html')


if __name__ == '__main__':
    main()
