#回顾上基本都会——蓝桥杯练得太值了，python的基础语法特别扎实！！！！

# s = open('葫芦娃.txt', mode = 'a', encoding = 'utf-8')
# names = ['周杰伦', '张无忌', '娃哈哈']
# for name in names:
#     s.write(name + '\n')
# s.close()

# with open('葫芦娃.txt', mode = 'rb') as f1, \
#     open('葫芦娃2.txt', mode = 'wb') as f2:
#     content = f1.read()
#     f2.write(content)

import os
# # #创建文件的完整流程
#
# paths = './a/b/c/d.txt/e.txt'
# # #判断文件存不存在
# # print(os.path.exists(paths))
#
# # os.makedirs(paths)  #创建文件夹目录结构
# #获取某路径的文件夹
# print(os.path.dirname(paths))  #路径
# print(os.path.basename(paths))  #文件名
#
# #判断是否是文件夹
# print(os.path.isdir(paths))

#创建文件的完整流程：

# file_path = './ab/c/d/e.txt'
#
# #判断文件路径是否存在
# if not os.path.isdir(os.path.dirname(file_path)):
#     os.makedirs(os.path.dirname(file_path))
#
# open(file_path, mode = 'w', encoding = 'utf_8')

import json
s = '{"name": "汪峰", "age" : 18, "money" : null}'
dic = json.loads(s)
dic_json = json.dumps(dic, separators = (',', ':'))
dic_dic = json.loads(dic_json)
print(dic, dic_json, dic_dic, sep = '\n')



