# 模拟博客园登录：
# 1)，启动程序，首页面应该显示成如下格式：
#

# 欢迎来到博客园首页
# 1:请登录
# 2:请注册
# 3:文章页面
# 4:日记页面
# 5:评论页面
# 6:收藏页面
# 7:注销
# 8:退出程序

# 2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。


# 3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，没成功则结束整个程序运行，成功之后，可以选择访问3~6项，访问页面之前，必须要在log文件中打印日志，日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，访问页面时，页面内容为：欢迎xx用户访问评论（文章，日记，收藏）页面



# 4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。

# 5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。

# 6)，退出程序为结束整个程序运行。
import time

login_status = {"username":None,"status":False}

def log(f):
    def inner(*args,**kwargs):
        struct_time = time.localtime()
        time_now = time.strftime("%Y-%m-%d %H:%M:%S",struct_time)
        with open("log.txt","a",encoding='utf-8') as f1:
            f1.write("在%s执行了 %s函数\n"%(time_now, f.__name__))
        res = f(*args, **kwargs)
        return res
    return inner




def func(f):
    def inner(*args,**kwargs):
        if login_status["status"]:

            res = f(*args, **kwargs)
            return res
        else:
            print("你需要登录")
            res_dict = login()
            if res_dict["status"]==True:
                res = f(*args, **kwargs)
                return res
    return inner




def login(*args):
    print("login函数")
    if args:
        login_status["username"] = args
        login_status["status"] = True
        return login_status
    n = 3
    while n >0:
        username = input("用户名")
        password = input("密码")
        with open(r"username","r",encoding='utf-8') as f:
            for line in f:
                name, pwd = line.strip().split("|")
                if username == name and password == pwd:
                    print("登陆成功")
                    login_status["username"] = username
                    login_status["status"] = True
                    n=0
                    return login_status
            else:
                print("登陆失败")
                n -= 1
                print("你还有%s次机会"%n)


def register():
    print("register函数")
    username = input("用户名")
    password = input("密码")

    with open(r"username", "r", encoding='utf-8') as f,\
        open(r"username", 'a', encoding='utf-8') as f2:
        for i in f:
            if username == i.strip().split("|")[0]:
                print("用户名已经存在")
                break
        else:
            f2.write(username + "|" + password + "\n")
            print("你注册成功了")
            return login(username,)

@func
@log
def article():
    print("article函数")


@func
def diary():
    print("diary函数")

@func
def comment():
    print("comment函数")
@func
def shoucang():
    print("shoucang函数")


def login_out():

    login_status["username"] = None
    login_status["status"] = False
    print("注销成功")

def quit_q():
    print("退出")
    exit()


choice_dict = {
    1:login,
    2:register,
    3:article,
    4:diary,
    5:comment,
    6:shoucang,
    7:login_out,
    8:quit_q,
}
while True:
    l = [
        '请登录',
        '请注册',
        '文章页面',
        '日记页面',
        '评论页面',
        '收藏页面',
        '注销',
        '退出程序',
    ]

    for i, v in enumerate(l, 1):
        print(i, v)

    inp = input("请输入你要选择的序号").strip()

    if inp.isdigit():
        inp = int(inp)
        if 0<inp<=len(choice_dict):
            choice_dict[inp]()
        else:
            print("你输入的不合法")
    else:
        print("你不合法")

