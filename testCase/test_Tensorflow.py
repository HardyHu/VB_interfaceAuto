# -*- coding:utf-8 -*-

import pytest
# import allure


def calculate(num, numan):
    return num * numan

# @allure.environment(host="172.6.12.27", test_vars=paras)
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


class Test_new:
    def setup(self):
        print("\n初始化……数据准备中")

    def teardown(self):
        print("\n清理测试痕迹……")

    def test_JiaFa(self):
        assert 5 + 3 == 8

    def test_JianFa(self):
        assert 7 - 2 == 5

    def test_chenFa(self):
        assert calculate(3, 4) == 12


if __name__ == "__main__":
    pytest.main(['-svx', 'test_Tensorflow.py'])
