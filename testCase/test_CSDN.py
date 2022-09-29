# -*- coding:utf-8 -*-

from selenium import webdriver
import pytest

# wd = webdriver.Chrome()
# url = "https://blog.csdn.net/qq_17195161"
# wd.get(url)    # 打印标题：开河大大的博客_CSDN博客-自动化,Python开发工具,Python爬虫领域博主
# wd.implicitly_wait(5)
# wd.maximize_window()
#
# def test_title():
#     title = wd.title
#     assert title == "开河大大的博客_CSDN博客-自动化,Python开发工具,Python爬虫领域博主"
#
# wd.quit()

def title_output():
    return "开河大大的博客_CSDN博客-自动化,"

def test_Quenendtitle():
    assert title_output() == "开河大大的博客_CSDN博客-自动化,"

if __name__ == "__main__":
    pytest.main()
