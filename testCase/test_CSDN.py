# -*- coding:utf-8 -*-

import logging
# import pytest
import random
import time

import requests
from bs4 import BeautifulSoup

url = "https://blog.csdn.net/qq_17195161"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
}
article_url_final = 'https://blog.csdn.net/qq_17195161/article/details/130194374'  # OS重装python
article_url = 'https://blog.csdn.net/qq_17195161/article/details/128528883'  # scrcpy（中）
reprinted_url = 'https://blog.csdn.net/qq_17195161/article/details/129854308'  # 避坑
article_url_backup = 'https://blog.csdn.net/qq_17195161/article/details/129703700'  # chatGPT漏洞
log = logging.getLogger(__name__)


def title_output():
    res_1 = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(res_1.text, 'lxml')
    return bs.text    # .title


def request_article(add_url):
    for i in range(8081):
        s = requests.session()
        # 设置连接活跃状态为False
        s.keep_alive = False
        sleepTime = random.randint(2, 4)
        print(f'此次休眠预备时长：{sleepTime}')
        response = requests.get(add_url, headers=headers, timeout=100)
        time.sleep(sleepTime)
        response.close()
        if response.status_code == 200:
            if i % 10 == 0:
                """顺便每10次访问下最新转载的文章"""
                time.sleep(2)
                another_visit = requests.get(reprinted_url, headers=headers, timeout=10)
                print(f'{another_visit.status_code = }')
                another_visit.close()

            print(response.text[-36:], end=' ')
            print(f'第{i + 1}次访问成功！\n')

    return


def test_queue_title():
    log.info("print title name...")
    print('\n确认网络状态中：无报错则网络正常，有报错则需校验相应参数和网络！')
    assert "开河大大" in title_output()


if __name__ == "__main__":
    # pytest.main(['-svx','test_CSDN.py'])

    # print(title_output())
    request_article(article_url_final)
    
    request_article(article_url_backup)
