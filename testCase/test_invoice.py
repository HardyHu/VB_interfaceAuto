# -*- coding:utf-8 -*-

"""
开票的增删改查，
初期仅实现对新建和删除的用例校验
"""
import pytest
import requests
import json
import datetime
import random

global order_newlist

t2 = datetime.datetime.now()
t2 = t2.strftime("%Y-%m-%d %H:%M:%S")
t = t2[:10] + "T" + t2[11:] + ".000Z"

newt = datetime.datetime.now()
t1 = (newt + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
dtjoin1 = t1[:10] + "T23:00:00.000Z"

t3 = (newt + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
dtjoin2 = t3[:10] + "T23:00:00.000Z"

with open('access_token.txt', 'r') as f:
    get_token = f.read()
get_token = get_token.strip()


@pytest.fixture(params=[t, dtjoin1, dtjoin2], name="demo")
def ready(request):
    """
    需要参数化：dtjoin1，mynum，dtjoin2
    """
    yield request.param


class Test_Invoice(object):
    def setup(self):
        print('测试用例已开始')

    def teardown(self):
        print('测试用例已结束')

    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_invoicesave(self, demo):  # , demo
        global headers
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
        save_url = 'http://192.168.3.156/dev-api/crm/invoice/save'
        date = demo
        data = {
            "account": "62287700100132071",
            "addressId": 1581907136998830083,  # 1570238472939667458 开票地址
            "amount": 7200000.00,
            "bank": "招商银行",
            "contacts": "市卫健委",
            "contactsMode": "13866668888",
            "contractId": 1573601475999346690,  # *09240010
            "contractNo": "HT202209240010",
            "customerId": 1580852611038867457,  # 测试大佬，张楚岚1570238472918695937,
            "date": date,  # 开票日期
            "identifyCode": "91330000142916567N",  # 纳税识别码 91330000142916567N
            "mailAddress": "一帆风顺，驱邪避灾，万事大吉大利！",
            "orderId": 1580820787574231041,
            "orderNo": "XS202210140027",
            "phone": "0755-626626",
            "remark": "祝大家都发财、有福气、心情愉快、事业有成、家族兴旺、婚姻美满、福如东海、前途似锦！",
            "rise": "woqu66668888",
            "riseType": 1,
            "status": 1,
            "type": 1
        }
        r = requests.post(url=save_url, headers=headers, data=json.dumps(data))
        resp = r.text
        print("********************")
        print(resp)
        invoice_id = json.loads(resp)['data']
        order_newlist = []
        order_newlist.append(invoice_id)

        assert json.loads(resp)["code"] == 200

    @pytest.mark.skip()
    def test_invoicedel(self):
        global idsdel1, idsdel2
        del_url = 'http://192.168.3.156/dev-api/crm/invoice/delete'
        if len(order_newlist) >= 3:
            idsdel1 = order_newlist[1]
            idsdel2 = order_newlist[2]
        data = {
            "ids": [idsdel1]
        }
        rone = requests.post(url=del_url, headers=headers, data=json.dumps(data))
        if idsdel1:
            print("用例：test_invoicedel 第一次")
            assert json.loads(rone.text)['code'] == 200
        data = {
            "ids": [idsdel2]
        }

        rtwo = requests.post(url=del_url, headers=headers, data=json.dumps(data))
        if idsdel2:
            print("用例：test_invoicedel 第二次")
            assert json.loads(rtwo.text)['code'] == 200
            print(rtwo.text, 'Check Over!')


if __name__ == '__main__':
    """-rs : Show skipped"""
    pytest.main(['-rsvx', 'test_invoice.py'])
