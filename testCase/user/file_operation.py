# -*- coding:utf-8 -*-

"""
对文件的操作，使文件易于操作，并能快速读写，每次覆盖写入关键配置
当前支持这三种文件格式：.csv， .yml， .xlsx
"""
import csv
import openpyxl
import yaml

# with open('info.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['配置文件1', '记得覆盖写入，第一列为索引'])
#     writer.writerow(['账号', 'huzk'])
#     writer.writerow(['密码', '123456'])
#     writer.writerow(['interface_AD', 'http://192.168.3.155:8080'])

def write_csv(data1):
    with open('info.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if len(data1) == 1:
            writer.writerow(data1)
        else:
            for i in range(len(data1)):
                if i%2 != 1:
                    writer.writerow(data1[i:i+2])
        # writer.writerows()


def run_choice1():
    print('请输入：举例： ["这是","哦列表"];"mafan";"space:带了冒号";"token1";"token2"')
    new_str = '[这是,哦列表];mafan;space:带了冒号;token1;token2'
    print(new_str.split(';'))
    # data = input('请输入您的内容，以；隔开：')
    write_csv(new_str.split(';'))


# run_choice1()
# print('csv 配置文件写入完成.')

def write_yaml(data2):
    """
    用来写入到 yml数据的
    :param data2: 数据内容
    :return:
    """
    with open('config.yml', 'a', encoding='utf-8') as yml_file:
        yml_file.write('\n')
        yaml.dump(data2, yml_file, encoding='utf-8', allow_unicode=True)


def read_yaml():
    f = open('config.yml', 'r', encoding='utf-8')
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

def update_yaml(file):
    old_data = read_yaml() # 读取文件数据
    old_data['title'] = '您的大哥现在是胡智凯' # 修改读取的数据
    with open(file, 'w', encoding='utf-8') as f:
        yaml.dump(old_data, f, encoding='utf-8', allow_unicode=True)


data = {"title": "最伟大的糊弄", "S_data": {"原谅": "几个管理"}, "S_data2": {"name": "见怪不怪", "company": "优质云"}}
write_yaml(data)
update_yaml('config.yml')
print('yml文件写入完成！')



