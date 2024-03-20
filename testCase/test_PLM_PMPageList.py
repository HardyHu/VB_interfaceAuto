# -*- coding:utf-8 -*-

"""
197PLM的列表接口处理
初期仅实现数据刷新校验
author_Hardy
"""
import json
import random

import pytest
import requests

from user.file_operation import ymlOperation

randomList = random.sample(range(4, 10), 2)

get_token = ymlOperation.read_yaml()['197_Env_Test'].get('197_token')
get_host = ymlOperation.read_yaml()['197_Env_Test'].get('Interface_Api_Host')
print(get_token, '\n', get_host)


def deal_root():
    api_url = get_host + 'plmProjectManageEntity/pageList'
    return api_url


url = deal_root()
print(url)


class Test_PM_List:

    def setup(self):
        print("\n初始化OK.")

    def teardown(self):
        print("数据已清理.\n")

    @pytest.mark.parametrize('demo',
                             [11, 22])
    def test_loaddata(self, demo):
        """
        用来测试ERP--进销存--及时库存第一页的数据状况
        :param demo:自动化需要校验的每页大小
        size::指定页的数据量，有每页10条/20条/30条...
        total: 实际去校验，拉取的数据有多少条
        recordsLength: 得到拉取的数据长度是多少

        """
        Authorization = 'Bearer ' + get_token

        headers = {
            "Authorization": Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "Content-Type": "application/json"
        }

        params = {
            'current': 1,
            'projectStatus': "",
            'searchWord': "",
            'size': 10
        }
        r = requests.post(url=url, headers=headers, data=json.dumps(params))
        # print(r.text)
        resPj = json.loads(r.text)

        # 当前页拉取的数据是否是标准的十条，还是开发未处理的多条（总量大于10条的情况）
        recordsLength = len(resPj["data"]["records"])
        if recordsLength == 10:
            print("检查加载第一页完成，第一页数据有10条！")
        else:
            print(f"recordsLength is :{recordsLength}")
            print("请检查测试环境是否出现服务异常，或者数据已经被清理!")
        size = resPj["data"]["size"]
        total = resPj["data"]["total"]

        if total > size == int(demo):
            print("当前在第一页")
            assert resPj["data"]["current"] == 1
        if total > recordsLength:
            print(f'可能数据不止一页：{total}条')
            assert resPj["data"]["pages"] > 1


if __name__ == '__main__':
    '''
    -s：显示程序中的 print/logging 输出。
    -v：丰富信息模式, 输出更详细的用例执行信息。
    -k：运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行 XX.py 中包含 add 的测试用例。
    -q：简单输出模式, 不输出环境信息。
    -x：出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
    '''
    # test_demo = 11
    # Test_PM_List.test_loaddata(Test_PM_List, test_demo)

    pytest.main(["-sqx", "test_PLM_PMPageList.py"])
    print("=====测试完成=====")
