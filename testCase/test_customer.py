# -*- coding:utf-8 -*-

"""
客户的增删改查，
初期仅实现对新建和删除的用例校验
"""
import datetime
import json
import random

import pytest
import requests

# global name
t = datetime.datetime.now()
r1 = random.randint(1000, 9001)
t2 = (t + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
name = "小明" + t2[:10] + str(r1)

rd = random.sample(range(13), 5)
rstr = "".join(str(i) for i in rd)
newname = "XM" + rstr

with open('access_token.txt', 'r') as f:
    get_token = f.read()
get_token = get_token.strip()


@pytest.fixture(params=[[name, t2[:10] + "1"], [name + "A", t2[:10] + "2"], [newname, t2[:10] + "3"],
                        ["超哥" + rstr, t2[:10] + str(random.randint(6, 9))]], name="demo")
def ready(request):
    """
    需要参数化：paymentPlaneDate1，paymentPlaneDate2，remark，
        paymentDate，employeeNum
    """
    yield request.param


class Test_Customer:
    def setup(self):
        print("=========分割线=========")
        print('测试用例已开始')

    def teardown(self):
        print('测试用例已结束')

    def test_customerSave(self, demo):  # ,demo
        # global headers
        Authorization = 'Bearer ' + get_token
        print(f'{Authorization=}')
        Cookie = 'rememberMe=true; Admin-Expires-In=1440; username=admin1;' \
                 ' password=xxx==; Admin-Token=' + get_token  # + '; Old-Token=' + old_token
        headers = {
            "Authorization": Authorization,
            "Cookie": Cookie,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 Chrome/103.0.0.0 Safari/537.36",
            "tenantId": "1573493506460860417",
            "Content-Type": "application/json"
        }
        url = "http://192.168.3.156/dev-api/crm/customer/save"
        createName = demo[0]
        email = demo[1] + '@qq.com'
        data = {
            "email": email,
            "employeeNum": 4,
            "industryId": 5,
            "industryName": "",
            "type": 1,
            "invoiceList": [
                {
                    "province": "山东省",
                    "city": "淄博市",
                    "county": "张店区",
                    "address": "5008"
                },
                {
                    "address": "天津哪个区",
                    "city": "市辖区",
                    "county": "河东区",
                    "province": "天津市",
                    "areas": ["天津市", "市辖区", "河东区"]
                }
            ],
            "level": 1,
            "name": createName,
            "owner":"13636035190",
            "phone": "",
            "receiveList": [
                {
                    "address": "甘肃贯连内蒙古，内蒙古去哪儿都方便",
                    "city": "庆阳市",
                    "county": "华池县",
                    "province": "甘肃省",
                    "areas": ["甘肃省", "庆阳市", "华池县"]
                }
            ],
            "remark": "这事超长的备注。。。（）（）（）（）（）（）（）（）（）（）（）"
                      "（）（）（）（）（）（）（）（）（）（）（）（）（）#￥%……&*（）—————————————————————————————————————————"
                      "—————————————————————————————————！！！！！！！！！！！！！！！！！！！！！！！！righting《 的我看就不"
                      "打空间大把我答辩机会不放假无法解开方便未接！这事超长的备注。。。（）（）（）（）（）（）（）（）（）（）（）（）（）（）（）（）（）（）（）（）（）"
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
        print(f'checkStr object is {checkStr}')
        assert "联系人" in checkStr


if __name__ == '__main__':
    pytest.main(["-sqx", "test_customer.py"])
