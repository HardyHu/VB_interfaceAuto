
cd E:\Veiban Project
E:
cd testCase
rem # 提前获取token
rem python tokenEasy.py
python "E:\\Veiban Project\\testCase\\tokenEasy.py"

rmdir ..\result /s/q
mkdir ..\result
pytest -sv --alluredir=..\result
xcopy "E://资料/自动化所需文档/基础配置文件\" "E://Veiban Project//result" /y

xcopy "E://资料//自动化所需文档//基础配置文件\" "E://Veiban Project//result" /y

rem allure generate -c -o ..\report ..\result
exit