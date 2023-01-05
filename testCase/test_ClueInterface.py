# -*- coding:utf-8 -*-

import json
import random
import pytest
import requests

url = "http://192.168.3.156/dev-api/crm/clue/save"

with open('access_token.txt', 'r') as f:
    get_token = f.read()
get_token = get_token.strip()


def setup():
    print("测试接口数据已准备")


def teardown():
    print("测试数据已经全部清除")


def test_ClueSave():  # demo
    global headers, ids, clueList
    clueList = []
    Authorization = 'Bearer ' + get_token

    headers = {
        "Authorization": Authorization,
        # "Cookie": Cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 Chrome/103.0.0.0 "
                      "Safari/537.36",
        "tenantId": "1586979014478311425",
        "Content-Type": "application/json"
    }

    for i in range(2):
        int_r = random.randint(18000, 20000)
        CN = "test." + str(int_r) + " Company"
        N = "Xtest." + str(int_r)
        data = {"companyName": CN, "name": N + str(i), "status": 1, "address": "Boss will not let u survive till the "
                                                                               "end.233", "province": "",
                "city": "", "county": ""}  # 江苏省 徐州市 云龙区
        r = requests.post(url=url, headers=headers, data=json.dumps(data))  # request.param

        ids = r.json().get("data")
        clueList.append(ids)
        print(f"接口响应内容为{r.text}")

        respCode = json.loads(r.text)["code"]
        print(f"接口内的状态码为{respCode}")
        assert respCode == 200
    print(clueList)


@pytest.mark.skip(reason='制造数据，暂未删除新建的数据。')
def test_ClueDel():
    del_url = "http://192.168.3.156/dev-api/crm/clue/delete"
    if len(clueList) >= 2:
        for i in range(len(clueList)):
            data = {"ids": [clueList[i]]}
            r = requests.post(url=del_url, headers=headers, data=json.dumps(data))
            print(f"删除接口响应为{r.text}")
            get_code = json.loads(r.text)["code"]
            print(f"接口内的状态码为{get_code}")
            assert get_code == 200

pytest.main(['-sqx', 'test_ClueInterface.py'])
