# -*- coding:utf-8 -*-
import time

import allure
import pytest

"""
截图专用Package...

在这个代码中，我分别定义了两个命令行参数 flag 和 browser。

flag：只有两个值 True 和 False，当用户不传 flag 参数时，默认为 False，当用户传递 flag 时，值为 True。

browser：代表要启用的浏览器，默认是 Firefox 浏览器。

对应地，get_flag 和 get_browser 这两个 fixture 就是分别用来取 flag 和 browser 的值。

被装饰器 @pytest.hookimpl(tryfirst=True, hookwrapper=True) 装饰的函数 pytest_runtest_makereport，是 pytest 提供的 Hook 函数，它有以下两个作用：

可以获取到测试用例不同执行阶段的结果（setup，call，teardown）；

可以获取钩子方法的调用结果（yield 返回一个 result 对象）和调用结果的测试报告（返回一个 report 对象，即 _pytest.runner.TestReport）。
"""

def pytest_addoption(parser):
    parser.addoption(
        "--flag", action="store_true", default=False, help="set skip or not")
    parser.addoption(
        "--browser", action="store", default="Chrome", help="set browser")      # 这里把Firefox 改成了 Chrome

# @pytest.fixture(scope='session')
# def get_flag(request):
#     return request.config.getoption('--flag')

# @pytest.fixture(scope='session')
# def get_browser(request):
#     return request.config.getoption('--browser')

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):

#     """
#     　　本hook用于制作测试报告
#     　　:param item:测试用例对象
#     　　:param call:测试用例的测试步骤
#     　　        执行完常规钩子函数返回的report报告有个属性叫report.when
#                 when=’setup’ 代表返回setup 的执行结果
#                 when=’call’ 代表返回call 的执行结果
#     　　:return:
#     """

#     outcome = yield
#     rep = outcome.get_result()
#     if (rep.when == "call" or rep.when == 'setup') and (rep.failed or rep.skipped):
#         try:
#             # t = time.time()
#             # printt = time.localtime(t)
#             # printt = time.strftime("%Y-%m-%d %H:%M:%S.%f", printt)
#             if "initial_browser" in item.fixturenames:
#                 web_driver = item.funcargs['initial_browser']
#             else:
#                 # 如果找不到driver，则直接return
#                 return

#             allure.attach(web_driver.get_screenshot_as_png(), name="1688",         # 关键动作在这行
#                           attachment_type=allure.attachment_type.PNG)
#         except Exception as e:
#             print("failed to take screenshot".format(e))