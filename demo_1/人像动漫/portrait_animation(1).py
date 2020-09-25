# -*- coding: utf-8 -*-
import requests, base64


# 这个函数的操作是为了获取access_token参数
def get_access_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    data = {
        'grant_type': 'client_credentials',  # 固定值
        'client_id': 'QEH32YDViRc3bmSTU6d8qOcy',  # 在开放平台注册后所建应用的API Key
        'client_secret': 'hxWlQd3wQe3CGjcdyHAHkLWug2k466Fw'  # 所建应用的Secret Key
    }
    res = requests.post(url, data=data)
    res = res.json()
    # print(res)
    access_token = res['access_token']
    print access_token
    return access_token


# 下面的代码就是API文档中的代码，直接搬过来使用即可。
request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime"
f = open('zhao.png', 'rb')  # 二进制方式打开图片文件
img = base64.b64encode(f.read())  # 图像转为base64的格式，这是百度API文档中要求的

params = {"image": img}
#access_token = '24.11731cd1f0...9f9b3a930f917f3681b.2592000.1596894747.282335-21221990'
request_url = request_url + "?access_token=" + get_access_token()
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
res = response.json()
# 前面我们讲述了这个请求返回的是一个字典，其中一个键就是image，代表的是处理后的图像信息。
# 将这个图像信息写入，得到最终的效果图。
if res:
    f = open("kouzhao1.jpg", 'wb')
    after_img = res['image']
    after_img = base64.b64decode(after_img)
    f.write(after_img)
    f.close()