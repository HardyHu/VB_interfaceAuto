# -*- coding:utf-8 -*-

"""
开票的增删改查，
初期仅实现对新建和删除的用例校验
"""
import datetime
import json
import random
import time
import pytest
import requests

global new_list

new_list = []


now_time = datetime.datetime.now()
time_str = now_time.strftime("%Y-%m-%d %H:%M:%S")
t = time_str[:10] + "T" + time_str[11:] + ".000Z"

t_one = (now_time + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
time_joinOne = t_one[:10] + "T23:00:00.000Z"

t_two = (now_time + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
time_joinTwo = t_two[:10] + "T23:00:00.000Z"

with open('access_token.txt', 'r') as f:
    get_token = f.read()
get_token = get_token.strip()


@pytest.fixture(params=[t, time_joinOne, time_joinTwo], name="demo")
def ready(request):
    """
    需要参数化：t, time_joinOne, time_joinTwo
    """
    yield request.param


class Test_Invoice(object):
    def setup(self):
        print('测试用例已开始')

    def teardown(self):
        print('测试用例已结束')

    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_invoiceSave(self, demo):  # , demo
        global headers
        Authorization = 'Bearer ' + get_token
        Cookie = 'rememberMe=true; Admin-Expires-In=720; username=admin1; ' \
                 'password=xxx==; ' \
                 'Admin-Token=' + get_token
        headers = {
            "Authorization": Authorization,
            "Cookie": Cookie,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
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
            "rise": "woWu66668888",
            "riseType": 1,
            "status": 1,
            "type": 1
        }
        r = requests.post(url=save_url, headers=headers, data=json.dumps(data))
        print("********************")
        print(r.text)
        invoice_id = json.loads(r.text)['data']
        new_list.append(invoice_id)
        assert json.loads(r.text)["code"] == 200

    # @pytest.mark.skip()
    def test_invoiceDel(self):
        del_url = 'http://192.168.3.156/dev-api/crm/invoice/delete'

        print(new_list)
        for content in new_list[-2:]:  # 取倒数三个数据进行删除操作
            data = {
                "ids": [content]
            }
            time.sleep(1)
            resp = requests.post(url=del_url, headers=headers, data=json.dumps(data))
            assert resp.json()['code'] == 200  # json.loads(resp.text)


if __name__ == '__main__':
    """-rs : Show skipped"""
    pytest.main(['-svx', 'test_invoice.py'])
