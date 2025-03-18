from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Chrome 选项（无头模式）
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 启动 WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # 打开登录页面
    driver.get("https://69yun69.com/auth/login")

    # 填写用户名和密码
    username = driver.find_element(By.NAME, "email")  # 根据网站的实际 HTML 结构调整
    password = driver.find_element(By.NAME, "password")

    username.send_keys("ccnuzw@gmail.com")
    password.send_keys("zw321561")
    password.send_keys(Keys.RETURN)

    time.sleep(10)  # 等待登录完成

    # 进入签到页面
    driver.get("https://69yun69.com/user")

    # 查找并点击签到按钮
    sign_in_button = driver.find_element(By.XPATH, "//button[contains(text(), '每日签到')]")
    sign_in_button.click()

    time.sleep(5)  # 等待签到完成

    print("签到成功！")

except Exception as e:
    print(f"签到失败: {e}")

finally:
    driver.quit()
