import time
from selenium.webdriver.common.by import By
def login_page(username,password,driver):
    element = driver.find_element(By.ID, 'username')
    element.send_keys(username)
    element = driver.find_element(By.ID, 'password')
    element.send_keys(password)
    element = driver.find_element(By.ID, 'btnSubmit').click()
def open_url(url,driver):     #打开网页
    driver.get(url)
    driver.maximize_window()

def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login_page(username,password,driver)
    element = driver.find_element(By.XPATH, "//span[text()='零售出库']").click()
    P_id = driver.find_element(By.XPATH,"//div[text()='零售出库']/..").get_attribute("id")  #通过找到元素获取id属性
    F_id = P_id+"-frame"
    driver.switch_to.frame(1)
    driver.find_element(By.ID,'searchNumber').send_keys(s_key)
    driver.find_element(By.ID,'searchBtn').click()
    time.sleep(2)
    num = driver.find_element(By.XPATH,'//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
    # print(num)
    return num