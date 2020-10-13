# import json
# dic = {'k':'v','k1':'v1'}
# print(type(dic),dic)
# jdic = json.dumps(dic)
# print(type(jdic),jdic)
#
# with open('dic_test','w') as f:
#     f.write(jdic)


# import pickle
# dic = {"k":{1,2,3},"k2":"v2"}
# pdic = pickle.dumps(dic)
# print(pdic)
#
# ret = pickle.loads(pdic)
# print(ret)
# import  json,pickle
# data = {
# {"username":'alex','password':'123'},
# {"username":'wusir','password':'456'},
# {"username":'xupeng','password':'789'}
# }
#
# with open('dic_test','w') as f:
#     pickle.dumps(data)
#
#
# with open('dic_test','rb') as f:
#     line = f.readline()
#     data = pickle.load(line)
#     print(data)

import  json,os

def login():
    with open('user.txt', mode='r', encoding='utf-8') as r:
        user = input('输入用户名:')
        pas = input('输入密码:')

        for i in r.readlines():
            o = json.loads(i)
            if user in o:

                # 校验密码
                p = o.get(user)
                if pas == p:
                    return '用户%s登录成功' %user
        return '用户%s不存在' %user


def register():
    with open('user.txt', mode='w', encoding='utf-8') as w:
        user = input('输入用户名称:')
        pas = input('输入用户密码')

        k = {user: pas}

        # 转换成str
        new = json.dumps(k)
        w.write(new)
        return '用户%s注册成功' % user







def welcome():
    while 1:
        lst = ['登陆','注册']
        for i in range(len(lst)):
            print(i+1,lst[i])
        client_select = input('欢迎登陆小站，请选择你的操作：').isdecimal()
        if  client_select == 1:
            ret = login()
            return ret
        elif client_select == 2:
            ret = register()
            return ret


welcome()

