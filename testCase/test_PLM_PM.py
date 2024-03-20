# -*- coding:utf-8 -*-

"""
197PLM的列表接口处理
初期仅实现数据刷新校验
author_Hardy
"""
import datetime
import json
import random
import time

import pytest
import requests

from user.file_operation import ymlOperation

randomList = random.sample(range(4, 10), 2)
t = time.localtime()
t2 = time.strftime("%Y-%m-%d %H:%M:%S", t)[:10]

get_token = ymlOperation.read_yaml()['197_Env_Test'].get('197_token')
get_host = ymlOperation.read_yaml()['197_Env_Test'].get('Interface_Api_Host')
# print(get_token, '\n', get_host)

dateT = datetime.datetime.now()
t_zero = (dateT + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
t_two = (dateT + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
t_thirty = (dateT + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
later_date0 = t_zero[:10] + "T10:00:00.000Z"
later_date1 = t_two[:10] + "T11:00:00.000Z"
later_date2 = t_thirty[:10] + "T13:00:00.000Z"


def deal_root():
    api_url = get_host + 'plmProjectManageEntity/insert'
    return api_url


url = deal_root()


class Test_PM:

    def setup(self):
        print("\n初始化OK.")

    def teardown(self):
        print("数据已清理.\n")

    @pytest.mark.parametrize('demo,ht_number,start,end',
                             [('测试up' + str(random.randint(1000, 5001)), 'HT_锦瀚' + t2, later_date1, later_date2),
                              ('测试up' + str(random.randint(900, 1000)), 'HT_优质云' + t2, later_date0, later_date1)])
    def test_PM_insert(self, demo, ht_number, start, end):
        """

        """
        Authorization = 'Bearer ' + get_token

        headers = {
            "Authorization": Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "Content-Type": "application/json"
        }

        params = {
            "manpowerInput": 3,
            "projectPeriod": 1,
            "projectBudget": 500,
            "customerId": "",
            "customerName": "",
            "projectAttachmentsName": "testContent.txt",
            "participationDept": "269",
            "outsourcingSupplier": "4d835bdfd05041cbba302b7d6cbe5a72",
            "projectCode": "test00" + str(random.randint(1000, 5000)),
            "projectName": demo,
            "projectSimpleName": "up",
            "projectType": "1",
            "projectLevel": "0",
            "projectVersion": "V5.87",
            "riskLevel": "0",
            "contractNumber": ht_number,
            "projectAttachments": "http://192.168.3.156:9000/hh-wb/plm/1679364851689/testContent.txt",
            "participationDeptName": "研发部",
            "planStartTime": start,
            "planEndTime": end,
            "outsourcingSupplierName": "给我个",
            "remark": "付服务费的备注",
            "projectContent": "测试"
        }
        r = requests.post(url=url, headers=headers, data=json.dumps(params))
        print(r.text)
        resPj = json.loads(r.text)

        result = resPj["code"]
        assert result == 200


if __name__ == '__main__':
    '''
    -s：显示程序中的 print/logging 输出。
    -v：丰富信息模式, 输出更详细的用例执行信息。
    -k：运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行 XX.py 中包含 add 的测试用例。
    -q：简单输出模式, 不输出环境信息。
    -x：出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
    '''

    pytest.main(["-sqx", "test_PLM_PM.py"])
    print("=====测试完成=====")
