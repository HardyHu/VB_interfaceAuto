# 这是一个示例 Python 脚本。

__Author__ = "胡智凯"
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import pytest


# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

# 实现滚动弹幕
def rollWord():
    adb = input("请输入一段广告宣传语：")

    # 滚动方向
    while 1:
        RorL = input("请输入是向左滚动（L）还是向右滚动（R）：").upper()
        if RorL in ["L","R"]:
            break
        print("Sorry,你输入有误，将继续输入。")

    # 滚动速度
    speed = float(input("请输入滚动速度(0.1~100)："))

    # 实现滚动效果
    print("滚动过程中可以随时按CTRL+C结束滚动.")
    advWord = adb
    if RorL == "L":
        advWord = adb[-1] + adb[:-1]
        while 1:
            advWord = advWord[1:] + advWord[0]
            print(advWord)
            time.sleep(1 / speed)
            os.system("cls")
    if RorL == "R":
        advWord = adb[1:] + adb[0]     # 准备滚动前的数据
        # 开始滚动的数据
        while 1:
            advWord = advWord[-1] + advWord[:-1]
            print(advWord)
            time.sleep(1/speed)
            os.system("cls")



# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    import time,os
    # rollWord()
    pytest.main()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
