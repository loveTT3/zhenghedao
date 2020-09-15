from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
import pymysql
# Create your views here.

# 链接zh_bms_cms库
def shujuku_app():
    conn = pymysql.connect(
    host='192.168.2.96',  #主机地址，若是自己的主机也可以用'localhost'
    port=3306,  #端口
    user='root',  #用户
    password='akQq5csSXI5Fsmbx5U4c',  #密码
    database='zh_bms_cms',  #数据库
    charset='utf8',  # 设置编码，此处不能写utf-8
    # autocommit=True  # 自动提交
    )
    return conn

# 链接db_weizhan库
def shujuku_h5():
    conn = pymysql.connect(
    host='192.168.2.96',  #主机地址，若是自己的主机也可以用'localhost'
    port=3306,  #端口
    user='root',  #用户
    password='akQq5csSXI5Fsmbx5U4c',  #密码
    database='db_weizhan',  #数据库
    charset='utf8',  # 设置编码，此处不能写utf-8
    # autocommit=True  # 自动提交
    )
    return conn

# 装饰器
def wrapper(f):
    def inner(request,*args,**kwargs):
        ret = f(request,*args,**kwargs)
        cook = request.COOKIES.get('k1')
        if cook == 'v1':
            return ret
        else:
            return redirect('login')
    return inner


# 主页
@wrapper
def base(request):
    return render(request,'base.html')


# 解密h5中的加密字段
import pyDes
import base64
Key = 'national'
Iv = None
def hexStringTobytes(str):
    '''
    16进制转bytes
    '''
    str = str.replace(" ", "")
    return bytes.fromhex(str)
# 解密
def decrypt_str(data):
    method = pyDes.des(Key, pyDes.ECB, Iv, pad=None, padmode=pyDes.PAD_PKCS5)
    k =hexStringTobytes(data)
    return method.decrypt(k)


def login(request):
    method = request.method
    # 根据方法不同 确定是请求界面 还是 表达提交
    if method == 'GET':
        # print('================================request请求的方法')
        # print('请求方法', request.method)
        # print('请求的 GET参数的类字典对象',request.GET)
        # print('请求的 POST参数的类字典对象',request.POST)
        # print('请求体',request.body)
        # print('请求头',request.META)
        # print('========================================')
        return render(request,'login.html')
    elif method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '123'  and password =='123':
            # return HttpResponse('登陆成功')
            # 登陆成功，重定向到首页
            ret = redirect('/base/')
            ret.set_cookie('k1','v1')
            return ret
             
        else:
            return HttpResponse('登陆失败') 


# def login(request):
#     method = request.method
#     # 根据方法不同 确定是请求界面 还是 表达提交
#     if method == 'GET':
#         # print('================================request请求的方法')
#         # print('请求方法', request.method)
#         # print('请求的 GET参数的类字典对象',request.GET)
#         # print('请求的 POST参数的类字典对象',request.POST)
#         # print('请求体',request.body)
#         # print('请求头',request.META)
#         # print('========================================')
#         return render(request,'login.html')
#     elif method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         if username == '123'  and password =='123':
#             # return HttpResponse('登陆成功')
#             # 登陆成功，重定向到首页
#             ret = redirect('/base/')
#             return ret
#         else:
#             return HttpResponse('登陆失败')    



# 获取app的验证码
def yanzhengma_app():
    conn = shujuku_app() #链接数据库
    cur2 = conn.cursor(cursor = pymysql.cursors.DictCursor) # 将查询出来的结果制作成字典的形式返回
    cur2.execute('SELECT * from tb_message ORDER BY update_time DESC LIMIT 5;')
    all = cur2.fetchall()   # 获取剩余结果的所有数据
    list1 = []
    for j in all :
        list1.append(j)  
    # print(list1[0]['update_time'])
    # print(type(list1[0]['update_time']))
    return list1

# 获取h5的验证码
def yanzhengma_h5(num):
    conn = shujuku_h5() #链接数据库
    cur2 = conn.cursor(cursor = pymysql.cursors.DictCursor) # 将查询出来的结果制作成字典的形式返回
    num = num
    if num == 7:
        cur2.execute('SELECT * FROM tb_wmp_auth_mobile ORDER BY update_date DESC LIMIT 7;')
    elif num == 5:
        cur2.execute('SELECT * FROM tb_wmp_auth_mobile ORDER BY update_date DESC LIMIT 5;')
    else:
        cur2.execute('SELECT * FROM tb_wmp_auth_mobile ORDER BY update_date DESC LIMIT 3;')
    all = cur2.fetchall()   # 获取剩余结果的所有数据
    list2 = []
    for j in all :
        # print('剩余结果的全部',j)
        list2.append(j) 
    # print(len(list2))
    for i in range(len(list2)):
        list2[i]['encrypt_mobile'] = decrypt_str(list2[i]['encrypt_mobile'])  # 解密
        # print(list2[i].encrypt_mobile)     
    # print(list1[0]['captcha'])
    # print(list2)

    return list2

# 获取验证码 界面
@wrapper
def app1base(request):
    method = request.method
    count = request.POST.get('count')
    print(count)
    if method == 'GET':
        list1 = yanzhengma_app()
        list2 = yanzhengma_h5(5)
        return render(request,'app1.html',locals())
    elif method == 'POST':
        list1 = yanzhengma_app()
        list2 = yanzhengma_h5(5)
        return render(request,'app1.html',locals())

import json
# ajax局部刷新
def ajax_h5(request):
    num = request.POST.get("sele1")
    print(num)
    list3 = yanzhengma_h5(int(num))
    print(type(list3))
    print(list3)
    list4 = []
    for i in range(len(list3)):
        yyy = list3[i]['encrypt_mobile']
        yyy = bytes.decode(yyy)
        print(type(yyy))
        list4.append(yyy)
    print(list4)
    return JsonResponse(list4,safe=False)