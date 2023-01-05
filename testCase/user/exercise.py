# -*- coding:utf-8 -*-

__author__ = 'Hardy'

import json
import random
import time

import requests

# Exercise 6

""" 该球从n米的高空落下后，第m次落地 """


def calculate_this(m=None):
    n = int(input('请输入高度: '))  # 落地时的高度
    if m is None:
        m = 0  # 落地次数
    Cristiano_Ronaldo = float(input('反弹力度: '))  # 反弹力度，默认是1/4
    if not Cristiano_Ronaldo:
        Cristiano_Ronaldo = 0.25
    my_sum = n
    while (n * Cristiano_Ronaldo) >= 0.00001:
        my_sum += n * Cristiano_Ronaldo * 2
        m += 1
        print(m)
        n = Cristiano_Ronaldo * n
    return '总运行距离%.2f' % my_sum, '运行次数%s' % (m + 1)


# print(calculate_this())

# n = int(input())
# m = int(input())
# test_num = n
# while m != 1:
#     test_num += n * 0.25 * 2
#     m = m - 1
#     n = 0.25 * n
# print('%.2f' % test_num)
# print('%.6f' % (n * 0.25))  # +0.0001 即最后一次弹起距离


# Exercise 5
# ls1 = [1, 2, 3, 4, 5, 6]
# ls2 = [11, 22, 33, 44, 55, 66, 88]
# for l1, l2 in zip(ls1, ls2):
#     print(l1, l2)


# Exercise 4
def check_num_calcu(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    if num % 3 != 0 and num % 5 != 0:
        return str(num)
    if num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'


# 针对公司未作限制的短信发送接口（http://192.168.3.156/register）
register_url = 'http://192.168.3.155:8080/smsCode?phone='


def run_spend_money():
    headers = {'isToken': 'false',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/103.0.0.0 Safari/537.36 '
               }
    phone_list = ['17349708757']
    # , '15271180204', '15800011245', '15800011246', '15800011247',

    statistic = 0
    # for i in range(20):
    #     list1 = '188000' + ''.join(str(n) for n in random.sample(range(10), 5))
    #     list2 = '158000' + ''.join(str(n) for n in random.sample(range(10), 5))
    #     list3 = '158186' + ''.join(str(n) for n in random.sample(range(10), 5))
    #     this = [list1, list2, list3]
    #     phone_list.append(random.choice(this))
    #     # print(phone_list, this)
    #     sms_url = register_url + random.choice(phone_list)
    #     print(sms_url)
    #     res = requests.get(sms_url, headers=headers)
    #     print(res.text)
    #     if list1 in phone_list:
    #         phone_list.remove(list1)
    #     if list2 in phone_list:
    #         phone_list.remove(list2)
    #     if list3 in phone_list:
    #         phone_list.remove(list3)
    #     time.sleep(1)
    #     if json.loads(res.text)['code'] == 200:
    #         statistic += 1

    # #### 打击沙女士给客官你那个岗位了 ####
    for i in range(20):
        list2 = '158000' + ''.join(str(n) for n in random.sample(range(10), 5))
        list3 = '158186' + ''.join(str(n) for n in random.sample(range(10), 5))
        phone_list.append(list2)
        phone_list.append(list3)
        # print(phone_list, this)
        sms_url = register_url + random.choice(phone_list)
        print(sms_url)
        res = requests.get(sms_url, headers=headers)
        print(res.text)
        if '15818630490' in phone_list:
            phone_list.remove('15818630490')
        if list2 in phone_list:
            phone_list.remove(list2)
        if list3 in phone_list:
            phone_list.remove(list3)
        time.sleep(60)
        if json.loads(res.text)['code'] == 200:
            statistic += 1
    print(f'Final list is{phone_list}')
    print(f'此次成功发送短信个数：{statistic}个.')


run_spend_money()


# 166平台接口批量导入
url = 'http://192.168.3.166:8086/staff/update'
url_add = 'http://192.168.3.166:8086/staff/add'
headers = {
    'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbktleSI6IlgtMjE4ZDEwNWY0ZjY4NDAxZWIxOTI2YjZmM2RjZTA2'
                     'NWMtNTQ2ZTQ2YWM5ZGFlNDI2MTliYWU2ZTE1MTk2OTYyYmMiLCJleHBpcmVUaW1lc3RhbXAiOiIxNzAwMjExNzI0MzE3Iiwic'
                     'GhvbmUiOiIxNTAxMzczNDIwOCIsInJlZnJlc2hUaW1lc3RhbXAiOiIxNjg0NDQzNzI0MzE3IiwiZXhwIjoxNzAwMjExNzI0LC'
                     'J1c2VySWQiOiIyMThkMTA1ZjRmNjg0MDFlYjE5MjZiNmYzZGNlMDY1YyIsImFjY2Vzc1RpbWVzdGFtcCI6IjE2Njg2NzU3MjQ'
                     'zMTcifQ.wuzQgYAS7nJwNrqi7jKiXinkGmprG8bX8sewKmTkVd0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36 ',
    'Content-Type': 'application/json;charset=UTF-8'
}
staffId = 'b55c5b5edeac4b23bd0c29dc2781a27b'
staffName = '张三23'
companyTel = '18800002003'
idCard = '421182199910101223'


# 166 - Admin端的信息更新
def staff_update():
    data = {"staffId": staffId,  # need change.
            "staffName": staffName, "companyTel": companyTel,  # need change.
            "companyId": "cfe05dd2cedf4dd1ad9475d32838eaf9",
            "officeIds": ["cfe05dd2cedf4dd1ad9475d32838eaf9"],
            "idCard": idCard,  # need change.
            "postIds": ["b34f1e936ae8dbef28f772026b91085a"],
            "directLeaderStaffId": "",
            "workPlace": "", "hireDate": "",
            "staffType": 0,
            "jobStatus": 0,  # 1是离职
            "hideType": 0,
            "hideRelationList": []}
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print(r.text)


# 166环境添加员工
def staff_add():
    for i in range(62, 70):
        staffName = '张三' + str(i)
        companyPhone = '188000026' + str(i)
        idCard = '4211821999101016' + str(i)
        data = {"staffName": staffName,
                "companyTel": companyPhone,
                "companyId": "cfe05dd2cedf4dd1ad9475d32838eaf9",
                "officeIds": ["03df386de8c54c669bb9d9dd81744227"],
                "idCard": idCard,
                "companyEmail": "",
                "roleId": "", "no": "",
                "postIds": ["b34f1e936ae8dbef28f772026b91085a"],
                "directLeaderStaffId": "",
                "companyPhone": "", "workPlace": "", "hireDate": "", "staffType": 0, "jobStatus": 0, "remark": "",
                "hideType": 0, "hideRelationList": []}
        res = requests.post(url_add, headers=headers, data=json.dumps(data))
        print(f'{staffName}添加成功，返回{res.text}')
    print('All staff add compeleted or Just end!')
# staff_add()
