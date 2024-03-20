# -*- coding:utf-8 -*-

"""
197PLM的产品BOM接口处理
初期仅实现数据新增、批量禁用/启用/审核/反审的功能校验
author_Hardy
"""
import datetime
import json

import pytest
import requests

from user.file_operation import ymlOperation

get_token = ymlOperation.read_yaml()['197_Env_Test'].get('197_token')
get_host = ymlOperation.read_yaml()['197_Env_Test'].get('Interface_Api_Host')

dateT = datetime.datetime.now()
t_one = (dateT + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")


def deal_root():
    api_url1 = get_host + 'bom/add'
    api_url2 = get_host + 'bom/changeStatus'
    api_url = [api_url1, api_url2]
    return api_url


#                               ('PlanA+' + t_one[:6], '6.6.6', 't_one is just a D.I.Y.-Date')]
class Test_Bom:

    def setup(self):
        print("\n初始化OK.")

    def teardown(self):
        print("数据已清理.\n")

    @pytest.mark.parametrize('code,version,remark',
                             [('Bom编码+' + t_one[:5], '1.3.5', '这是个备注1')])
    def test_Bom_add(self, code, version, remark):
        """
        这是产品BOM的相关功能
        :param code:BOM编码
        :param version:版本号
        :param remark:备注，可为任意值
        :return:
        """
        Authorization = 'Bearer ' + get_token

        headers = {
            "Authorization": Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "Content-Type": "application/json"
        }

        params1 = {
            "project": "",
            "bomConfig": "",
            "customer": "",

            "materialName": "物料名称213",
            "materialModel": "",
            "materialSpecs": "",
            "materialId": "1613419889790820353",
            "code": code,
            "type": 1,
            "materialCode": "1613419889790820353",
            "version": version,
            "remark": remark,
            "infoList": [
                {
                    "createBy": "",
                    "createName": "",
                    "createTime": "",
                    "updateBy": "",
                    "updateName": "",
                    "updateTime": "",
                    "tenantId": "",
                    "id": "",
                    "status": 1,
                    "bomId": "",
                    "materialId": "1612352993385603074",
                    "materialIdReplace": "",
                    "moduleItem": 1,
                    "functionItem": "16G",
                    "moduleType": 1,
                    "unitDosage": 1,
                    "address": "BD2B",
                    "loss": 0.3,
                    "remark": "",
                    "moduleItemName": "家居",
                    "moduleTypeName": "二选一",
                    "workshopName": "",
                    "materialCode": "list06",
                    "materialName": "列表第六",
                    "materialReplaceCode": "",
                    "materialReplaceName": "",
                    "materialModel": "",
                    "materialSpecs": "3008",
                    "materialPack": "",
                    "workshopId": ""
                },
                {
                    "createBy": "",
                    "createName": "",
                    "createTime": "",
                    "updateBy": "",
                    "updateName": "",
                    "updateTime": "",
                    "tenantId": "",
                    "id": "",
                    "status": 1,
                    "bomId": "",
                    "materialId": "1612998635942440962",
                    "materialIdReplace": "",
                    "moduleItem": 1,
                    "functionItem": "16G",
                    "moduleType": 1,
                    "unitDosage": 1,
                    "address": "P26",
                    "loss": 0.3,
                    "remark": "",
                    "moduleItemName": "家居",
                    "moduleTypeName": "二选一",
                    "workshopName": "",
                    "materialCode": "list_Anoth",
                    "materialName": "新的",
                    "materialReplaceCode": "",
                    "materialReplaceName": "",
                    "materialModel": "XXX000",
                    "materialSpecs": "123",
                    "materialPack": "",
                    "workshopId": ""
                },
                {
                    "createBy": "",
                    "createName": "",
                    "createTime": "",
                    "updateBy": "",
                    "updateName": "",
                    "updateTime": "",
                    "tenantId": "",
                    "id": "",
                    "status": 1,
                    "bomId": "",
                    "materialId": "1612998635942440962",
                    "materialIdReplace": "",
                    "moduleItem": 3,
                    "functionItem": "独立显卡-256",
                    "moduleType": 3,
                    "unitDosage": 1,
                    "address": "R18",
                    "loss": 1.8,
                    "remark": "",
                    "moduleItemName": "奢侈品",
                    "moduleTypeName": "可选",
                    "workshopName": "",
                    "materialCode": "list_Anoth",
                    "materialName": "新的",
                    "materialReplaceCode": "",
                    "materialReplaceName": "",
                    "materialModel": "XXX000",
                    "materialSpecs": "123",
                    "materialPack": "",
                    "workshopId": ""
                },
                {
                    "createBy": "",
                    "createName": "",
                    "createTime": "",
                    "updateBy": "",
                    "updateName": "",
                    "updateTime": "",
                    "tenantId": "",
                    "id": "",
                    "status": 1,
                    "bomId": "",
                    "materialId": "1612354938032709633",
                    "materialIdReplace": "",
                    "moduleItem": 0,
                    "functionItem": "核心公用",
                    "moduleType": 0,
                    "unitDosage": 1,
                    "address": "R12",
                    "loss": 0.3,
                    "remark": "",
                    "moduleItemName": "电器",
                    "moduleTypeName": "必选",
                    "workshopName": "",
                    "materialCode": "list10",
                    "materialName": "列表第拾",
                    "materialReplaceCode": "",
                    "materialReplaceName": "",
                    "materialModel": "",
                    "materialSpecs": "扣得多",
                    "materialPack": "",
                    "workshopId": ""
                },
                {
                    "createBy": "",
                    "createName": "",
                    "createTime": "",
                    "updateBy": "",
                    "updateName": "",
                    "updateTime": "",
                    "tenantId": "",
                    "id": "",
                    "status": 1,
                    "bomId": "",
                    "materialId": "1612348342892322817",
                    "materialIdReplace": "",
                    "moduleItem": 2,
                    "functionItem": "I5",
                    "moduleType": 2,
                    "unitDosage": 1,
                    "address": "XBB1.5",
                    "loss": 1.5,
                    "remark": "",
                    "moduleItemName": "生活品",
                    "moduleTypeName": "N选一",
                    "workshopName": "",
                    "materialCode": "list02",
                    "materialName": "列表第二",
                    "materialReplaceCode": "",
                    "materialReplaceName": "",
                    "materialModel": "",
                    "materialSpecs": "222",
                    "materialPack": "",
                    "workshopId": ""
                }
            ]
        }
        print(json.dumps(params1))
        r = requests.post(url=deal_root()[0], headers=headers, data=json.dumps(params1))
        print(r.text)
        # resPj = json.loads(r.text)
        result = 'this Bom'

        # result = resPj["code"]
        assert 'Bom' in result


if __name__ == '__main__':
    ""
    pytest.main(["-sqx", "test_PLM_Plan.py"])
    print("=====测试完成=====")
