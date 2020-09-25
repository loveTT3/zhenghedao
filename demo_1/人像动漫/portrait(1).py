# -*- coding: utf-8 -*-
import requests, base64


# 这个函数的操作是为了获取access_token参数
def get_access_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    data = {
        'grant_type': 'client_credentials',  # 固定值
        'client_id': '0i0DBsy9cqgjrGRi4Si96RRp',  # 在开放平台注册后所建应用的API Key
        'client_secret': 'GxMFfqvjCGExBkHxMhG0cGyiYw26rbYh'  # 所建应用的Secret Key
    }
    res = requests.post(url, data=data)
    res = res.json()
    # print(res)
    access_token = res['access_token']
    return access_token


request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/style_trans"
# 二进制方式打开图片文件
f = open('zhao.png', 'rb')
img = base64.b64encode(f.read())
# 注意：这里就是多了type参数和mask_id参数，都是在源文档中可以查看的参数。
# type的值为anime或者anime_mask。前者生成二次元动漫图，后者生成戴口罩的二次元动漫人像。
# 1～8之间的整数，用于指定所使用的口罩的编码。大家可以自行下去尝试。
params = {"image": img, "option": 'lavender'}
access_token = '24.11731cd1f0...9f9b3a930f917f3681b.2592000.1596894747.282335-21221990'
request_url = request_url + "?access_token=" + get_access_token()
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
res = response.json()
# print(res)
if res:
    f = open("kouzhao5.jpg", 'wb')
    after_img = res['image']
    after_img = base64.b64decode(after_img)
    f.write(after_img)
    f.close()
