from ceshi import test05          #导入函数文件
from test_data import test_date   #  导入测试数据
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 调用函数  1.取出参数  2.传参到函数调用里
url = test_date.url["url"]  #取值url
user = test_date.login_date["username"]   #取值登录用户名
pwd = test_date.login_date["password"]    #取值登录密码
s_key = test_date.s_key["s_key"]       #取值搜索的关键字
print(url,user,pwd,s_key)
# 给函数定一个返回值，调用的时候用一个变量接受
result = test05.search_key(driver=driver,url=url,username=user,password=pwd,s_key=s_key)  #调用函数
if s_key in result:
    print("正确")
else:
    print("错误")