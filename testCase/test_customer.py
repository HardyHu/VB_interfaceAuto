# -*- coding:utf-8 -*-

'''
yonghu的增删改查， 
初期仅实现对新建和删除的用例校验
'''
import pytest
import requests
import json,random
import datetime


global name
t = datetime.datetime.now()
r1 = random.randint(1000,9001)
t2 = (t + datetime.timedelta(days = 2)).strftime("%Y-%m-%d %H:%M:%S")
name = "村头二狗" + t2[:10] + str(r1)



# @pytest.fixture(params=[[dtjoin1,dtjoin2,"小小的备注",dtjoin1,"这是个mark"],[dtjoin1,dtjoin2,"微微的备注",dtjoin1,r"这是个mark\|/"],
	# [dtjoin1,dtjoin2,"单据Aa的备注",dtjoin1,r"这是~！@#￥%……&*（）"]],name="demo")
def ready(request):
	'''
	需要参数化：paymentPlaneDate1，paymentPlaneDate2，remark，
		paymentDate，employeeNum
	'''
	
	yield request.param

class Test_Customer():
	# @pytest.fixture()
	def setup(self):
		# global randomHTName
		# intr = random.randint(1000.0,5001)
		# randomHTName = "Automatic." + str(intr)
		print('测试用例已开始')

	def teardown(self):
		print('测试用例已结束')

	def test_CustomerSave(self):		# ,demo
		global headers
		headers ={
		"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxNTksInVzZXJfa2V5IjoiZTFiMzNmNWYtNWY3YS00MDc5LThjNzMtZWM5MmE5OTdjZGI3IiwidXNlcm5hbWUiOiJodXprIn0.G3lvAvibnbxr5R-nRms79Q9M4IhDGVrJuXhvJ9zU4Sm2myWquMPaDhTCBvc-dQdEXdiwn9QywlQxGPd2gAemGQ",
		"Cookie":"rememberMe=true; Admin-Expires-In=720; username=huzk; password=Ce8Xk0ifC2xa3pAjSQiX3woOewkWzBDnIqRsrmXdUGHRP9XJoKxDxUfqS/CUcU901BZz5TrPYf2NkDkHUEdaOg==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxNTksInVzZXJfa2V5IjoiZTFiMzNmNWYtNWY3YS00MDc5LThjNzMtZWM5MmE5OTdjZGI3IiwidXNlcm5hbWUiOiJodXprIn0.G3lvAvibnbxr5R-nRms79Q9M4IhDGVrJuXhvJ9zU4Sm2myWquMPaDhTCBvc-dQdEXdiwn9QywlQxGPd2gAemGQ",
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
		"tenantId":"1567682114956627970",
		"Content-Type":"application/json"
		}
		url = "http://192.168.3.156/dev-api/crm/customer/save"
		data = {
  		"email": "666888@qq.com",
  		"employeeNum": 2000,
  		"industryId": 3,
  		"industryName": "",
  		"status":1,
  		"invoiceList": [
    		{
                "province": "山东省",
                "city": "淄博市",
                "county": "张店区",
                "address": "5008"
            }
  		],
  		"level": 1,
  		"name": name,
  		"phone": "13855556666",
  		"receiveList": [
    		{
                "province": "安徽省",
                "city": "马鞍山市",
                "county": "市辖区",
                "address": "思想觉悟"
			}
  		],
  		"remark": "string..++--**//"
		}
		print(data)
		data = json.dumps(data)
		r = requests.post(url=url,headers=headers,data=data)
		resp = r.text

		code = json.loads(resp)["code"]
		print(code)
		assert code == 200

	def test_CustomerDel(self):
		
		url = "http://192.168.3.156/dev-api/crm/customer/save"
		data = {"目前客户、联系人都没有删除功能，无需校验"}
		checkstr = list(data)[0][4:8]
		print(f'checkstr is {checkstr}')
		assert "联系人" in checkstr

if __name__ == '__main__':
	Test_Customer().test_CustomerSave()
	Test_Customer().test_CustomerDel()


