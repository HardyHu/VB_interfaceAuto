# -*- utf-8 -*-

__Author__ = "HuZk"

import datetime
import json
import os
import time
import zipfile
from _pydecimal import Decimal, Context, ROUND_HALF_UP

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import yagmail

user = 'hzk@veiban.com'
password = '110bg123!'


def execute_bat_file():
    os.system('ExcPy.bat')  # tmp.bat
    # quit()


# 压缩文件
def zipDir(dir_path, zip_here):
    """
    :param dir_path: 为需要导出的文件夹路径
    :param zip_here: 导出路径（含压缩包名称）
    :return:
    """
    tryZip = zipfile.ZipFile(zip_here, "w", zipfile.ZIP_DEFLATED)
    for path, dirNames, filenames in os.walk(dir_path):
        # 去掉目标根路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dir_path, '')
        for filename in filenames:
            tryZip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    tryZip.close()


def rightContent():
    with open(r'.\report\widgets\summary.json', 'r') as f:
        textContent = f.read()
    summary = json.loads(textContent)
    failed = summary['statistic']['failed']
    broken = summary['statistic']['broken']
    skipped = summary['statistic']['skipped']
    passed = summary['statistic']['passed']
    unknown = summary['statistic']['unknown']
    total = summary['statistic']['total']

    time_start = str(summary['time']['start'])[:10] + '.' + str(summary['time']['start'])[10:]
    time_stop = str(summary['time']['stop'])[:10] + '.' + str(summary['time']['start'])[10:]
    duration = summary['time']['duration']

    r_start = datetime.datetime.fromtimestamp(float(time_start))
    r_end = datetime.datetime.fromtimestamp(float(time_stop))

    start = r_start.strftime('%Y-%m-%d %H:%M:%S.%f')  # 精确到毫秒
    stop = r_end.strftime("%Y-%m-%d %H:%M:%S.2%f")
    duration = format(duration, ',')
    # 通过率
    pass_probability = str(Context(prec=4, rounding=ROUND_HALF_UP).create_decimal(Decimal(passed / total * 100))) + '%'

    summaryOut = rf'''
    本次自动化代码总共加入测试用例：{total}个，
    失败用例：{failed}，故障用例：{broken}，通过用例：{passed}，跳过用例：{skipped}，未知用例：{unknown}。
    通过率为：{pass_probability}
    详情请见附件，报告查看请使用allure工具（工具获取与使用，请联系HuZK）,谢谢！
    
    用例开始日期为：{start}
    结束日期为：{stop}
    总计耗时{duration}ms。
    '''
    return summaryOut, stop


# 发送报告
# 连接邮箱服务器,smtp里password输入的是授权码
yag = yagmail.SMTP(user=user, password=password, host='smtp.mxhichina.com')  # smtp.qq.com

# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 第一步与第二步
    execute_bat_file()

    # 第二步，执行脚本，跑完代码，并生成报告(推荐使用os.path.join)
    try:
        os.system('cd E:\\VeiBan Project\\testCase')
        os.system(r'xcopy "E://资料//自动化所需文档//基础配置文件\" "E://VeiBan Project//result" /y')
        time.sleep(2)
        os.system(r'allure generate -c -o .\report .\result')  # 目录位置一定要确认正确

        # 打包最新report内容到桌面。
        zipDir("E:\\VeiBan Project\\report", r"E:\Users\Administrator\Desktop\report.zip")
    finally:
        os.system('exit')
        pass

    # 第三步。。准备邮件正文与附件，发送邮件
    summaryTitle = rightContent()
    salt = summaryTitle[1][:16]
    # 邮箱正文，自定义
    contents = ['\n', summaryTitle[0], '\n<br>VeiBan Project接口测试内容：CRM+PLM</br>\n', '线索：test_ClueInterface',
                '合同：test_Contract',
                '客户：test_customer',
                '开票：test_invoice', '实时库存：test_LoadRealtimeInventory', '订单：test_order', '回款：test_Payment',
                '报价：test_quote', 'PLM相关：', '项目管理：test_PLM_PM', '项目计划：test_PLM_Plan',
                '...', 'ISC构建中，请期待...','\n\n关键配置文件：config.yml']
    print(contents[1])
    # 发送带附件的邮件，最后1个参数为附件地址
    # 接收邮件的邮箱和附件地址可以为列表，即发送给多个邮箱，发送多个附件
    receive_address = ['zhangxueqing@veiban.com', 'lwb@epipe.com.cn', 'zyw@epipe.com.cn',
                       'zdj@epipe.com.cn', 'lgm@epipe.com.cn', 'mxc@epipe.com.cn']  # >谨记：发送的时候再加上领导邮件<

    if summaryTitle:
        yag.send(receive_address, '自动化系统测试报告含ISC_' + salt, contents,
                 [r"E:\Users\Administrator\Desktop\report.zip"])
    print('发送动作已完成！')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
