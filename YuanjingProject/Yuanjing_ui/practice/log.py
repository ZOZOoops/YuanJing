# import logging
# from logging.handlers import RotatingFileHandler
# logging.basicConfig(level=logging.ERROR,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - [line:%(lineno)s]')
# logger = logging.getLogger('mainModule')
# logger.setLevel(level=logging.INFO)
# logger.critical('这是一条严重的信息，流程阻塞')
# logger.debug('这是DEBUG信息')
# logger.error('这是error信息')
#
# file_handler = logging.FileHandler('../Log/log.txt',mode='a',encoding='utf-8')
# file_handler.setLevel(logging.ERROR)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
# logger.error('重新进入程序')
#
#
import logging
import os
from logging.handlers import RotatingFileHandler
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)
print(os.getcwd())
rHandler = RotatingFileHandler('../Log/log.txt',mode='a',maxBytes=1024*1,backupCount=3)
rHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
rHandler.setFormatter(formatter)
logger.error('这就是error 内容')

# import logging
# logger = logging.getLogger()
# logger.setLevel(logging.ERROR)
# logger.setLevel(logging.ERROR)
# console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler('../Log/log.txt',mode='a',encoding='utf-8')
# file_fmt = '%(asctime)s - %(levelname)s - %(name)s - %(pathname)s'
# console_fmt = '%(asctime)s - %(name)s - %(pathname)s'
# fmt1 = logging.Formatter(fmt=file_fmt)
# fmt2 = logging.Formatter(fmt=console_fmt)
# console_handler.setFormatter(fmt2)
# file_handler.setFormatter(fmt1)
# file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s - %(name)s - %(pathname)s'))
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)
# logger.error('asdaasd')
# logger.error('真是打印的信息')
#
# def logger():
#     return logger