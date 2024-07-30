# -*- coding:utf-8 -*-

"""
197ISC系统的
发货通知单接口处理
涉及列表查询、新增、审核、关闭、结案、编辑、业务状态查询等操作
author_Hardy
"""
import datetime
import json
import random

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
# 销售出库信息单
saleOutList = ['XOUT0320240603001', 'XOUT0320240326004', 'XOUT0320240326003', 'XOUT0320240326002', 'XOUT0320240326001',
               'XOUT0320240125001',
               'XOUT0320240124004', 'XOUT0320240124003', 'XOUT0320240124002', 'XOUT0320240124001']

Authorization = 'Bearer ' + get_token
headers = {
    "Authorization": Authorization,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}


def right_url():
    search_operate = get_host + '/salaryReconcile/page'  # 分页查询
    add_op = get_host + 'salaryReconcile/add'
    order_approve = get_host + '/salaryReconcile/approve'  # 审批操作的接口
    order_disApprove = get_host + '/salaryReconcile/disApprove'  # 反审操作

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
    'reconcileEndDate, reconcileStartDate, paymentCustomerCode, paymentCustomerName, billCode, resourceBillCode',
    [(
             str(t_one)[:10],
             "2021-01-01",
             "测试购货单位",
             "测试购货单位",
             random.choices(saleOutList)[0],
             random.choices(saleOutList)[0]
     ),
     (
             str(t_two)[:10],
             "2022-06-01",
             "朱伟个人的客户",
             "朱伟个人的客户",
             random.choice(saleOutList),
             random.choice(saleOutList)
     )])
def test_add(reconcileEndDate, reconcileStartDate, paymentCustomerCode,
             paymentCustomerName, billCode, resourceBillCode):
    print(right_url()[1])
    params = {
        "customerCode": "TY0003",
        "customerName": "财务购货单位一",
        "salesmanCode": "TEST001",
        "salesmanName": "张谊文",
        "currencyCode": "rmb",
        "currencyName": "人民币",
        "settlementCode": "003",
        "settlementName": "分期付款",
        "paymentCustomerCode": paymentCustomerCode,
        "paymentCustomerName": paymentCustomerName,
        "remark": "未知程序错误.",
        "itemList": [
            {
                "tenantId": "1586979014478311425",
                "tenantName": "深圳优制云工业互联网有限公司",
                "createBy": "",
                "createName": "",
                "createTime": "",
                "updateBy": "",
                "updateName": "",
                "updateTime": "",
                "remark": "",
                "id": "1797524762822279170",
                "itemId": "1797524763052965890",
                "status": "APPROVED",
                "billCode": billCode,  # 123test

                "billType": "STANDARD",
                "billDate": "2024-06-03",
                "customerName": "财务购货单位一",
                "deptName": "",
                "salesmanName": "张谊文",
                "warehouseKeeperName": "张谊文",
                "redBlue": "BLUE",
                "currencyName": "人民币",
                "settlementName": "分期付款",
                "seq": 1,
                "materialCode": "RCWL002",
                "materialName": "洗碗机",
                "specParameters": "60x85x60",
                "model": "全自动",
                "batch": "P0001",
                "unitCode": "DW001",
                "unitName": "个",
                "shouldExQuantity": 100,
                "actualExQuantity": 100,
                "price": 500,
                "amount": 50000,
                "warehouseName": "宝安仓库222",
                "positionName": "",
                "projectName": "",
                "resourceBillType": "SALARY_EX_WAREHOUSE",
                "resourceBillCode": resourceBillCode,  # 需要源单据，记得优化处理
                "resourceSeq": 1,
                "orderBillType": "",
                "orderBillCode": "",
                "orderSeq": "",
                "customerBillCode": "",
                "customerMaterialCode": "",
                "realQuantity": 100,
                "inRedQuantity": 0,
                "redFreeQuantity": 100,
                "statusName": "已审核",
                "billTypeName": "标准销售出库",
                "redBlueName": "蓝字",
                "resourceBillTypeName": "发货通知单",
                "orderBillTypeName": "",
                "deliveryBillCode": "DN0320240517002",
                "salaryBillCode": "",
                "warehouseExQuantity": 100,
                "warehouseExDate": "2024-06-03"
            }
        ],
        "reconcileStartDate": reconcileStartDate,
        "reconcileEndDate": reconcileEndDate
    }

    resp = requests.post(right_url()[1], headers=headers, data=json.dumps(params))  # params
    print(resp.text)
    contentAdd = json.loads(resp.text)
    assert contentAdd['code'] == 200


if __name__ == '__main__':
    pytest.main(["-sqx", "test_salaryReconcile.py"])
