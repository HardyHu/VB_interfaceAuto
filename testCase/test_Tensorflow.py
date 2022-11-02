# -*- coding:utf-8 -*-

import pytest


def calculate(num, numan):
    return num * numan


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
