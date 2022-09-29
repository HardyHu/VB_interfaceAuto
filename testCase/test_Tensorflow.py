# -*- coding:utf-8 -*-

import selenium
import pytest
import allure_pytest
import allure

def cacl(num,numan):
    return num * numan

class Testnewclass():
    def setup(self):
        print("\n初始化……数据准备中")

    def teardown(self):
        print("\n清理测试痕迹……")

    def test_Jiafa(self):
        assert 5 + 3 == 8

    def test_Jianfa(self):
        assert 7 - 2 == 5

    def test_Chenfa(self):
        assert cacl(3,4) == 12

# def setup():
#     print("初始化……数据准备中")
#
#
# def teardown():
#     print("清理测试痕迹……")
#
#
# def test_Jiafa():
#     assert 5 + 3 == 8
#
#
# def test_Jianfa():
#     assert 7 - 2 == 5
#
#
# def test_Chenfa():
#     assert 3 * 4 == 12

if __name__ == "__main__":
    pytest.main()
