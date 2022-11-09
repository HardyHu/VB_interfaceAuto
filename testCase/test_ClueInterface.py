# -*- coding:utf-8 -*-

import json
import requests
import pytest
import random

url = "http://192.168.3.156/dev-api/crm/clue/save"
int_r = random.randint(10000, 15000)
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
    Cookie = 'rememberMe=true; Admin-Expires-In=720; username=admin1; ' \
             'password=xxxx==; ' \
             'Admin-Token=' + get_token
    headers = {
        "Authorization": Authorization,
        "Cookie": Cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 Chrome/103.0.0.0 "
                      "Safari/537.36",
        "tenantId": "1586979014478311425",
        "Content-Type": "application/json"
    }

    CN = "test." + str(int_r) + " Company"
    N = "Xtest." + str(int_r)
    for i in range(2):
        data = {"companyName": CN, "name": N + str(i), "status": 1}
        # print(data)
        r = requests.post(url=url, headers=headers, data=json.dumps(data))  # request.param

        resp = r.text
        # ids = json.loads(resp)["data"]
        ids = r.json().get("data")
        clueList.append(ids)
        print(f"接口响应内容为{resp}")

        respCode = json.loads(resp)["code"]
        print(f"接口内的状态码为{respCode}")
        assert respCode == 200
    print(clueList)


# @pytest.mark.skip(reason='不想删除。。。。')
def test_ClueDel():
    # print(f"CN is:{CN}")
    del_url = "http://192.168.3.156/dev-api/crm/clue/delete"
    if len(clueList) >= 2:
        for i in range(len(clueList)):
            data = {"ids": [clueList[i]]}
            r = requests.post(url=del_url, headers=headers, data=json.dumps(data))
            print(f"删除接口响应为{r.text}")
            get_code = json.loads(r.text)["code"]
            print(f"接口内的状态码为{get_code}")
            assert get_code == 200


if __name__ == '__main__':
    # # 注意global在新建函数内，所以要调用test_ClueSave才能够在这里使用全局变量ids
    # test_ClueSave()
    # print(f"\r线索添加接口测试正常。\n已返回新建线索的id：{ids}.\t状态：待删除！")
    # test_ClueDel()

    pytest.main(['-sqx', 'test_ClueInterface.py'])
