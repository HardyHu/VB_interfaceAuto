# -*- coding:utf-8 -*-

import json
import requests
import pytest
import random

'''
上传前记得修改passwd
'''
reqPostUrl = 'http://192.168.3.155:8080/auth/login'
user = 'huzk'
passwd = '*****'  # 上传前记得修改

url = "http://192.168.3.156/dev-api/crm/clue/save"
intr = random.randint(10000, 15000)
with open('access_token.txt', 'r') as f:
    get_token = f.read()
get_token = get_token.strip()
# print('\nget_token = {}'.format(get_token))


# @pytest.fixture(params=[get_token], name="demo")
def setup():  # request
    # print(request.param)
    # yield request.param
    print("测试接口数据已准备")


def teardown():
    print("测试数据已经全部清除")


def test_ClueSave():        # demo
    global CN, N, headers, ids
    Authorization = 'Bearer ' + get_token
    Cookie = 'rememberMe=true; Admin-Expires-In=720; username=admin1; ' \
             'password=gYxS3/mkNjn/DS352bZmHQDB8abWFrg4GbfjIDtuMqRXm30A0ENkMUa9DgEBJDP/TfqCzzyXnYFyxZHgxNUeNQ==; ' \
             'Admin-Token=' + get_token
    print('\n' + Authorization)
    headers = {
        "Authorization": Authorization,
        "Cookie": Cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 "
                      "Safari/537.36",
        "tenantId": "1567682114956627970",
        "Content-Type": "application/json"
    }

    CN = "Autotest." + str(intr) + " Company"
    N = "XAutotest." + str(intr)
    data = {"companyName": CN, "name": N, "status": 1}  # ,"status": 1
    # print(data)
    data = json.dumps(data)  # 类型转换
    r = requests.post(url=url, headers=headers, data=data)  # request.param

    resp = r.text
    # ids = json.loads(resp)["data"]
    ids = r.json().get("data")
    print(f"接口响应值为{resp}")

    respCode = json.loads(resp)["code"]
    print(f"接口内的状态码为{respCode}")
    assert respCode == 200

@pytest.mark.skip(reason='不想删除。。。。')
def test_ClueDel():
    # print(f"CN is:{CN}")
    del_url = "http://192.168.3.156/dev-api/crm/clue/delete"
    data = {"ids": [ids]}
    # 1572412561666162689
    r = requests.post(url=del_url, headers=headers, data=json.dumps(data))
    print(f"接口响应值为{r.text}")
    get_code = json.loads(r.text)["code"]
    print(f"接口内的状态码为{get_code}")
    assert get_code == 200


if __name__ == '__main__':
    # # 注意global在新建函数内，所以要调用test_ClueSave才能够在这里使用全局变量ids
    # test_ClueSave()
    # print(f"\r线索添加接口测试正常。\n已返回新建线索的id：{ids}.\t状态：待删除！")
    # test_ClueDel()

    pytest.main(['-sqx', 'test_ClueInterface.py'])
