# -*- coding:utf-8 -*-

__Author__ = "Hardy"

# -*- coding: utf-8 -*-
import json

import requests

req_url = 'http://192.168.3.155:8080/code'
reqPostUrl = 'http://192.168.3.155:8080/auth/login'
choose_url = 'http://192.168.3.155:8080/system/user/chooseTenant'
old_url = 'http://192.168.3.155:8080/auth/old/platform/login'

user = 'huzk'
passwd = '123456'


def check_code():
    r = requests.get(req_url)
    print(r.headers)
    res = json.loads(r.text)
    img = res['img']
    img_id = res['uuid']
    return [img, img_id] if res['captchaEnabled'] else False


def login_auth(pic_result, img_id):
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    data = {'username': user, 'password': passwd, 'code': pic_result, 'uuid': img_id}
    datas = json.dumps(data)
    r = requests.post(reqPostUrl, headers=headers, data=datas)
    res = json.loads(r.text)
    print(res)
    return res['data']['access_token'] if res['code'] == 200 else None


def choose_tenant(token1):
    """
    切换公司，告诉新平台，我现在要用哪个公司身份去登录
    :param token1:使用新平台的token
    :return:
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 Chrome/86.0.4240.198 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "Bearer " + token1
    }
    data = {"tenantId": "1586979014478311425"}  # 深圳前海优管信息技术测试公司 1586979014478311425    好哒：1573493506460860417
    r = requests.post(choose_url, data=json.dumps(data), headers=headers)
    res = json.loads(r.text)
    print(res)
    return True if res['code'] == 200 else False


def switch_auth(token1):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 Chrome/86.0.4240.198 Safari/537.36",
        "Authorization": "Bearer " + token1
    }
    r = requests.post(old_url, headers=headers)
    res = json.loads(r.text)
    print(res)
    return res['data']['token']


if __name__ == '__main__':

    # 拿到登录token，并写入指定文件
    result = 1
    get_img_id = '3bea263c1daa4a149e03902357461ba7'
    get_token = login_auth(result, get_img_id)
    if choose_tenant(get_token):
        print('公司身份登录成功') # tenantId: "1586979014478311425"
    else:
        print('sorry，token出现问题! ')
    another_token = switch_auth(get_token)
    with open('access_token.txt', 'w') as f:
        f.write(get_token)
        print('覆盖写入token完成!')
    with open('old_token.txt', 'w+') as file:
        file.write(another_token)   # 现在又取消了老token的使用
        print(f'{another_token= }\n 已生成')
