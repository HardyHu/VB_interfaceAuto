# -*- coding:utf-8 -*-

__Author__ = "Hardy"

# -*- coding: utf-8 -*-
import json
import requests

req_url = 'http://192.168.3.155:8080/code'
reqPostUrl = 'http://192.168.3.155:8080/auth/login'

user = 'huzk'
passwd = '110bg123'


def checkcode():
    r = requests.get(req_url)
    print(r.headers)
    res = json.loads(r.text)
    img = res['img']
    imgid = res['uuid']
    return [img, imgid] if res['captchaEnabled'] else False


def login_auth(picResult, imgid):
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    data = {}
    data['username'] = user
    data['password'] = passwd
    data['code'] = picResult
    data['uuid'] = imgid
    datas = json.dumps(data)
    r = requests.post(reqPostUrl, headers=headers, data=datas)
    res = json.loads(r.text)
    print(res)
    return res['data']['access_token'] if res['code'] == 200 else False


if __name__ == '__main__':
    # # 获取验证码的图片base64码破解后的值，及图片对应uuid
    # imgl = checkcode()
    # if imgl:
    #     xxx = True

    # 拿到登录token，并写入指定文件
    result = 3
    imgid = '87c7aff8541744f7832f0e01e32adeef'
    get_token = login_auth(result, imgid)
    with open('access_token.txt', 'w') as f:
        f.write(get_token)
        print('覆盖写入token完成!')