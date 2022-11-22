# -*- coding:utf-8 -*-

__author__ = 'Hardy'

import json

import requests

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
        companyTel = '188000026' + str(i)
        idCard = '4211821999101016' + str(i)
        data = {"staffName": staffName,
                "companyTel": companyTel,
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

str1 = 'abcee'
str2 = 'ceabe'
str3 = 'newbi'


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


print(check_num_calcu(19))


def check_repeat(str):
    print(set(str))
    if len(str) == 0:
        return False
    if len(set(str)) == len(str):
        return True
    return False


# print(check_repeat(str1))
#
# print(check_repeat(str3))

def check_another(str1, str2):
    print(sorted(str1))
    if sorted(str1) == sorted(str2):
        return '两个字符其中一个是另一个的排列'
    else:
        return False


# print(check_another(str1, str2))

def rechange_str(str):
    if isinstance(str, list):
        return str[::-1]
    else:
        print(list(str), False)
        return list(str)[::-1]


print(rechange_str(str2))
