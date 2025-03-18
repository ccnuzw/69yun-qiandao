import requests

# 登录信息
LOGIN_URL = "https://69yun69.com/auth/login"  # 替换为实际的登录 URL
CHECKIN_URL = "https://69yun69.com/user/checkin"  # 替换为签到 API

# 用户凭据
data = {
    "email": "ccnuzw@gmail.com",
    "password": "zw321561"
}

# 伪装成浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": LOGIN_URL
}

# 创建 Session 维持登录状态
session = requests.Session()

# **1. 登录**
response = session.post(LOGIN_URL, data=data, headers=headers)

if "登录失败" in response.text or response.status_code != 200:
    print("登录失败！请检查用户名或密码")
else:
    print("登录成功！")

    # **2. 进行签到**
    checkin_response = session.post(CHECKIN_URL, headers=headers)
    
    if checkin_response.status_code == 200:
        print("签到成功！")
    else:
        print(f"签到失败: {checkin_response.status_code}, {checkin_response.text}")
