# -*- utf-8 -*-

__Author__ = "Huzk"

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import pytest
import time
import os
import zipfile
import yagmail

# from testCase.test_invoice import *
user = 'king917619381@vip.qq.com'
password = 'kbgopsvwjhunbaih'  # QQMail授权码

def execute_bat_file():
    os.system('ExcPy.bat')       # tmp.bat
    # quit()

# 压缩文件
def zipDir(dirpath, ziphere):
    # dirpath为需要导出的文件夹路径
    # ziphere（含压缩包名称）
    tryzip = zipfile.ZipFile(ziphere, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标根路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')
        for filename in filenames:
            tryzip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    tryzip.close()


# 发送报告
# 连接邮箱服务器,smtp里password输入的是授权码
yag = yagmail.SMTP(user=user, password=password, host='smtp.qq.com')


# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

# 实现滚动弹幕,加油打气用的
def rollWord():
    adb = input("请输入一段广告宣传语：")

    # 滚动方向
    while 1:
        RorL = input("请输入是向左滚动（L）还是向右滚动（R）：").upper()
        if RorL in ["L", "R"]:
            break
        print("Sorry,你输入有误，将继续输入。")
    # 滚动速度
    speed = float(input("请输入滚动速度(0.1~100)："))
    # 实现滚动效果
    print("滚动过程中可以随时按CTRL+C结束滚动.")
    # advWord = adb
    if RorL == "L":
        advWord = adb[-1] + adb[:-1]
        while 1:
            advWord = advWord[1:] + advWord[0]
            print(advWord)
            time.sleep(1 / speed)
            os.system("cls")
    if RorL == "R":
        advWord = adb[1:] + adb[0]  # 准备滚动前的数据
        # 开始滚动的数据
        while 1:
            advWord = advWord[-1] + advWord[:-1]
            print(advWord)
            time.sleep(1 / speed)
            os.system("cls")


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # execute_bat_file()
    #
    # 目标：自动执行.bat脚本，并打包结果，最终发送邮件
    # os.system("D:\\xxx1\\xxx2XMLnew\\otr.bat ")   # 执行脚本，跑完代码，并生成报告(推荐使用os.path.join)
    zipDir("E:\\Veiban Project\\report", r"E:\Users\Administrator\Desktop\report.zip")
    # 邮箱正文，自定义
    contents = ['\n<br>InterfacePythonTest测试内容：</br>\n', '线索：test_ClueInterface', '合同：test_Contract',
                '客户：test_customer',
                '开票：test_invoice', '实时库存：test_LoadRealtimeInventory', '订单：test_order', '回款：test_Payment',
                '报价：test_quote', '...', '\n\n作者：huzk']
    import uuid

    salt = str(uuid.uuid4())
    # 发送带附件的邮件，最后1个参数为附件地址
    # 接收邮件的邮箱和附件地址可以为列表，即发送给多个邮箱，发送多个附件
    recieve_address = ['1151132197@qq.com','mxc@epipe.com.cn']
    yag.send(recieve_address, 'CRM系统自动化报告' + salt, contents, [r"E:\Users\Administrator\Desktop\report.zip"])
    print('发送动作已完成！')


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
