# -*- coding:utf-8 -*-

"""
商机的增删改查， -- 也需要关注统计与报表
初期仅实现对新建和删除的用例校验
"""

import random
import pytest
import json
from user.file_operation import ymlOperation
import requests

randomList = random.sample(range(4, 10), 2)
relay = 0  # 中继函数
if randomList[0] > randomList[1]:
    relay = randomList[0]
    randomList[0] = randomList[1]
    randomList[1] = relay
    if randomList[1] - randomList[0] == 1:
        randomList[1] = randomList[1] + 5

if randomList[1] - randomList[0] == 1:
    randomList[1] = randomList[1] + 3

get_token = ymlOperation.read_yaml()['new_plate'].get('access_token')
print(get_token)
randomUse = get_token[randomList[0]:randomList[1]]
newKey1 = -randomList[0]
newKey2 = -randomList[1]



def test_new_module():
    string = 'this is business_chance,and I can deal with it'
    assert 'deal' in string


class Test_BusinessChance:
    def setup(self):
        print('测试用例已开始')

    def teardown(self):
        print('测试用例已结束')

    @pytest.mark.parametrize('amount, suffix, sale_stage',
                             [(1888, randomUse + '8', 1),
                              (''.join(str(s) for s in random.sample(range(10), 3)) + '666', randomUse + '6', 1)])
    def test_BusinessSave(self, amount, suffix, sale_stage):
        Authorization = 'Bearer ' + get_token
        headers = {
            "Authorization": Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "tenantId": "1586979014478311425",
            "Content-Type": "application/json"
        }
        length = random.randint(3, 5)  # 注：现在要求商机名不能重复，为避免二次重跑时，名称出现问题，现在追加了对截取随机片段的随机性切片
        name = get_token[newKey2:newKey1+length] + suffix
        saleStage = sale_stage  # 销售阶段1-初步接洽、2-需求确定、3-方案/报价、4-谈判审核、5-赢单、6输单 
        url = "http://192.168.3.155:8080/crm/business-chance/save"
        data = {
            "amount": amount,
            "customerId": '1808028532628668418',
            "endDate": "2025-10-01T16:00:00.000Z",
            "marketActivity": "string.+",
            "name": name,
            "saleStage": saleStage,
            "source": 2,
            "type": 3,
            "owner": "马兴超",
            "businessChanceContent": "自动化修改1Content",
            "contactsName": "自动化联系人01",
            "contactsPhone": "15512344444",
            "contactsList": [
                {
                    "name": "自动化联系人01",
                    "phone": "15512344444",
                    "status": 1
                }
            ],
        }
        # print(data)
        r = requests.post(url=url, headers=headers, data=json.dumps(data))
        print("\n==========看下打印情况===========")
        print(r.text)

        assert json.loads(r.text)["code"] == 200  # r


pytest.main(['-sqx', 'test_business_chance.py'])
