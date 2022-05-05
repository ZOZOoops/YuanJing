# import re
#
# for letter in "python":
#     print("当前字母：%s"  % letter)
# fruits = ['apple','banana']
# for fruit in fruits:
#     print('%s' % fruit)
# for letter in 'pyhton':
#     print('当前输入的字符：%s' % letter)
# emp1 = ('zara',1000)
# print(emp1)
# class People(object):
#
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def QuXiFu(self):
#         print('%s %d %s 开车去娶媳妇' %  (self.name,self.age,self.gender))
#
#     def GoHome(self):
#         print('%s %d %s 回家' %  (self.name,self.age,self.gender))
#
# laoli  = People('老李',40,'男')
# zhangsan = People('张三',20,'男')
#
# laoli.QuXiFu()
# zhangsan.GoHome()
import unittest

money = 1000
s = int(input('请输入你的金额:'))
#进行判断
if money > s:
    money -= s
else:
    print('当前余额不足')
print('当前余额: %d' %money)

