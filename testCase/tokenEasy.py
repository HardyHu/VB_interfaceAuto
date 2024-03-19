# -*- coding:utf-8 -*-

__Author__ = "Hardy"

# -*- coding: utf-8 -*-
import json

import requests

req_url = 'http://192.168.3.155:8080/code'
reqPostUrl = 'http://192.168.3.155:8080/auth/login'
choose_url = 'http://192.168.3.155:8080/system/user/chooseTenant'
old_url = 'http://192.168.3.155:8080/auth/old/platform/login'

# 读取197环境验证码和用户访问端口
Env197_ReqUrl = 'http://192.168.3.197:8080/code'
Env197_ReqPUrl = 'http://192.168.3.197:8080/auth/login'
Env197_ChooseUrl = 'http://192.168.3.197:8080/system/user/chooseTenant'
ENv197_representation = 'http://192.168.3.197:8080/auth/old/platform/login'

user = 'huzk'
passwd = '123456'

# ENV197_user = 'test'
# ENV197_passwd = '123456'
ENV197_user = '15013734208'
ENV197_passwd = 'maxc2023'


def check_code(url1=req_url):
    r = requests.get(url1)
    print(r.headers)
    res = json.loads(r.text)
    # img = res['img']  # 暂时注释，无需传出
    img_id = res['uuid']
    return img_id if res['captchaEnabled'] else False


def login_auth(pic_result, img_id, url22=reqPostUrl, user=user, passwd=passwd):
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    data = {'username': user, 'password': passwd, 'code': pic_result, 'uuid': img_id}
    datas = json.dumps(data)
    r = requests.post(url22, headers=headers, data=datas)
    res = json.loads(r.text)
    print(res)
    return res['data']['access_token'] if res['code'] == 200 else None


def choose_tenant(token1, url2=choose_url, tenantId='1586979014478311425'):
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
    data = {"tenantId": tenantId}  # 深圳前海优管信息技术测试公司 1586979014478311425
    r = requests.post(url2, data=json.dumps(data), headers=headers)
    res = json.loads(r.text)
    print(res)
    return True if res['code'] == 200 else False


def switch_auth(token1, url3=old_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 Chrome/86.0.4240.198 Safari/537.36",
        "Authorization": "Bearer " + token1
    }
    r = requests.post(url3, headers=headers)
    res = json.loads(r.text)
    print(res)
    return res['data']['token']


if __name__ == '__main__':
    from user.file_operation import ymlOperation

    # 拿到登录token，并写入指定文件 <<- 注释完记得解注释 ->>
    get_img_id = '1e2de5f60f9a47db8f8d0be0ff9e6293'  # 万能验证码88
    easy = check_code()
    if easy:
        # global result, get_img_id
        result = 88
        get_img_id = easy

    # noinspection PyUnboundLocalVariable
    get_token = login_auth(result, get_img_id)
    if choose_tenant(get_token):
        print('公司身份登录成功')  # tenantId: "1586979014478311425"
    else:
        print('sorry，old token出现问题! ')
    another_token = switch_auth(get_token)
    with open('access_token.txt', 'w') as f:
        f.write(get_token)
        print('覆盖写入token完成!')
    # with open('old_token.txt', 'w+') as file: # 暂时不用写入老token
    #     file.write(another_token)  # 现在又取消了老token的使用
    #     print(f'{another_token= }\n 已生成')

    # 尝试更新token
    d = {'access_token': get_token}
    op_path = 'E:\\Veiban Project\\testCase\\user\\config.yml'
    ymlOperation.update_yaml(ymlOperation, op_path, 'new_plate', d)

    # 197环境更新token和ApiHost
    allKey = 88
    pic197_id = check_code(Env197_ReqUrl)
    print(f'  197环境的狗屁图片验证码id是 {pic197_id}')
    try197_token = login_auth(allKey, pic197_id, Env197_ReqPUrl, ENV197_user, ENV197_passwd)

    try:
        choose_tenant(try197_token, Env197_ChooseUrl, '1586979014478311425')  # 华瀚集团（测试）公司1572050341476212737
    finally:
        # 同时绑定老平台token
        my197_representation = switch_auth(try197_token, ENv197_representation)
        # 写入新平台token，老平台老规矩暂不处理
        d = {'197_token': try197_token, 'Interface_Api_Host': 'http://192.168.3.197:8080/plm/'}
        op_path = 'E:\\Veiban Project\\testCase\\user\\config.yml'
        ymlOperation.update_yaml(ymlOperation, op_path, '197_Env_Test', d)

    # 校验一下
    my_read = ymlOperation.read_yaml()
    print(my_read)
