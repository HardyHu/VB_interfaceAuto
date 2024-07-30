# -*- coding:utf-8 -*-

"""
197ISC系统的
发货通知单接口处理
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
t_one = (dateT + datetime.timedelta(days=5)).strftime("%Y-%m-%d %H:%M:%S")  # 延迟 - 五 - 天的单据日期，注意格式化成str后再截取
t_two = (dateT + datetime.timedelta(days=15)).strftime("%Y-%m-%d %H:%M:%S")
t_thirty = (dateT + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")

Authorization = 'Bearer ' + get_token
headers = {
    "Authorization": Authorization,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}


def right_url():
    search_operate = get_host + '/deliveryAdvice/page'  # 分页查询
    add_op = get_host + 'deliveryAdvice/add'
    order_approve = get_host + '/deliveryAdvice/approve'  # 审批操作的接口
    order_disApprove = get_host + '/deliveryAdvice/disApprove'  # 反审操作

    return search_operate, add_op, order_approve, order_disApprove


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
    resp = requests.post(right_url()[0], headers=headers, data=json.dumps(params))  # , timeout=10
    print(resp.text)
    content = json.loads(resp.text)

    dataList = []
    dataNum = len(content["data"]["records"])
    for i in range(dataNum):
        # 获取创建者昵称
        j = content["data"]["records"][i]["salesmanName"]
        print(j)
        dataList.append(j)
    # 注意不同，此处校验的是业务员的昵称正确
    assert "马兴超" in dataList


@pytest.mark.parametrize(
    'deptCode, deptName, billDate, paymentDate',
    [(
            "Product&Test",
            "产品与测试部",
            str(t_one)[:10],
            str(t_two)[:10]
    ),
        (
                "TY002",
                "研发部",
                str(t_one)[:10],
                str(t_thirty)[:10]
        )])
def test_add(deptCode, deptName, billDate, paymentDate):
    print(right_url()[1])
    params = {
        "billType": "STANDARD",
        "businessType": "SELF",
        "billDate": billDate,
        "orgCode": "",
        "orgName": "",
        "deptCode": deptCode,  # "Product&Test",
        "deptName": deptName,
        "customerCode": "老板黄鹤",
        "customerName": "老板黄鹤",
        "salesmanCode": "587",
        "salesmanName": "马兴超",
        "followCode": "12",
        "followName": "胡智凯",
        "currencyCode": "rmb",
        "currencyName": "人民币",
        "settlementCode": "CASH",
        "settlementName": "现金",
        "includingTax": "true",
        "contacts": "老板黄鹤",
        "phoneNumber": "18894186666",
        "deliveryMethod": "HOME_DELIVERY",
        "address": "湖南省邵阳市武冈市吴刚兄",
        "paymentCustomerCode": "",
        "paymentCustomerName": "",
        "supplierCode": "",
        "supplierName": "",
        "remark": "",
        "attrList": [],
        "itemList": [
            {
                "id": "19",
                "tenantId": "1586979014478311425",
                "code": "B0818001",
                "name": "洗涤装置",
                "model": "TV0",
                "specParameters": "XML",
                "brand": "pinPAI",
                "encapsulation": "FZ007",
                "materialCategoryId": "15",
                "sealedSampleIcon": "http://192.168.3.156:9000/hh-wb/2024/04/25/汉长安_20240425110822A019.jpg",
                "stockKeepingUnitId": 13,
                "shelfLife": 0,
                "salesUnitId": 13,
                "minimumPackaging": 1,
                "purchasingCycle": 0,
                "purchaseLeadTime": 0,
                "logisticsCycle": 0,
                "purchaseUnitId": 13,
                "productionUnitId": 13,
                "standardLoss": 2,
                "inspectionExemption": "false",
                "status": 0,
                "approvalStatus": 1,
                "productionAttr": 1,
                "materialProperty": 61,
                "generalAttr": 0,
                "batchManagement": 0,
                "materialGrade": 1,
                "processProperties": 3,
                "materialCategoryCode": "TY0818001",
                "materialCategoryName": "成品配件",
                "stockKeepingUnitCode": "DW001",
                "stockKeepingUnitName": "个",
                "salesUnitCode": "DW001",
                "salesUnitName": "个",
                "purchaseUnitName": "个",
                "productionUnitCode": "DW001",
                "productionUnitName": "个",
                "materialPropertyName": "成品",
                "createdBy": "15013734208",
                "createdTime": "2023-08-18T16:09:26+08:00",
                "lastModifiedBy": "15013734208",
                "lastModifiedTime": "2024-04-25T11:08:47+08:00",
                "materialCode": "B0818001",
                "materialName": "洗涤装置",
                "unitName": "个",
                "unitCode": "DW001",
                "gift": "false",
                "salaryQuantity": 10,
                "seq": 1,
                "price": "2",
                "amount": "20.00",
                "deliveryDate": "2024-07-30"
            }
        ],
        "projectCode": "",
        "projectName": "",
        "paymentDate": paymentDate
    }

    resp = requests.post(right_url()[1], headers=headers, data=json.dumps(params))  # params
    print(resp.text)
    contentAdd = json.loads(resp.text)
    assert contentAdd['code'] == 200


if __name__ == '__main__':
    pytest.main(["-sqx", "test_DeliveryAdvice.py"])
