# -*- coding:utf-8 -*-

import time
import pytest
import json
import requests
import random
from bs4 import BeautifulSoup 


url = "https://blog.csdn.net/qq_17195161"
# wd.get(url)    # 打印标题：开河大大的博客_CSDN博客-自动化,Python开发工具,Python爬虫领域博主
headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
article_url = 'https://blog.csdn.net/qq_17195161/article/details/126322450'
article_url_backup = 'https://blog.csdn.net/qq_17195161/article/details/127420365'


def title_output():
	res_1 = requests.get(url=url,headers=headers)
	# print(res_1.text)
	bs = BeautifulSoup(res_1.text,'lxml')

	# print(res_1.status_code)
	return bs.title.text

def request_imparticle():
	for i in range(3):
		s = requests.session()
		# 设置连接活跃状态为False
		s.keep_alive = False
		sleeptime = random.randint(2,6)
		print(f'此次休眠预备时长：{sleeptime}')
		response = requests.get(article_url_backup, headers=headers, timeout=100)
		if response.status_code == 200:
			print(response.text[-36:],end=' ')
			print(f'第{i+1}次访问成功！\n')
		time.sleep(sleeptime)
		response.close()
	return

def test_Quenendtitle():
	print('确认网络状态中：无报错则网络正常，有报错则需校验相应参数和网络！')
	assert  "开河大大的博客_CSDN博客-自动化," in title_output()

if __name__ == "__main__":
	pytest.main(['-svx','test_CSDN.py'])

    # request_imparticle()

    # print(test_Quenendtitle())
