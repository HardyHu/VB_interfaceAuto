# -*- coding:utf-8 -*-

"""
回款的增删改查， -- 对接移动端，较为重要
初期仅实现对新建和删除的用例校验
"""
import pytest
import requests
import json
import datetime

t = datetime.datetime.now()

t2 = (t + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
dtjoin1 = t2[:10] + "T16:00:00.000Z"

t3 = (t + datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")
dtjoin2 = t3[:10] + "T16:00:00.000Z"

with open('access_token.txt', 'r') as f:
    get_token = f.read()
get_token = get_token.strip()


@pytest.fixture(params=[[dtjoin1, dtjoin2, "小小的备注", dtjoin1, "这是个mark"],
                        [dtjoin1, dtjoin2, "微微的备注", dtjoin1, r"这是个mark\|/"],
                        [dtjoin1, dtjoin2, "单据Aa的备注", dtjoin1, r"这是~！@#￥%……&*（）"]], name="demo")
def ready(request):
    """
    需要参数化：paymentPlaneDate1，paymentPlaneDate2，remark，paymentDate，employeeNum
    """
    yield request.param


class Test_Payment(object):
    # @pytest.fixture()
    def setup(self):
        print('测试用例已开始')

    def teardown(self):
        print('测试用例已结束')

    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_PaymentSave(self, demo):
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
        url = "http://192.168.3.156/dev-api/crm/payment/save"
        paymentPlaneDate1 = demo[0]
        paymentPlaneDate2 = demo[1]
        remark = demo[2]
        paymentDate = demo[3]
        remark1 = demo[4]

        # 1574238066577022978
        data = {
            "amount": "12000.00",
            "contractId": "1574238066577022978",
            "contractNum": "HT2022-10-204896",
            "contractAmount": "10000.00",
            "customerId": "1570238472918695937",  # 张楚岚
            "list": [{
                "orderId": "",
                "orderNo": "suibianAdd",
                "amount": "4800",
                "paymentPlanId": "",
                "paymentPlanNo": "JH0002",
                "paymentPlaneAmount": "4800",
                "paymentPlaneDate": paymentPlaneDate1,
                "surplusAmount": "7200",
                "productCode": "4800",
                "remark": "还剩7200"
            }, {
                "orderId": "",
                "orderNo": "Add2",
                "amount": "5200",
                "paymentPlanId": "",
                "paymentPlanNo": "JH0003",
                "paymentPlaneAmount": "5200",
                "paymentPlaneDate": paymentPlaneDate2,
                "surplusAmount": "2000",
                "productCode": "5200",
                "remark": remark
            }],
            "paymentDate": paymentDate,
            "paymentMode": "3",
            "remark": remark1,
            "status": 1,
            "employeeNum": "1000"
        }
        # print(data)

        data = json.dumps(data)
        r = requests.post(url=url, headers=headers, data=data)
        resp = r.text
        print("********************")
        print(resp)
        code = json.loads(resp)["code"]

        assert code == 200


if __name__ == '__main__':
    pytest.main(["-sv", "test_payment.py"])  # "-x",
