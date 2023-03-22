# import selenium    #工具所有内容导入
from selenium import webdriver   #从selenium工具导入webdriver库
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()   #初始化 建立会话
driver.implicitly_wait(10)
#1.打开网址
# driver.get("http://erp.lemfix.com")
#2.窗口最大化
driver.maximize_window()
# 3.打开新页面
driver.get("http://erp.lemfix.com")
# 4.向前 后退 刷新
# time.sleep(1)
# driver.back()  #后退
# time.sleep(1)
# driver.forward()   #向前
# time.sleep(1)
# driver.refresh()  #刷新
# 5.退出
# time.sleep()
# driver.quit()  #关闭驱动
# driver.close()  #关闭当前窗口
element = driver.find_element(By.ID,'username')
element.send_keys('test123')
# # <input type="text" id="username" name="username" class="form-control required" data-msg-required="请填写登录账号." placeholder="登录账号">
# # time.sleep()
element = driver.find_element(By.ID,'password')
element.send_keys('123456')
# # time.sleep()
# #<button type="submit" class="btn btn-primary btn-block btn-flat" id="btnSubmit" data-loading="登录验证成功，正在进入..." data-login-valid="正在验证登录，请稍候...">立即登录
element = driver.find_element(By.ID,'btnSubmit').click()
# time.sleep(2)
# element = driver.find_element(By.XPATH,"//input[@id='username']")
# element.send_keys('test123')
# # time.sleep(2)
page_text = driver.find_element(By.XPATH,'//div[@class="login-logo"]//b').text
if page_text =="柠檬ERP":
    print("标题是：{}".format(page_text))
else:
    print("不通过")
# time.sleep(2)
login_user = driver.find_element(By.XPATH,"//p[text()='测试用户']").text
if login_user == "测试用户":
    print("用户是：{}".format(login_user))
else:
    print("不通过")
element = driver.find_element(By.XPATH,"//span[text()='零售出库']").click()
P_id = driver.find_element(By.XPATH,"//div[text()='零售出库']/..").get_attribute("id")  #通过找到元素获取id属性
F_id = P_id+"-frame"
# 1. 通过id进行frame切换
# driver.switch_to.frame(F_id)
# driver.find_element(By.ID,'searchNumber').send_keys("314")

# 2.通过元素定位（xpath）切换frame
# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='{}']".format(F_id)))
# driver.find_element(By.ID,'searchNumber').send_keys("314")

# 3.iframe下标 从0开始 html页面=0，第一个宝宝-1，第二个宝宝-2
driver.switch_to.frame(1)
driver.find_element(By.ID,'searchNumber').send_keys("246")
driver.find_element(By.ID,'searchBtn').click()
time.sleep(2)
num = driver.find_element(By.XPATH,'//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
# print(num)
if "246" in num:
    print("正确")
else:
    print("错误")
time.sleep(2)