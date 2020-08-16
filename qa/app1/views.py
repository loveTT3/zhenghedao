from django.shortcuts import render,HttpResponse,redirect
import pymysql
# Create your views here.
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

# 登陆
def login(request):
    return(request,'login.html')
# 主页
def base(request):
    return render(request,'base.html')



def login(request):
    method = request.method
    # 根据方法不同 确定是请求界面 还是 表达提交
    if method == 'GET':
        print('================================request请求的方法')
        print('请求方法', request.method)
        print('请求的 GET参数的类字典对象',request.GET)
        print('请求的 POST参数的类字典对象',request.POST)
        print('请求体',request.body)
        print('请求头',request.META)
        print('========================================')
        return render(request,'login.html')
    elif method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '123'  and password =='123':
            # return HttpResponse('登陆成功')
            # 登陆成功，重定向到首页
            return redirect('/base/')
        else:
            return HttpResponse('登陆失败')    

def yanzhengma_app():
    conn = shujuku_app() #链接数据库
    cur2 = conn.cursor(cursor = pymysql.cursors.DictCursor) # 将查询出来的结果制作成字典的形式返回
    cur2.execute('SELECT * from tb_message ORDER BY update_time DESC LIMIT 3;')
    all = cur2.fetchall()   # 获取剩余结果的所有数据
    list1 = []
    for j in all :
        # print('剩余结果的全部',j)
        list1.append(j)  
    # print(list1[0]['captcha'])
    # print(list1[1])
    # print(list1[2])
    return list1
def yanzhengma_h5():
    conn = shujuku_h5() #链接数据库
    cur2 = conn.cursor(cursor = pymysql.cursors.DictCursor) # 将查询出来的结果制作成字典的形式返回
    cur2.execute('SELECT * FROM tb_wmp_auth_mobile ORDER BY update_date DESC LIMIT 3;')
    all = cur2.fetchall()   # 获取剩余结果的所有数据
    list2 = []
    for j in all :
        print('剩余结果的全部',j)
        list2.append(j)  
    # print(list1[0]['captcha'])
    # print(list1[1])
    # print(list1[2])
    return list2

# 获取验证码
def app1base(request):
    method = request.method
    if method == 'GET':
        list1 = yanzhengma_app()
        list2 = yanzhengma_h5()
        return render(request,'app1.html',locals())
    elif method == 'POST':
        list1 = yanzhengma_app()
        list2 = yanzhengma_h5()
        return render(request,'app1.html',locals())