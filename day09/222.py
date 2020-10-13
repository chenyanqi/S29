import json

def register():
    username = input('请输入用户名：')
    password = input('请输入密码：')
    user_dic = {"username": username, "password": password}
    with open('usermanage_json', mode='r', encoding='utf-8') as f:
        for line in f:
            dic = json.loads(line)
            if username == dic['username']:
                return False
    with open('usermanage_json', mode='a', encoding='utf-8') as f:
        f.write(json.dumps(user_dic) + '\n')
        return True


def login():
    username = input('请输入用户名：')
    password = input('请输入密码：')
    with open('usermanage_json', mode='r', encoding='utf-8') as f:
        for line in f:
            user_dic = json.loads(line)
            if username == user_dic['username'] and password == user_dic['password']:
                return True
        return


def main():
    menu_map = {'1': login, '2': register}
    info = """
    ************** Welcome to Luffy City ****************
          1、用户登录                2、注册账户
    """
    print(info)
    while True:
        inp = input('请输入功能选项(q|Q)：')
        if inp in menu_map:
            res = menu_map[inp]()
            if res:
                print('成功')
            else:
                print('失败')
        elif inp.upper() == 'Q':
            break
        else:
            print('参数有误，请重新输入！')


if __name__ == '__main__':
    main()
