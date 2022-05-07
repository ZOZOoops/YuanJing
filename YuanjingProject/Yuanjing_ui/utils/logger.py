#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import datetime
import logging
import os
import time


class Log:
    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            # 创建一个handle写入文件
            _time = time.strftime('%Y-%m-%d_%H：%M：%S')
            # file_handler = logging.FileHandler(filename='../test_log/' + _time + '-log.txt',mode='a',encoding='utf-8')
            file_handler = logging.FileHandler(filename='../test_log/test_log.txt',mode='a')
            file_handler.setLevel(logging.ERROR)
            self.logger.addHandler(file_handler)


            # 创建一个handle输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)


            # 定义输出的格式
            formatter = logging.Formatter(self.fmt)
            file_handler.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 添加到handler到logger
            self.logger.addHandler(file_handler)
            self.logger.addHandler(ch)

    @property
    def fmt(self):
        return '%(levelname)s - %(asctime)s - [%(filename)s:%(lineno)d] - %(message)s'

log = Log().logger
