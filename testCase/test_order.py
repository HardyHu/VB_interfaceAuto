# -*- coding:utf-8 -*-

"""
订单的增删改查，
初期仅实现对新建和删除的用例校验
"""
import datetime
import json
import random

import pytest
import requests

global order_newList
order_newList = []

t = datetime.datetime.now()

# 2022-10-14 14:29:02.572777
t2 = datetime.datetime.now()
t2 = t2.strftime("%Y-%m-%d %H:%M:%S")
nowDate = t2[:10] + "T" + t2[11:] + ".000Z"

t3 = (t + datetime.timedelta(days=100)).strftime("%Y-%m-%d %H:%M:%S")
afterDate = t3[:10] + "T23:00:00.000Z"

with open('access_token.txt', 'r') as f:
    get_token = f.read()
get_token = get_token.strip()


@pytest.fixture(params=[[nowDate, ''.join(str(i) for i in random.sample(range(10), 5)), afterDate],
                        [nowDate, ''.join(str(i) for i in random.sample(range(10), 5)), afterDate],
                        [nowDate, ''.join(str(i) for i in random.sample(range(10), 5)), afterDate]], name="demo")
def ready(request):
    """
    需要参数化：nowDate，mynum，afterDate
    """
    yield request.param


class Test_Order(object):
    def setup(self):
        print('测试用例已开始')

    def teardown(self):
        print('测试用例已结束')

    # @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_order_save(self, demo):
        Authorization = 'Bearer ' + get_token
        Cookie = 'rememberMe=true; Admin-Expires-In=720; username=admin1; ' \
                 'password=xx/CUcU901BZz5TrPYf2NkDkHUEdaOg==; ' \
                 'Admin-Token=' + get_token
        headers = {
            "Authorization": Authorization,
            "Cookie": Cookie,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                          "Chrome/103.0.0.0 Safari/537.36",
            "tenantId": "1586979014478311425",
            "Content-Type": "application/json"
        }
        save_url = 'http://192.168.3.156/dev-api/crm/order/save'
        deliveryDate = demo[2]
        mynum = demo[1]
        placeOrderDate = demo[0]
        data = {"amount": 9900000.00,
                "contractId": 1591959981957705729,  # 不同租户的合同需要替换掉,名:
                # "name": "合同test010","number": "wsht_010",
                "contractNumber": "HT2022-11-141316R",
                "customerId": 1591353038708686850,  # "name":Tester13090875
                "discount": 90.00,
                "invoiceAddressId": 1591353038750629889,  # 开票地址一定要跟客户相关联
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
                        # "discount": 98.50,  # 折扣
                        "minNum": 10,
                        "num": 1000,
                        "productCode": "Already" + mynum,
                        "productName": "AutomaticTest",
                        "remark": "商品好啊" + mynum,
                        "specs": "1000*2000",
                        "unit": "吨",
                        "unitPrice": 2000,
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
                        # "discount": 98.50,  # 折扣
                        "minNum": 10,
                        "num": 10000,
                        "productCode": "Already" + mynum[1:],
                        "productName": "AutomaticTest",
                        "remark": "商品好啊卐卍卍卍666" + mynum[1:],
                        "specs": "1000*2000",
                        "unit": "吨",
                        "unitPrice": 200,
                        "warehouseId": ""  # 1e572de3a2174ff8b47b24b4bde7b619 table:erp_location,name:洞天福地11 status:0启用
                    }
                ],
                "placeOrderDate": placeOrderDate,
                "receiveAddressId": 1591353038750629890,  # 收货地址一定要跟客户相关联
                "remark": r"九折带5\|/",
                "status": 1
                }
        r = requests.post(url=save_url, headers=headers, data=json.dumps(data))
        resp = r.text
        print(resp)
        order_id = json.loads(resp)['data']
        order_newList.append(order_id)
        code = json.loads(resp)["code"]
        assert code == 200

    @pytest.mark.skip(reason='暂时跳过')
    def test_orderDel(self):
        Authorization = 'Bearer ' + get_token
        Cookie = 'rememberMe=true; Admin-Expires-In=720; username=admin1; ' \
                 'password=xx/CUcU901BZz5TrPYf2NkDkHUEdaOg==; ' \
                 'Admin-Token=' + get_token
        headers = {
            "Authorization": Authorization,
            "Cookie": Cookie,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
                          "Chrome/103.0.0.0 Safari/537.36",
            "tenantId": "1573493506460860417",
            "Content-Type": "application/json"
        }
        del_url = 'http://192.168.3.156/dev-api/crm/order/delete'
        idsDel1 = order_newList[1]
        idsDel2 = order_newList[2]
        data = {
            "ids": [
                idsDel1
            ]
        }
        print(data)
        rOne = requests.post(url=del_url, headers=headers, data=json.dumps(data))
        print("********************")
        if idsDel1:
            assert json.loads(rOne.text)['code'] == 200

        data = {
            "ids": [
                idsDel2
            ]
        }
        print(data)
        rtwo = requests.post(url=del_url, headers=headers, data=json.dumps(data))
        print("/////////////////////")
        if idsDel2:
            assert json.loads(rtwo.text)['code'] == 200
            print(rtwo.text)


if __name__ == "__main__":
    pytest.main(['-sqx', 'test_order.py'])
