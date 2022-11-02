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


# coding:utf-8

import pytest
import allure


# 测试函数
@allure.step("字符串相加：{0}，{1}")  # 测试步骤，可通过format机制自动获取函数参数
def str_add(str1, str2):
    print("hello")
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2


# # @llure.environment(host="172.6.12.27", test_vars=paras) -- . allure模块的应用与 pytest用例调用
# @allure.severity("critical")  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
# @allure.feature("测试模块_demo1")  # 功能块，feature功能分块时比story大,即同时存在feature和story时,feature为父节点
# @allure.story("测试模块_demo2")  # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
# @allure.issue("BUG号：123")  # 问题表识，关联标识已有的问题，可为一个url链接地址
# @allure.testcase("用例名：测试字符串相等")  # 用例标识，关联标识用例，可为一个url链接地址
# @pytest.mark.parametrize("para_one, para_two",  # 用例参数
#                          [("hello world", "hello world"),  # 用例参数的参数化数据
#                           (4, 4),
#                           ("中文", "中文")],
#                          ids=["test ASCII string",  # 对应用例参数化数据的用例名
#                               "test digital string",
#                               "test unicode string"])
# def test_case_example(para_one, para_two):
#     """用例描述：测试字符串相等
#     :param para_one: 参数1
#     :param para_two: 参数2
#     """
#
#     # 获取参数
#     paras = vars()
#     # 报告中的环境参数，可用于必要环境参数的说明，相同的参数以后者为准
#     allure.environment(host="172.6.12.27", test_vars=paras)
#     # 关联的资料信息, 可在报告中记录保存必要的相关信息
#     allure.attach("用例参数", "{0}".format(paras))
#     # 调用测试函数
#     res = str_add(para_one, para_two)
#     # 对必要的测试中间结果数据做备份
#     allure.attach("str_add返回结果", "{0}".format(res))
#     # 测试步骤，对必要的测试过程加以说明
#     with pytest.allure.step("测试步骤2，结果校验 {0} == {1}".format(res, para_one + para_two)):
#         assert res == para_one + para_two, res
#
#
# if __name__ == '__main__':
#     # 执行，指定执行测试模块_demo1, 测试模块_demo2两个模块，同时指定执行的用例优先级为critical,blocker
#     pytest.main(['--allure_stories=测试模块_demo1, 测试模块_demo2', '--allure_severities=critical, blocker'])
