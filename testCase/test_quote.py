# -*- coding:utf-8 -*-

"""
报价的增删改查，
初期仅实现对新建和删除的用例校验
"""
import pytest
import requests
import json
import datetime
import random
import time

global newlist,headers
with open('access_token.txt', 'r') as f:
    get_token = f.read()
get_token = get_token.strip()
newlist = []
Authorization = 'Bearer ' + get_token
Cookie = 'rememberMe=true; Admin-Expires-In=720; username=admin1; ' \
         'password=Ce8Xk0ifC2xa3pAjSQiX3woOewkWzBDnIqRsrmXdUGHRP9XJoKxDxUfqS/CUcU901BZz5TrPYf2NkDkHUEdaOg==; ' \
         'Admin-Token=' + get_token
headers = {
    "Authorization": Authorization,
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.0.0 Safari/537.36",
    "tenantId": "1567682114956627970",
    "Content-Type": "application/json"
}

t2 = datetime.datetime.now()
t2 = t2.strftime("%Y-%m-%d %H:%M:%S")
t = t2[:10] + "T" + t2[11:] + ".000Z"




@pytest.fixture(params=[[1, t], [2, t], [3, t], [4, t], [5, t]], name="demo")
def ready(request):
    """
    需要参数化：t
    """
    yield request.param


class Test_Quote(object):
    def setup(self):
        print('测试用例已开始~~')

    def teardown(self):
        print('测试用例已结束~~')

    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_quotesave(self, demo):  # , demo
        save_url = 'http://192.168.3.156/dev-api/crm/quote/save'

        date = demo[1]
        num = str(demo[0])
        data = {
            "amount": 35000000,
            "businessId": 1574730119043932162,  # 商机id
            "currency": "rmb",
            "customerId": 1580852611038867457,  # 测试大佬
            "date": date,  # 报价日期
            "discount": 1,  # 折扣
            "fileList": [
                {
                    "name": "正则替换compile到sub_OBJ1_STR.png",
                    "url": "http://192.168.3.156:9000/hh-wb/crm/test/20221018/1666056278264.png"
                }
            ],
            "name": "美好的报价单" + num,  # 报价单名称
            "quoteDetailList": [
                {
                    "amount": 100000,
                    "currency": "",
                    "discount": 1,
                    "minNum": 20,
                    "num": 10000,
                    "productCode": "NYmarket008",
                    "productName": "Newyork city",
                    "rate": 1,
                    "remark": "报价明细1",
                    "specs": "500*3600",
                    "unit": "斤",
                    "unitPrice": 800
                },
                {
                    "amount": 100000,
                    "currency": "",
                    "discount": 1,
                    "minNum": 20,
                    "num": 10000,
                    "productCode": "WSTmarket009",
                    "productName": "Washington city",
                    "rate": 1,
                    "remark": "报价明细2",
                    "specs": "500*3600",
                    "unit": "吨",
                    "unitPrice": 900
                },
                {
                    "amount": 100000,
                    "currency": "",
                    "discount": 1,
                    "minNum": 20,
                    "num": 10000,
                    "productCode": "LA010",
                    "productName": "Los Angeles city",
                    "rate": 1,
                    "remark": "报价明细3",
                    "specs": "500*3600",
                    "unit": "个",
                    "unitPrice": 200
                },
                {
                    "amount": 100000,
                    "currency": "",
                    "discount": 1,
                    "minNum": 20,
                    "num": 10000,
                    "productCode": "NYmarket008",
                    "productName": "Newyork city",
                    "rate": 1,
                    "remark": "报价明细4",
                    "specs": "500*3600",
                    "unit": "盒",
                    "unitPrice": 800
                },
                {
                    "amount": 100000,
                    "currency": "",
                    "discount": 1,
                    "minNum": 20,
                    "num": 10000,
                    "productCode": "NYmarket008",
                    "productName": "Newyork city",
                    "rate": 1,
                    "remark": "报价明细5",
                    "specs": "500*3600",
                    "unit": "盒",
                    "unitPrice": 800
                }
            ],
            "rate": 0.90,  # 汇率
            "remark": "人民币由1.0汇率，被主动调整成0.9了。testing & waiting ：Let the Bullets Fly",  # 备注
            "status": 1  # 报价单状态1-新建、2-已审核、3-通过、4-拒绝
        }
        response = requests.post(url=save_url, headers=headers, data=json.dumps(data))
        print(response.text)
        quote_id = json.loads(response.text)['data']
        newlist.append(quote_id)  # 补充新建的数据id到列表
        assert json.loads(response.text)["code"] == 200

    @pytest.mark.skip(reason='只是想跳过.')
    def test_quotedel(self):
        del_url = 'http://192.168.3.156/dev-api/crm/quote/delete'

        for content in newlist[-3:]:  # 取倒数三个数据进行删除操作
            data = {
                "ids": [content]
            }
            time.sleep(1)
            resp = requests.post(url=del_url, headers=headers, data=json.dumps(data))
            assert json.loads(resp.text)['code'] == 200


if __name__ == '__main__':
    pytest.main(['-svx', 'test_quote.py'])  # -rs
