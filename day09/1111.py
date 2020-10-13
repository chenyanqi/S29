import json,os

# 注册

def add():

    with open('user.txt', mode='w', encoding='utf-8') as w:
        user = input('输入用户名称:')
        pas  = input('输入用户密码')

        k = {user:pas}

        # 转换成str
        new = json.dumps(k)
        w.write(new)
        return '用户%s注册成功' % user

# 登录
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

# 主函数

def A():

    # 功能列表
    l = ['注册','登录']

    for i in range(0,len(l)):
        print(i,l[i])

    user_input = input('请选择需要执行的ID:')
    status = True
    while status:
        if not user_input.isdecimal():

            print('输入正确的ID')
            continue
        else:
            if int(user_input) == 0:
                ret = add()
                return ret
            else:
                ret = login()
                return ret

if __name__ == '__main__':
    print(A())
