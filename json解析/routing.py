# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import json

    
'''
读数据文件，返回为字符串。
'''
def readFile(path):
   with open(path,'r') as fp:
        data=fp.read()
        return data
      
'''
将文件保存为csv文件，文件名为'results1.csv
'''    
def savaData(results):
    df=pd.DataFrame(results)
    df.to_csv('./results1.csv')
    
'''
解析数据文件，提取经纬度坐标，返回一个字典列表。
'''
def getRoutesInfo(data):
    data = json.loads(data)
    steps_list = data['result']['routes'][0]['steps']
    step = steps_list[0]
    all_points = []
    for step in steps_list:     # 循环获取经纬度
        duration = step['duration']
        all_points.extend(getPointInfo(step))
    print(all_points)
    return all_points

def getPointInfo(step):
    points_list = []
    path_list = step['path'].split(';')
    for path in path_list:
        point = {}
        coords = path.split(',')
        lng = coords[0]         # 获取经度
        lat = coords[1]         # 获取纬度
        point['lat'] = lat      # 写入纬度
        point['lng'] = lng      # 写入经度
        points_list.append(point)
    return points_list





def main():
       path='./routing.json'
       try:
        data=readFile(path)
        result=getRoutesInfo(data)
        savaData(result)
       except:
          print('无法打开文件routing.json')
       
if __name__=='__main__':
    main()
    

    