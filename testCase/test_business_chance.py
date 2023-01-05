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

get_token = ymlOperation.read_yaml()['new_plate'].get('access_token')
print(get_token)
randomUse = get_token[randomList[0]:randomList[1]]


def test_new_module():
    string = 'this is business_chance,and I can deal with it'
    assert 'deal' in string


class Test_BusinessChance:
    def setup(self):
        print('测试用例已开始')

    def teardown(self):
        print('测试用例已结束')

    @pytest.mark.parametrize('amount, suffix, sale_stage',
                             [(''.join(str(s) for s in random.sample(range(10), 3)) + '888', randomUse + 'S888', 1),
                              (''.join(str(s) for s in random.sample(range(10), 3)) + '666', randomUse + 'S666', 1)])
    def test_BusinessSave(self, amount, suffix, sale_stage):
        Authorization = 'Bearer ' + get_token
        headers = {
            "Authorization": Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "tenantId": "1586979014478311425",
            "Content-Type": "application/json"
        }
        amount = amount
        name = "UseAmount" + suffix
        saleStage = sale_stage  # 销售阶段1-初步接洽、2-需求确定、3-方案/报价、4-谈判审核、5-赢单、6输单
        url = "http://192.168.3.155:8080/crm/business-chance/save"
        data = {
            "amount": amount,
            "customerId": '1592578254873063425',
            "endDate": "2028-12-30T08:08:08.888Z",
            "marketActivity": "string.+",
            "name": name,
            "remark": "这是很短的备注",
            "saleStage": saleStage,
            "source": 2,
            "type": 3
        }
        # print(data)
        r = requests.post(url=url, headers=headers, data=json.dumps(data))
        print("==========看下打印情况===========")
        print(r.text)

        assert json.loads(r.text)["code"] == 200  # r


pytest.main(['-sqx', 'test_business_chance.py'])
