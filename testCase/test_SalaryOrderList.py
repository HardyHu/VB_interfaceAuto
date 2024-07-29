# -*- coding:utf-8 -*-

"""
197ISC系统的
销售订单接口处理
涉及列表查询、新增、审核、关闭、结案、编辑、业务状态查询等操作
author_Hardy
"""
import datetime
import json

import pytest
import requests

from user.file_operation import ymlOperation

get_token = ymlOperation.read_yaml()['197_Env_Test'].get('197_token')
# 切换项目
get_host = ymlOperation.read_yaml()['197_Env_Test'].get('Interface_Api_Host').replace('plm', 'isc')

dateT = datetime.datetime.now()
t_one = (dateT + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")  # 延迟一天的单据日期，注意格式化成str后再截取
t_two = (dateT + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
t_thirty = (dateT + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")

Authorization = 'Bearer ' + get_token
headers = {
    "Authorization": Authorization,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}


def deal_root():
    search_operate = get_host + 'salaryOrder/page'  # remember to change main url
    add_op = get_host + 'salaryOrder/add'
    order_approve = get_host + 'salaryOrder/approve'  # 审批操作的接口
    close_op = get_host + 'salaryOrder/close'
    closeCase = get_host + 'salaryOrder/closeCase'
    edit_op = get_host + 'salaryOrder/edit'
    itemStatus = get_host + 'salaryOrder/itemStatus'
    order_disApprove = get_host + 'salaryOrder/disApprove'  # 反审操作

    return search_operate, add_op, order_approve, close_op, closeCase, edit_op, itemStatus, order_disApprove


def setup():
    print("\n初始化OK.")


def teardown():
    print("数据已清理.\n")


def test_search():
    params = {
        "currentPageSize": 10,
        "currentPage": 1,
        # "searchWord": "",
        # "status": ""
    }
    resp = requests.post(deal_root()[0], headers=headers, data=json.dumps(params))  # , timeout=10
    print(resp.text)
    content = json.loads(resp.text)

    dataList = []
    dataNum = len(content["data"]["records"])
    for i in range(dataNum):
        # 获取创建者昵称
        j = content["data"]["records"][i]["createName"]
        print(j)
        dataList.append(j)
    # 判断创建人是token登陆的超哥账号，且创建人的昵称正确
    assert "马兴超" in dataList


@pytest.mark.parametrize(
    'orgName, billDate, customerCode, customerName, currencyCode, currencyName, settlementCode,'
    ' settlementName, address, batch, salaryQuantity, price, deliveryDate',
    [(
            "产品与测试部", str(dateT)[:10],
            '老板黄鹤', '老板黄鹤',
            'rmb', '人民币',
            'CASH', '现金',
            '湖南省邵阳市武冈市吴刚兄',
            'AUTO_test_' + '007',
            66,
            '1',
            str(t_two)[:10]
    ),
        (
                "产品与测试部", str(dateT)[:10],
                '老板黄鹤', '老板黄鹤',
                'rmb', '人民币',
                'CASH', '现金',
                '湖南省邵阳市武冈市吴刚兄',
                'AUTO_test_' + '008',
                50,
                '2',
                str(t_thirty)[:10]
        )])
def test_add(orgName, billDate, customerCode, customerName, currencyCode, currencyName, settlementCode,
             settlementName, address, batch, salaryQuantity, price, deliveryDate):
    print(deal_root()[1])
    params = {
        "billType": "STANDARD",
        "billDate": billDate,
        "orgCode": "Product&Test",
        "orgName": orgName,
        "customerCode": customerCode,
        "customerName": customerName,
        "salesmanCode": "587",
        "salesmanName": "马兴超",
        "followCode": "",
        "followName": "",
        "currencyCode": currencyCode,
        "currencyName": currencyName,
        "settlementCode": settlementCode,
        "settlementName": settlementName,
        "includingTax": "true",
        "deliveryMethod": "HOME_DELIVERY",
        "address": address,
        "changeReason": "",
        "projectCode": "",
        "projectName": "",
        "contractCode": "",
        "contractName": "",
        "remark": "",
        "attrList": [],
        "itemList": [
            {
                "seq": 1,
                "materialCode": "Y0818003",
                "materialName": "钢铁",
                "specParameters": "CXX",
                "model": "TV4",
                "batch": batch,
                "unitCode": "DW003",
                "unitName": "千克",
                "salaryQuantity": salaryQuantity,
                "inExQuantity": 0,
                "exQuantity": "",
                "price": price,
                "amount": (salaryQuantity * int(price)),
                "itemStatusName": "",
                "deliveryDate": deliveryDate,
                "gift": "false",
                "packagingSpecification": "",
                "specialRequest": "",
                "customerOrder": "",
                "customerMaterialCode": "",
                "remark": ""
            }
        ]
    }

    resp = requests.post(deal_root()[1], headers=headers, data=json.dumps(params))  # params
    print(resp.text)
    # 日志打印出日期格式是否正确
    print(str(t_thirty)[:10])
    contentAdd = json.loads(resp.text)
    assert contentAdd['code'] == 200


def test_itemStatus0():
    resp = requests.get(deal_root()[6], headers=headers, timeout=10)
    print(resp.text)
    # 将收集的响应值放入key值，检验value，可以逐个校验
    response = json.loads(resp.text)
    TOBE_DELIVERY = response['data']['TOBE_DELIVERY']

    assert TOBE_DELIVERY == '待交货'


def test_itemStatus1():
    resp = requests.get(deal_root()[6], headers=headers, timeout=10)
    print(resp.text)
    # 将收集的响应值放入key值，检验value，可以逐个校验
    response = json.loads(resp.text)
    PARTIAL_DELIVERY = response['data']['PARTIAL_DELIVERY']

    assert PARTIAL_DELIVERY == '部分交货'


def test_itemStatus2():
    resp = requests.get(deal_root()[6], headers=headers, timeout=10)
    print(resp.text)
    # 将收集的响应值放入key值，检验value，可以逐个校验
    response = json.loads(resp.text)
    IN_DELIVERY = response['data']['IN_DELIVERY']

    assert IN_DELIVERY == '交货中'


def test_itemStatus3():
    resp = requests.get(deal_root()[6], headers=headers, timeout=10)
    print(resp.text)
    # 将收集的响应值放入key值，检验value，可以逐个校验
    response = json.loads(resp.text)
    CLOSED = response['data']['CLOSED']

    assert CLOSED == '已关闭'


def test_itemStatus4():
    resp = requests.get(deal_root()[6], headers=headers, timeout=10)
    print(resp.text)
    # 将收集的响应值放入key值，检验value，可以逐个校验
    response = json.loads(resp.text)
    CLOSE_CASE = response['data']['CLOSE_CASE']

    assert CLOSE_CASE == '已结案'


@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_ISC_approve():
    """审核：
    # 轮换值，查出数据如果是已审核，则进行反审操作，如果是待审核，则直接审核通过。以返回值为200检验审核通过
    """
    #  对单号SD0320240710002 进行查询
    # global finalRes
    params = {
        "currentPageSize": 10,
        "currentPage": 1,
        "billCode": "SD0320240710002"
        # "searchWord": "",
        # "status": ""
    }
    resp = requests.post(deal_root()[0], headers=headers, data=json.dumps(params))  # , timeout=10
    print(resp.text)
    content = json.loads(resp.text)
    checkStatus = content["data"]["records"][0]["statusName"]

    preUrl = deal_root()[7]
    if checkStatus == "待审核":
        preUrl = deal_root()[2]

    print(f"此时待操作的是《{checkStatus}》 与 {preUrl} 《地址》.")
    #  即单号SD0320240710002 的ID，切记一定要与上方查询的数据一致
    data = {
        "ids": [
            "1810735669148745730"
        ]
    }
    try:
        if preUrl is not None:
            finalRes = requests.post(preUrl, headers=headers, data=json.dumps(data))
    finally:
        pass

    assert json.loads(finalRes.text)["code"] == 200


if __name__ == '__main__':
    pytest.main(["-sqx", "test_SalaryOrderList.py"])
