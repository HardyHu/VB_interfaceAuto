# -*- coding:utf-8 -*-

"""
197PLM的项目角色接口处理
初期仅实现数据刷新校验
author_Hardy
"""
import datetime
import json
import random
import pytest
import requests

from user.file_operation import ymlOperation

global newlist
newlist = []
L = ['睿智的', '果敢的', '奸诈的', '忠诚的', '清爽的', '豁达的', '胆小的', '臃肿的']

get_token = ymlOperation.read_yaml()['197_Env_Test'].get('197_token')
get_host = ymlOperation.read_yaml()['197_Env_Test'].get('Interface_Api_Host')

dateT = datetime.datetime.now()
t_one = (dateT + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
t_two = (dateT + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
t_thirty = (dateT + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")


def deal_root():
    add_url = get_host + 'projectRole/add'  # remember to change main url
    role_pageList = get_host + 'projectRole/pageList'
    role_update = get_host + 'projectRole/update'
    return add_url, role_pageList, role_update


class Test_ProRole:

    def setup(self):
        print("\n初始化OK.")

    def teardown(self):
        print("数据已清理.\n")

    @pytest.mark.parametrize('jobDescription, name, remark',
                             [(
                                     '职责是' + t_two,
                                     '名' + random.choice(L) + str(random.randint(8000, 12000)),
                                     '备注是下个月' + t_thirty),
                                 (
                                         '职责是' + t_one,
                                         '子曰' + random.choice(L) + str(random.randint(10000, 10100)),
                                         '备注是下个月' + t_thirty + '好的备注。')])  #
    def test_role_add(self, jobDescription, name, remark):
        Authorization = 'Bearer ' + get_token

        headers = {
            "Authorization": Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "Content-Type": "application/json"
        }

        params = {
            # "id": 0,
            "jobDescription": jobDescription,
            "name": name,
            "remark": remark
        }
        r = requests.post(url=deal_root()[0], headers=headers, data=json.dumps(params))
        print(r.text)
        resPj = json.loads(r.text)

        result = resPj["code"]
        assert result == 200

    def test_role_list(self):
        """
        校验第一页的数据是否准确
        :return: a list will be seeing
        """
        Authorization = 'Bearer ' + get_token

        headers = {
            "Authorization": Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "Content-Type": "application/json"
        }

        params = {
            "current": 1,
            "searchWord": "",
            "size": 10
        }
        r = requests.post(url=deal_root()[1], headers=headers, data=json.dumps(params))
        # print(r.text)
        resp = json.loads(r.text)
        checkNum = len(resp['data']['records'])

        assert checkNum == 10

    def test_standby_value(self):
        """
        按关键值搜索，获取结果
        :return: a list will be seeing
        """
        Authorization = 'Bearer ' + get_token

        headers = {
            "Authorization": Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "Content-Type": "application/json"
        }

        params = {
            "current": 1,
            "searchWord": "产品大佬啊",
            "size": 10
        }
        r = requests.post(url=deal_root()[1], headers=headers, data=json.dumps(params))
        # print(r.text)
        resp = json.loads(r.text)

        roleData = resp['data']['records'][0]
        newlist.append(roleData)
        print(f'{newlist=}')
        assert "一切" in roleData['remark']

    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_role_change(self):
        """
        尝试修改内容
        :return: change contents in this stage.
        """
        Authorization = 'Bearer ' + get_token
        headers = {
            "Authorization": Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "Content-Type": "application/json"
        }
        # print(newlist)
        data = newlist[0]

        if data['jobDescription'] == "位高权重a":
            jobName = '呵呵，位高权重易滥用'
            remark = '一切不堪直视'
        else:
            jobName = "位高权重a"
            remark = "决定了一切。！"
        # print(jobName, f'{remark=}')

        params = {
            "id": 7,
            "name": "产品大佬啊",
            "jobDescription": jobName,
            "remark": remark
        }
        right_url = deal_root()[2]
        r = requests.post(url=right_url, headers=headers, data=json.dumps(params))
        print(r.text)

        resp = json.loads(r.text)
        result = resp["code"]
        assert result == 200


if __name__ == '__main__':
    '''
    -s：显示程序中的 print/logging 输出。
    -v：丰富信息模式, 输出更详细的用例执行信息。
    -k：运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行 XX.py 中包含 add 的测试用例。
    -q：简单输出模式, 不输出环境信息。
    -x：出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
    '''

    pytest.main(["-sqx", "test_PLM_projectRole.py"])

    # A = Test_ProRole
    # A.test_standby_value(A)
    # print(A.test_role_change(A))
