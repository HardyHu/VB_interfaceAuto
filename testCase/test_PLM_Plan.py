# -*- coding:utf-8 -*-

"""
197PLM的列表接口处理
初期仅实现数据刷新校验
author_Hardy
"""
import datetime
import json
import random

import pytest
import requests

from user.file_operation import ymlOperation

get_token = ymlOperation.read_yaml()['197_Env_Test'].get('197_token')
get_host = ymlOperation.read_yaml()['197_Env_Test'].get('Interface_Api_Host')

dateT = datetime.datetime.now()
t_one = (dateT + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
t_two = (dateT + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
t_thirty = (dateT + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
later_date0 = t_one[:10] + "T10:00:00.000Z"
later_date1 = t_two[:10] + "T11:00:00.000Z"
later_date2 = t_thirty[:10] + "T13:00:00.000Z"


def deal_root():
    api_url = get_host + 'plmProjectPlanEntity/insert'
    return api_url


class Test_PM:

    def setup(self):
        print("\n初始化OK.")

    def teardown(self):
        print("数据已清理.\n")

    @pytest.mark.parametrize('demo,start,end',
                             [('PlanB+' + str(random.randint(10000, 20000)), later_date1, later_date2),
                              ('PlanA+' + str(random.randint(10000, 10100)), later_date0, later_date1)])
    def test_PM_insert(self, demo, start, end):
        """
        项目管理里的项目计划，此为新增计划
        :param demo:计划的编码
        :param start:计划开始日期
        :param end:计划的结束日期
        """
        Authorization = 'Bearer ' + get_token

        headers = {
            "Authorization": Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "Content-Type": "application/json"
        }

        params = {
            "responsibleRole": 6,
            "responsibleName": "27",  # 注意，此责任人与前面的责任角色都是提前在项目创建时绑定好了的，所以项目Id变，也要因之而变
            "planNo": demo,
            "subordinationStage": "1",
            "projectId": "20",
            "planStartTime": start,
            "planType": "2",
            "planName": "成龙A计划~",
            "outputType": "0",
            "milestoneFlag": "0",
            "outputClassify": "2",
            "planDetailDesc": "ThoseBOSS cuts costs every day, and sooner or later, nothing can achieve good results."
                              " He is the first disgusting person",
            "resourceAssistance": "资源协助位+1！",
            "remark": "",
            "planEndTime": end
        }
        r = requests.post(url=deal_root(), headers=headers, data=json.dumps(params))
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

    pytest.main(["-sqx", "test_PLM_Plan.py"])
    print("=====测试完成=====")
