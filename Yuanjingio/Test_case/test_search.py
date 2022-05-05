#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
from utils.logger import log
from common.readconfig import ini
from page_object.searchpage import SearchPage


class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_baidu(self, drivers):
        """打开百度"""
        search = SearchPage(drivers)
        search.get_url(ini.url)

    def test_001(self, drivers):
        """搜索"""
        search = SearchPage(drivers)
        search.input_search("selenium")
        search.click_search()
        result = re.search(r'selenium', search.get_source)
        log.info(result)
        assert result

    def test_002(self, drivers):
        """测试搜索候选"""
        search = SearchPage(drivers)
        search.input_search("selenium")
        log.info(list(search.imagine))
        assert all(["selenium" in i for i in search.imagine])


if __name__ == '__main__':
    pytest.main(['TestCase/test_search.py'])


'''
===================================
页面元素定位
===================================
// 账号输入框 name="domainAccount"
// 密码输入框 name="password"
// 登录按钮 class="sso-btn-submit"
// 跳转到选择团队登录界面==>选择团队
// 选择团队 //*[@id="App"]/div/div/div[2]/div/div[4]/div/p/span[2]
        (//*[class="tenantselect-publicAccount-name"]/span[2])
//点击提交按钮 //*[@class="kuma-button kuma-button-primary"]/span
//点击文档进入到文档 link_text ('文档')
//点击工作台进入到工作台 link_text('工作台')
//点击“新建项目”  class="next-icestark-btn-helper"
//进入到控制台新建项目名称 id="gameName"
// input标签 上传项目图片 name="file"
// 创建项目弹窗 确认按钮 class="next-icestark-btn-helper"
(/html/body/div[3]/div[2]/div[2]/form/div[3]/button[2]/span)
// 创建项目弹窗取消按钮  //*div/button
(/html/body/div[3]/div[2]/div[2]/form/div[3])
// 创建项目弹窗 关闭按钮 /html/body/div[3]/div[2]/a
// 主控台项目搜索框 //*[@role="searchbox"]
// 主控台项目搜索按钮 //*[@class="next-icestark-input-inner next-icestark-after"]/i
// 创建的项目 //*[@id="ice-container"]/section/section/section/div/div/div/div/div/div[3]/div/div[1]/div/div[1]/div/div[1]'''
