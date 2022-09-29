# -*- coding:utf-8 -*-

import json
import requests
import pytest

@pytest.fixture(scope="function",params=["10","20"],autouse =False,name="demo")
def get_param(request):
	print("前置=====")
	yield request.param
	print("后置=====")

class TestRTInventory():
	'''
	用来测试ERP--进销存--及时库存第一页的数据状况
	param checksize::指定页的数据量，有每页10条/20条/30条...
	param recordsl::实际去校验，拉取的数据有多少条
	'''
	def setup(self):
		print("初始化OK.")

	def teardown(self):
		print("数据已清理.")

	def test_loaddata(self,demo):
		headers = {
		"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxNTksInVzZXJfa2V5IjoiY2M5MzRhYjMtMTkwNi00MTFjLThjMTEtZmViZGU1ZjRlY2RjIiwidXNlcm5hbWUiOiJodXprIn0.H2psnQjVEH0XVA1V70da4sDVUTkMEFq6l-K77_m3dCqD0EXrDM_8VvZC-MnBIU2zv-6QJOGUICZDxwYopiotYg",
		"Cookie":"rememberMe=true; Admin-Expires-In=720; username=admin1; password=gYxS3/mkNjn/DS352bZmHQDB8abWFrg4GbfjIDtuMqRXm30A0ENkMUa9DgEBJDP/TfqCzzyXnYFyxZHgxNUeNQ==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxNTksInVzZXJfa2V5IjoiY2M5MzRhYjMtMTkwNi00MTFjLThjMTEtZmViZGU1ZjRlY2RjIiwidXNlcm5hbWUiOiJodXprIn0.H2psnQjVEH0XVA1V70da4sDVUTkMEFq6l-K77_m3dCqD0EXrDM_8VvZC-MnBIU2zv-6QJOGUICZDxwYopiotYg",
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
		"tenantId":"1567682114956627970"
		}
		url = "http://192.168.3.156/dev-api/erp/item/stock/list?currentPage=1&currentPageSize=" + demo
		print(url)
		params = {
		'currentPage':"1",
		'currentPageSize':demo
		}
		r = requests.get(url=url,headers=headers,params=params)
		resp = r.text
		print(resp)
		respj = json.loads(resp)
		
		recordsl = len(respj["data"]["records"])
		if recordsl == 10:
			print("检查加载第一页完成，第一页数据有10条！")
		else:
			print(f"recordsl is :{recordsl}")
			print("请检查测试环境是否出现服务异常，或者数据已经被清理!")	
		checksize = respj["data"]["size"]
		print(checksize)
		assert int(checksize) == recordsl

if __name__ == '__main__':
	'''
	-s：显示程序中的 print/logging 输出。
	-v：丰富信息模式, 输出更详细的用例执行信息。
	-k：运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行 XX.py 中包含 add 的测试用例。
	-q：简单输出模式, 不输出环境信息。
	-x：出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
	'''

	pytest.main(["-s","-q","-x","test_LoadRealtimeInventory.py"])
	print("=====测试完成=====")