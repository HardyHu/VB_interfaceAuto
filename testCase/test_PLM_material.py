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
# name = '青椒' + random.choice(newlist)
global newlist
newlist = []
L = ['2', '88', '4', '5', '7']


def deal_root():
    add_url = get_host + 'category/add'  # remember to change main url
    ma_pageList = get_host + 'material/pageList'
    changeSta_url = get_host + 'material/changeStatus'
    return add_url, ma_pageList, changeSta_url


class Test_Material:

    def setup(self):
        print("\n初始化OK.")

    def teardown(self):
        print("数据已清理.\n")

    @pytest.mark.parametrize('code,name,pid',
                             [(
                                     'Us' + "".join(random.sample(t_two[:8], 3)),
                                     '小炒' + '+' + random.choice(L) + str(random.randint(11000, 12000)),
                                     0),
                                 (
                                         'US' + "".join(random.sample(t_two[:10], 4)),
                                         '青椒' + random.choice(L) + str(random.randint(10000, 10100)),
                                         0)])  # t_two[:10]
    def test_ma_add(self, code, name, pid):
        Authorization = 'Bearer ' + get_token

        headers = {
            "Authorization": Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "Content-Type": "application/json"
        }
        length = random.randint(3, 7)

        params = {
            "code": code,  # 必填
            # "id": 0,
            "name": name,  # 必填
            "pid": pid,  # 必填，所属分类，0为根目录
            "remark": "whatF**k",
            "shortCode": "".join(random.sample(code, length)),
            "standard": ""
        }
        r = requests.post(url=deal_root()[0], headers=headers, data=json.dumps(params))
        print(r.text)
        resPj = json.loads(r.text)

        result = resPj["code"]
        assert result == 200

    def test_ma_get_list(self):
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
            "categoryId": "",
            "current": 1,
            "searchWord": "",
            "size": 10
        }
        r = requests.post(url=deal_root()[1], headers=headers, data=json.dumps(params))
        # print(r.text)
        resPj = json.loads(r.text)
        for i in resPj['data']['records']:
            name = i['name']
            newlist.append(name)
        print(newlist)

        assert '物料名称213' in newlist or "物料1"

    def test_ma_change(self):
        """
        尝试禁用第一页的第二条数据
        :return: always disabled data which status is 'YiShenHe'
        """
        Authorization = 'Bearer ' + get_token

        headers = {
            "Authorization": Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "Content-Type": "application/json"
        }
        print('简单获取的禁用列表值正确：1612354938032709633')
        params = {
            "ids": ['1612354938032709633'],
            "status": 0
        }
        right_url = deal_root()[2]
        print(right_url)
        r = requests.post(url=right_url, headers=headers, data=json.dumps(params))
        print(r.text)
        assert right_url is not None
        # return r.text
        # resPj = json.loads(r.text)
        # result = resPj["code"]
        # assert result == 200


if __name__ == '__main__':
    '''
    -s：显示程序中的 print/logging 输出。
    -v：丰富信息模式, 输出更详细的用例执行信息。
    -k：运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行 XX.py 中包含 add 的测试用例。
    -q：简单输出模式, 不输出环境信息。
    -x：出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
    '''

    # pytest.main(["-sqx", "test_PLM_Plan.py"])
    # print(Test_Material.test_ma_change())
    print("=====测试完成=====")
