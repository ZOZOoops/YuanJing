# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("zzzz"+self.name)
# p1 = Person("bill",13)
# p1.myfunc()
# p1.age = 20 #使用关键字删除对象的属性
# del p1
# # class Person:
# #     pass
# # #创建子类，要创建从其他类继承功能的类，请在创建子类时将父类作为参数发送
# # class Student(person):
# #     pass
# mytuple = ('apple','banana','orange')
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# mytuple = ("apple",'banana')
# myit = iter(mytuple)
# #iter 方法的作用相似，您可以执行操作（初始化等），但必须始终返回迭代器本身
# #next 方法也允许执行操作，但必须返回序列中的下一个项目
# my = (       '11111','apple','ban','orange')
# for i in my:
#     print(i)
# a = 'banana'
# for i in a :
#     print(i)
#
# def myfunc():
#     x = 100
#     print(x)
# myfunc()
# print(x)
# def myfunc():
#     x = 100
#     def myinnerfunc():
#         print(x)
#         myinnerfunc()
# myfunc()
# #如果您需要创建一个全局变量，但被卡在本地作用域内，则可以使用global变量
# #关键字
# print(len(my))
# dict = {'brand':'porsche'}
# for i in dict:
#     print(i)
# print(len(i))
# thisdict = {
#     'brand':'Porsche',
#     'model':'911'
# }
# thisdict =	{
#   "brand": "Porsche",
#   "model": "911",
#   "year": 1963
# }
# del thisdict
# print(dict)
# fruits = ['apple','banana','cherry']
# for i in fruits:
#     if i == 'banana':
#         break
#     print(i)
# for x in range(2,10):
#     print(x)
# else:
#     print('打印完成之后，任务结束')

#函数默认将序列递增1，但是可以通过添加第三个参数来指定增量
def myfunction(name):
    print(name+'阿里')
myfunction('111  333')
def my_function(country = 'china'):
    print('i am from '+ country)
my_function()
my_function('india')
def my_function(aaa):
    for x in aaa:
        print(x)
fruits = ['apple','banana','cherry']
my_function(fruits)
price = 1
txt = 'The price is {} dollars'
print(txt.format(price))
#如需写入已有的文件，必须向open（）函数添加参数
import os
if os.path.exists('demofile.txt'):
    os.remove('demofile.txt')
else:
    print('The file does not exist')
import os
def myfunction():
import os
os.remove('demofile.txt')
import time
from time import thread_time
