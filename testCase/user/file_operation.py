# -*- coding:utf-8 -*-

"""
对文件的操作，使文件易于操作，并能快速读写，每次覆盖写入关键配置
当前支持这三种文件格式：.csv， .yml， .xlsx
"""
import csv

import yaml

# with open('info.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['配置文件1', '记得覆盖写入，第一列为索引'])
#     writer.writerow(['账号', 'huzk'])
#     writer.writerow(['密码', '123456'])
#     writer.writerow(['interface_AD', 'http://192.168.3.155:8080'])


"""
# 将中文转换为Unicode编码
text_unicode = text.encode('unicode-escape').decode()
print(text_unicode)
 
# 将Unicode编码转换为中文
# s = text_unicode.encode('utf-8').decode('unicode_escape')
s = text_unicode.encode().decode('unicode_escape')
"""


def write_csv(data1):
    with open('info.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if len(data1) == 1:
            writer.writerow(data1)
        else:
            for i in range(len(data1)):
                if i % 2 != 1:
                    writer.writerow(data1[i:i + 2])
        # writer.writerows()


def run_choice1():
    print('请输入：举例： ["这是","哦列表"];"mafan";"space:带了冒号";"token1";"token2"')
    new_str = '[这是,哦列表];mafan;space:带了冒号;token1;token2'
    print(new_str.split(';'))
    # data = input('请输入您的内容，以；隔开：')
    write_csv(new_str.split(';'))


# run_choice1()
# print('csv 配置文件写入完成.')

class ymlOperation:
    def path_right(self):
        import os
        file = 'config.yml'
        pwd = 'E:\\Veiban Project\\testCase\\user'
        right = os.path.join(pwd, file)
        return right

    @classmethod
    def write_yaml(cls, data2):
        """
        用来写入到 yml数据的
        :param data2: 数据内容
        :return:
        """
        # data2 = self.data2
        myClass = ymlOperation()
        file_position = cls.path_right(self=myClass)
        with open(file_position, 'w', encoding='utf-8') as yml_file:  # , encoding='utf-8', a是追加
            yml_file.write('\n')
            yaml.dump(data2, yml_file, encoding='utf-8', allow_unicode=True)  # utf-8, unicode

    @classmethod
    def read_yaml(cls):
        myClass = ymlOperation()
        file_position = cls.path_right(self=myClass)
        f = open(file_position, 'r', encoding='utf-8')  # , encoding='utf-8'
        yml_config = yaml.load(f, Loader=yaml.FullLoader)
        """
        Loader的几种加载方式
        BaseLoader - -仅加载最基本的YAML
        SafeLoader - -安全地加载YAML语言的子集。建议用于加载不受信任的输入。
        FullLoader - -加载完整的YAML语言。避免任意代码执行。这是当前（PyYAML5.1）默认加载器调用yaml.load(input)（发出警告后）。
        UnsafeLoader - -（也称为Loader向后兼容性）原始的Loader代码，可以通过不受信任的数据输入轻松利用。
        """
        f.close()
        return yml_config

    @staticmethod
    def update_yaml(self, file, key, value):
        # myClass = ymlOperation()
        file_position = ymlOperation.path_right(self)
        if not file:
            file = file_position
        old_data = ymlOperation.read_yaml()  # 读取文件数据
        old_data[key] = value  # 修改为取值的
        with open(file, 'w', encoding='utf-8') as f:
            yaml.dump(old_data, f, encoding='utf-8', allow_unicode=True)


data = {"title": "Write and maintain by __Author__: HuZk",
        "new_plate": {"access_token": "abcd_test"},
        "old_platform": {"token": "old_token_eyJ0eXA", "company": "just seems tenantId"}}
# ymlOperation.write_yaml(data)
# print('yml文件写入完成！')

# 更新yml文件内特定内容
# d = {}
# test_token = 'Bearer testX'
# d['access_token'] = test_token
# title = 'title has his haha.'
# ymlOperation.update_yaml(ymlOperation, '', 'title', title)

# 需要将类实例化, 读取文件, 然后直接使用json操作，拿到值
# B = ymlOperation()
# access_token = B.read_yaml()['new_plate']['access_token']
# access_token = ymlOperation.read_yaml()
# print(access_token)
