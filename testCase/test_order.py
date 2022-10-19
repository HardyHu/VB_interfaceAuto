# -*- coding:utf-8 -*-

"""
订单的增删改查，
初期仅实现对新建和删除的用例校验
"""
import pytest
import requests
import json
import datetime
import random

global order_newlist
order_newlist = []

t = datetime.datetime.now()

# 2022-10-14 14:29:02.572777
t2 = datetime.datetime.now()
t2 = t2.strftime("%Y-%m-%d %H:%M:%S")
dtjoin1 = t2[:10] + "T" + t2[11:] + ".000Z"

t3 = (t + datetime.timedelta(days=100)).strftime("%Y-%m-%d %H:%M:%S")
dtjoin2 = t3[:10] + "T23:00:00.000Z"

with open('access_token.txt', 'r') as f:
    get_token = f.read()
get_token = get_token.strip()


@pytest.fixture(params=[[dtjoin1, ''.join(str(i) for i in random.sample(range(10), 5)), dtjoin2],
                        [dtjoin1, ''.join(str(i) for i in random.sample(range(10), 5)), dtjoin2],
                        [dtjoin1, ''.join(str(i) for i in random.sample(range(10), 5)), dtjoin2]], name="demo")
def ready(request):
    """
    需要参数化：dtjoin1，mynum，dtjoin2
    """
    yield request.param


