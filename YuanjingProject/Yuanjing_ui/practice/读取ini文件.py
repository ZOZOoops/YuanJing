# import os
#
# with open('../Data/data.ini',encoding='utf-8') as f:
#     # line = f.readline()
#     # while line != '':
#     #     print(line)
#     #     line = f.readline()
#     lines = f.readlines()
#     for line in lines:
#         print(line.lstrip())
# import os
# print(os.getcwd())
# list_dir = os.listdir('D:\project')
# print(list_dir)
# print(os.path.abspath(''))
# print(os.path.split('D:\project')) # 分离当前路径和文件为两部分，返回元组类型
# print(os.path.exists('D:\project')) # 判断当前path是否存在
# print(os.path.isdir('D:\project')) # 判断当前目录是否为目录
# with open('D:\project') as f:
#     f.write('D:\project')
# print(f.tell())
import os

path1 = os.path.dirname(__file__)
print(path1)
path2 = os.path.abspath(__file__)
print(path2)
path3 = os.path.dirname(os.path.abspath(__file__))
print(path3)
path4 = os.path.join(os.path.dirname(os.path.abspath(__file__)),'test001.py')
print(path4)
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.dirname(__file__))
