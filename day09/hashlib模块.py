import hashlib
from getpass import getpass
# md5 = hashlib.md5(b'123456')
# ret=md5.hexdigest()
# print(ret)




def md5(s):
    md5 = hashlib.md5(b'username')
    md5.update(s.encode('utf-8'))
    ret = md5.hexdigest()
    return md5

def register():
    username = input('请输入您的用户名：')
    password = input('请输入您的密码：')
    with open('user.txt', mode='w', encoding='utf-8') as f:
        f.write('%s:%s' %(username,md5(password)))
    return True


def login(username,password):

    with open('user.txt',mode='r',encoding='utf-8') as f:
        for line in f:
            user,md5_pwd= line.split(':')
            if user == username and md5(password) == md5_pwd:
                return True
            else:
                return False




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

if __name__ == '__main__':
    welcome()
