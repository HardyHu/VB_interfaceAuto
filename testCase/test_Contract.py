# -*- coding:utf-8 -*-

'''
合同的增删改查，
初期仅实现对新建和删除的用例校验
'''
import pytest
import requests
import json,time,random

global ttodate,randomHTName
t = time.localtime()
t2 = time.strftime("%Y-%m-%d %H:%M:%S", t)[:10]
ttodate = t2 + "T16:00:00.000Z"
intr = random.randint(1000.0,5001)
randomHTName = "Automatic." + str(intr)

@pytest.fixture(params=[[ttodate,ttodate,randomHTName,"你当我是备注吧","备注皆因为我害怕的条款",ttodate],[ttodate,ttodate,randomHTName+"R","你当我是666吧","666皆因为888a条款",ttodate]],name="demo")
def ready(request):
	'''
	需要参数化：companySignDate，customerSignDate，name，
		remark，specialTerms，startDate，
	'''
	yield request.param

class Test_Contract():
	# @pytest.fixture()
	def setup(self):
		# global randomHTName
		# intr = random.randint(1000.0,5001)
		# randomHTName = "Automatic." + str(intr)
		print('测试用例已开始')

	def teardown(self):
		print('测试用例已结束')

	def test_ContractSave(self,demo):
		headers ={
		"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxNTksInVzZXJfa2V5IjoiZjNmZDJiNDYtMjUwNS00YTIxLWIyNTQtMjM2MzRlZTM2NzkxIiwidXNlcm5hbWUiOiJodXprIn0.16DTpPzNr_hz9OCkeVMLXD7XYOmdszS9GvaivYZz_J9Ob97IjfCwtewGMY7qaVClSZFb28Ph0H7tmAP8uWcFew",
		"Cookie":"rememberMe=true; Admin-Expires-In=720; username=admin1; password=gYxS3/mkNjn/DS352bZmHQDB8abWFrg4GbfjIDtuMqRXm30A0ENkMUa9DgEBJDP/TfqCzzyXnYFyxZHgxNUeNQ==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxNTksInVzZXJfa2V5IjoiZjNmZDJiNDYtMjUwNS00YTIxLWIyNTQtMjM2MzRlZTM2NzkxIiwidXNlcm5hbWUiOiJodXprIn0.16DTpPzNr_hz9OCkeVMLXD7XYOmdszS9GvaivYZz_J9Ob97IjfCwtewGMY7qaVClSZFb28Ph0H7tmAP8uWcFew",
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
		"tenantId":"1567682114956627970",
		"Content-Type":"application/json"
		}
		url = "http://192.168.3.156/dev-api/crm/contract/save"
		companySignDate = demo[0]
		customerSignDate = demo[1]
		name = demo[2]
		remark = demo[3]
		specialTerms = demo[4]
		startDate = demo[5]

		data = {
		"EXO":"古惑仔",
		"amount": "12000.00",
		"companySignDate": companySignDate,
		"companySignatory": "他才是签字人",
		"currency": "rmb",
		"customerId": "1570601452197924866",
		"customerSignDate": customerSignDate,
		"customerSignatory": "我不是签字人",
		"endDate": "2034-10-01T16:00:00.000Z",
		"fileList": [{
			"name": "allure报告思路.png",
			"url": "http://192.168.3.156:9000/hh-wb/crm/test/20220924/1664005788312.png",
				}],
		"invoiceList": [{
			"province": "天津市",
			"city": "市辖区",
			"county": "河东区",
			"address": "三十年河东"
					}],
		"name": name,
		"paymentMode": 2,
		"receiveList": [{
			"province": "湖北省",
			"city": "黄冈市",
			"county": "武穴市",
			"address": "老家"
					}],
		"remark": remark,
		"signatoryPosition": "开跑车的职务",
		"specialTerms": specialTerms,
		"startDate": startDate,
		"status": 1,									
		"quoteId": 1573509794071429122
		}
		# print(data)
		data = json.dumps(data)
		r = requests.post(url=url,headers=headers,data=data)
		resp = r.text
		print("==========看下打印情况===========")
		print(resp)
		code = json.loads(resp)["code"]

		assert code == 200		# r

if __name__ == '__main__':
	pytest.main(["-s","-v","test_Contract.py"])		# ,"-x"

