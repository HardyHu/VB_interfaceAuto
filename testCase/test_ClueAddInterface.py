# -*- coding:utf-8 -*-

import json
import requests
import pytest
import random

# @pytest.fixture(params=[{"companyName":"Mynameis","name":"Zhaozilong"},{"companyName":"Urnameis","name":"ZhangFei"}])
# @pytest.fixture()
def setup():	# request
	# data = request.param
	print("测试接口数据已准备")

def teardown():
	print("测试数据已经全部清除")

# http://192.168.3.156/prod-api/auth/login
# 
def get_header():
	headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
	"Cookie":"rememberMe=true; Admin-Expires-In=720; username=admin666; password=DZTgg5Lf/mQ9yd6AI+wGYTlkr+YE1KdNkhLaGzgg8H0ZXxn46eB6bjDLIC8rRWMLSo6KtQKxir6+88U48c1nHw=="
	}
	datas = {"username":"admin666","password":"xxx","code":"10","uuid":"25203b19c15a458a8b1e2e11f022bfee"}		 # ,"code":"1"
	url = "http://192.168.3.156/prod-api/auth/login"
	datas = json.dumps(datas)
	r = requests.post(url=url,headers=headers,data = datas)
	print(r.text)
	# try:
	# 	token = r.json().get("data").get("access_token")
	# 	print(token)
	# # from selenium.common.exceptions import TimeoutException
	# except requests.exceptions.RequestException as e:
	# 	print(e)
	
	print(r.status_code)



def test_ClueSave():
	global CN,N,headers,ids
	headers = {
	"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxNTksInVzZXJfa2V5IjoiMjljODM2MjUtOTU1NC00ZWEyLTk0MmQtMmE2YzAyNGE1NWMxIiwidXNlcm5hbWUiOiJodXprIn0.TtBw4P54vMFt-VEXMS_cI5TQ53VfK47q_EiNMeyJoOAHRhXklAKRYWyf0xxEmySc3QpasvK0pSNi9MbQpWpefA",
	"Cookie":"rememberMe=true; Admin-Expires-In=720; username=admin1; password=gYxS3/mkNjn/DS352bZmHQDB8abWFrg4GbfjIDtuMqRXm30A0ENkMUa9DgEBJDP/TfqCzzyXnYFyxZHgxNUeNQ==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxNTksInVzZXJfa2V5IjoiMjljODM2MjUtOTU1NC00ZWEyLTk0MmQtMmE2YzAyNGE1NWMxIiwidXNlcm5hbWUiOiJodXprIn0.TtBw4P54vMFt-VEXMS_cI5TQ53VfK47q_EiNMeyJoOAHRhXklAKRYWyf0xxEmySc3QpasvK0pSNi9MbQpWpefA",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
	"tenantId":"1567682114956627970",
	"Content-Type":"application/json"
	}
	url = "http://192.168.3.156/dev-api/crm/clue/save"
	intr = random.randint(10000.0,15000)
	# yield intr
	CN = "Autotest." + str(intr) + " Company"
	N = "XAutotest." + str(intr)
	data = {"companyName":CN,"name":N,"status": 1}		# ,"status": 1
	print(data)

	data = json.dumps(data)		# 类型转换
	r = requests.post(url = url,headers=headers,data=data)	# request.param
	# rstatus = r.status_code
	resp = r.text
	# ids = json.loads(resp)["data"]	# 
	ids = r.json().get("data")
	print(f"接口响应值为{resp}")
	
	respCode = json.loads(resp)["code"]
	print(f"接口内的状态码为{respCode}")
	assert respCode == 200
	
def test_ClueDel():
	# print(f"CN is:{CN}")
	url = "http://192.168.3.156/dev-api/crm/clue/delete"
	data = {"ids":[ids]}
	# 1572412561666162689
	r = requests.post(url=url,headers=headers,data=json.dumps(data))
	print(f"接口响应值为{r.text}")
	get_code = json.loads(r.text)["code"]
	print(f"接口内的状态码为{get_code}")
	assert get_code == 200

if __name__ == '__main__':
	# get_header()

	# 注意global在新建函数内，所以要调用test_ClueSave才能够在这里使用全局变量ids
	test_ClueSave()
	print(f"\r线索添加接口测试正常。\n已返回新建线索的id：{ids}.\t状态：待删除！")
	# test_ClueDel()
	# pytest.main()