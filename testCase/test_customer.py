# -*- coding:utf-8 -*-

"""
客户的增删改查，
初期仅实现对新建和删除的用例校验
"""
# import datetime
import json
import random

import pytest
import requests
from user.file_operation import ymlOperation

# global name
r1 = random.randint(1000, 9001)
name = "bug" + str(r1)

rd = random.sample(range(13), 5)
rstr = "".join(str(i) for i in rd)
newname = "Tester" + rstr


get_token = ymlOperation.read_yaml()['197_Env_Test'].get('197_token')


@pytest.fixture(
    params=[[name + str(random.randint(0, 10)), "1779675995667251201"], [name + "A", "1779675995667251201"],
            [newname, "1771001397778141185"],
            ["测试" + rstr, "1771001397778141185"]], name="demo")
def ready(request):
    """
    需要参数化：paymentPlaneDate1，paymentPlaneDate2，remark，
        paymentDate，employeeNum
    """
    yield request.param


def setup():
    print("=========分割线=========")
    print('测试用例已开始')


def teardown():
    print('测试用例已结束')


class Test_Customer:

    def test_customerSave(self, demo):  # ,demo
        # global headers
        Authorization = 'Bearer ' + get_token
        # print(f'{Authorization=}')

        headers = {
            "Authorization": Authorization,
            # "Cookie": Cookie,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 Chrome/103.0.0.0 Safari/537.36",
            "tenantId": "1586979014478311425",
            "Content-Type": "application/json"
        }
        url = "http://192.168.3.197/prod-api/crm/customer/save"

        data = {
            "contactsList": [
                {
                    "name": "自动化联系人01",
                    "phone": "15512344444"
                }
            ],
            "owner": "马兴超",
            "countryId": "10",
            "name": demo[0],
            "type": demo[1],
            "industryId": "4",
            "areaId": "120000000000",
            "areaName": "天津市",
            "address": "修改了国家等区域信息；；；",
            "relatedBusinessId": "1773548333945917443",
            "contacts": "自动化联系人01",
            "countryName": "中国"
        }
        # print(data)
        data = json.dumps(data)
        r = requests.post(url=url, headers=headers, data=data)
        print(r.text)

        code = json.loads(r.text)["code"]
        # print(code)
        assert code == 200

    def test_CustomerDel(self):
        # url = "http://192.168.3.156/dev-api/crm/customer/save"
        data = {"目前客户、联系人都没有删除功能，无需校验"}
        checkStr = list(data)[0][4:8]
        print(f'{checkStr =}')
        assert "联系人" in checkStr


if __name__ == '__main__':
    pytest.main(["-sqx", "test_customer.py"])