class Test_Order(object):
    def setup(self):
        print('测试用例已开始')

    def teardown(self):
        print('测试用例已结束')

    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_ordersave(self, demo):
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
        save_url = 'http://192.168.3.156/dev-api/crm/order/save'
        deliveryDate = demo[2]
        mynum = demo[1]
        placeOrderDate = demo[0]
        data = {"amount": 990000.00,
                "contractId": 1573601475999346690,
                "contractNumber": "HT202209240010",
                "customerId": 1570601452197924866,  # 戚继光
                "discount": 90.00,
                "invoiceAddressId": 0,
                "orderDetailList": [
                    {
                        "amount": 1000000.00,
                        "deliveryDate": deliveryDate,  # 交货日期
                        "deliveryWarehouse": "string",
                        "discount": 98.50,  # 折扣
                        "minNum": 10,
                        "num": 10000,
                        "productCode": "Already" + mynum[:-1],
                        "productName": "AutomaticTest",
                        "remark": "商品好啊djh卐卍888" + mynum[:-1],
                        "specs": "1000*2000",
                        "unit": "吨",
                        "unitPrice": 100,
                        "warehouseId": ""  # 1e572de3a2174ff8b47b24b4bde7b619 table:erp_location,name:洞天福地11 status:0启用
                    },
                    {
                        "amount": 1000000.00,
                        "deliveryDate": deliveryDate,  # 交货日期
                        "deliveryWarehouse": "string",
                        "discount": 98.50,  # 折扣
                        "minNum": 10,
                        "num": 10000,
                        "productCode": "Already" + mynum,
                        "productName": "AutomaticTest",
                        "remark": "商品好啊" + mynum,
                        "specs": "1000*2000",
                        "unit": "吨",
                        "unitPrice": 100,
                        "warehouseId": ""  # 1e572de3a2174ff8b47b24b4bde7b619 table:erp_location,name:洞天福地11 status:0启用
                    },
                    {
                        "amount": 1000000.00,
                        "deliveryDate": deliveryDate,  # 交货日期
                        "deliveryWarehouse": "string",
                        "discount": 98.50,  # 折扣
                        "minNum": 10,
                        "num": 10000,
                        "productCode": "Already" + mynum,
                        "productName": "AutomaticTest",
                        "remark": "商品好啊" + mynum,
                        "specs": "1000*2000",
                        "unit": "吨",
                        "unitPrice": 100,
                        "warehouseId": ""  # 1e572de3a2174ff8b47b24b4bde7b619 table:erp_location,name:洞天福地11 status:0启用
                    },
                    {
                        "amount": 1000000.00,
                        "deliveryDate": deliveryDate,  # 交货日期
                        "deliveryWarehouse": "string",
                        "discount": 98.50,  # 折扣
                        "minNum": 10,
                        "num": 10000,
                        "productCode": "Already" + mynum,
                        "productName": "AutomaticTest",
                        "remark": "商品好啊" + mynum,
                        "specs": "1000*2000",
                        "unit": "吨",
                        "unitPrice": 100,
                        "warehouseId": ""  # 1e572de3a2174ff8b47b24b4bde7b619 table:erp_location,name:洞天福地11 status:0启用
                    },
                    {
                        "amount": 1000000.00,
                        "deliveryDate": deliveryDate,  # 交货日期
                        "deliveryWarehouse": "string",
                        "discount": 98.50,  # 折扣
                        "minNum": 10,
                        "num": 10000,
                        "productCode": "Already" + mynum,
                        "productName": "AutomaticTest",
                        "remark": "商品好啊" + mynum,
                        "specs": "1000*2000",
                        "unit": "吨",
                        "unitPrice": 100,
                        "warehouseId": ""  # 1e572de3a2174ff8b47b24b4bde7b619 table:erp_location,name:洞天福地11 status:0启用
                    },
                    {
                        "amount": 1000000.00,
                        "deliveryDate": deliveryDate,  # 交货日期
                        "deliveryWarehouse": "string",
                        "discount": 98.50,  # 折扣
                        "minNum": 10,
                        "num": 10000,
                        "productCode": "Already" + mynum,
                        "productName": "AutomaticTest",
                        "remark": "商品好啊" + mynum,
                        "specs": "1000*2000",
                        "unit": "吨",
                        "unitPrice": 100,
                        "warehouseId": ""  # 1e572de3a2174ff8b47b24b4bde7b619 table:erp_location,name:洞天福地11 status:0启用
                    },
                    {
                        "amount": 1000000.00,
                        "deliveryDate": deliveryDate,  # 交货日期
                        "deliveryWarehouse": "string",
                        "discount": 98.50,  # 折扣
                        "minNum": 10,
                        "num": 10000,
                        "productCode": "Already" + mynum,
                        "productName": "AutomaticTest",
                        "remark": "商品好啊" + mynum,
                        "specs": "1000*2000",
                        "unit": "吨",
                        "unitPrice": 100,
                        "warehouseId": ""  # 1e572de3a2174ff8b47b24b4bde7b619 table:erp_location,name:洞天福地11 status:0启用
                    },
                    {
                        "amount": 1000000.00,
                        "deliveryDate": deliveryDate,  # 交货日期
                        "deliveryWarehouse": "string",
                        "discount": 98.50,  # 折扣
                        "minNum": 10,
                        "num": 10000,
                        "productCode": "Already" + mynum,
                        "productName": "AutomaticTest",
                        "remark": "商品好啊" + mynum,
                        "specs": "1000*2000",
                        "unit": "吨",
                        "unitPrice": 100,
                        "warehouseId": ""  # 1e572de3a2174ff8b47b24b4bde7b619 table:erp_location,name:洞天福地11 status:0启用
                    },
                    {
                        "amount": 1000000.00,
                        "deliveryDate": deliveryDate,  # 交货日期
                        "deliveryWarehouse": "string",
                        "discount": 98.50,  # 折扣
                        "minNum": 10,
                        "num": 10000,
                        "productCode": "Already" + mynum,
                        "productName": "AutomaticTest",
                        "remark": "商品好啊" + mynum,
                        "specs": "1000*2000",
                        "unit": "吨",
                        "unitPrice": 100,
                        "warehouseId": ""  # 1e572de3a2174ff8b47b24b4bde7b619 table:erp_location,name:洞天福地11 status:0启用
                    },
                    {
                        "amount": 1000000.00,
                        "deliveryDate": deliveryDate,  # 交货日期
                        "deliveryWarehouse": "string",
                        "discount": 98.50,  # 折扣
                        "minNum": 10,
                        "num": 10000,
                        "productCode": "Already" + mynum,
                        "productName": "AutomaticTest",
                        "remark": "商品好啊" + mynum,
                        "specs": "1000*2000",
                        "unit": "吨",
                        "unitPrice": 100,
                        "warehouseId": ""  # 1e572de3a2174ff8b47b24b4bde7b619 table:erp_location,name:洞天福地11 status:0启用
                    },
                    {
                        "amount": 1000000.00,
                        "deliveryDate": deliveryDate,  # 交货日期
                        "deliveryWarehouse": "string",
                        "discount": 98.50,  # 折扣
                        "minNum": 10,
                        "num": 10000,
                        "productCode": "Already" + mynum[1:],
                        "productName": "AutomaticTest",
                        "remark": "商品好啊卐卍卍卍666" + mynum[1:],
                        "specs": "1000*2000",
                        "unit": "吨",
                        "unitPrice": 100,
                        "warehouseId": ""  # 1e572de3a2174ff8b47b24b4bde7b619 table:erp_location,name:洞天福地11 status:0启用
                    }
                ],
                "placeOrderDate": placeOrderDate,
                "receiveAddressId": 0,
                "remark": r"九折带5\|/",
                "status": 1
                }
        r = requests.post(url=save_url, headers=headers, data=json.dumps(data))
        resp = r.text
        print(resp)
        order_id = json.loads(resp)['data']
        order_newlist.append(order_id)
        code = json.loads(resp)["code"]
        assert code == 200

    @pytest.mark.skip(reason = '我想跳过')
    def test_orderdel(self):
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
        del_url = 'http://192.168.3.156/dev-api/crm/order/delete'
        if len(order_newlist) >= 3:
            idsdel1 = order_newlist[1]
            idsdel2 = order_newlist[2]
        data = {
            "ids": [
                idsdel1
            ]
        }
        print(data)
        rone = requests.post(url=del_url, headers=headers, data=json.dumps(data))
        print("********************")
        if idsdel1:
            assert json.loads(rone.text)['code'] == 200

        data = {
            "ids": [
                idsdel2
            ]
        }
        print(data)
        rtwo = requests.post(url=del_url, headers=headers, data=json.dumps(data))
        print("/////////////////////")
        if idsdel2:
            assert json.loads(rtwo.text)['code'] == 200
            print(rtwo.text)


if __name__ == "__main__":
    pytest.main(['-sqx', 'test_order.py'])
