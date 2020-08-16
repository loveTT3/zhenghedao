import pymysql

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

shujuku_h5()
yanzhengma_h5()