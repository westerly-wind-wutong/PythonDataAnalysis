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
    soup = BeautifulSoup(data, 'lxml')
    result = []
    # for i in range(8,154,2):            # 2021年
    for i in range(8, 296, 2):  # 包括2020年
        name = soup.find_all('td')[i].text
        description = soup.find_all('td')[i + 1].text
        dict = {'description': description, 'name': name}
        result.append(dict)
    return result


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
