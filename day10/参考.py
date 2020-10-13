"""
2. 选课系统开发 系统登录需要有两类用户：
    学生, 管理员

    针对不用用户提供不同功能：
        学生用户:
        对于学生用户来说，登陆之后有一下几个功能
             1、查看所有课程
             2、选择课程
             3、查看所选课程
             4、删除已选课程
        管理员用户：
        管理员用户除了可以做一些查看功能之外，还有很多创建工作。
             1、创建课程
             2、创建学生学生账号
             3、查看所有课程
             4、查看所有学生的选课情况
    类:
        学生类
        课程类
        管理员类
        客户端类
"""

# 为了方便. 先初始化userinfo文件
import json
import os
# d = {"username":"admin", "password":"123456", "usertype":0}  # 0: 管理员, 1: 学生
# d_json = json.dumps(d)
# print(d_json)


class Client:
    def __init__(self):
        self.userinfo = None  # 如果是管理员登录. userinfo就是管理员, 如果是学生登录, userinfo就是学生

    def login(self):  # 写有一个登录功能
        # 用户名和密码
        while 1:
            username = input("请输入你的用户名:")
            password = input("请输入你的密码:")
            with open("userinfo", mode="r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    d = json.loads(line)
                    #print(d['username'],d['password'])
                    if username == d['username'] and password == d['password']:
                        print("登录成功")
                        # 判断这个人是管理员还是普通用户
                        # 假设是管理员. 需要把管理员信息保存到客户端
                        # 假设你是学生. 也需要把学生信息保存到客户端
                        if d['usertype'] == 0:  # 管理员
                            self.userinfo = Admin(d['username'], d['password'], d['usertype'])   # 管理员对象-> 管理员类
                        else:  # 学生
                            self.userinfo = Student(d['username'], d['password'], d['usertype'], d['cour_list'])  # 学生对象  ->  学生类
                        return
                else:
                    print("登录失败")

    def startup(self):  # 启动
        self.login()
        # 登录成功了
        if self.userinfo.usertype == 0:
            self.admin_client()
        else:
            self.stu_client()

    def admin_client(self):
        while 1:
            menu = ("创建学生", "创建课程", "查看所有课程", "查看所有学生的选课情况", "退出")
            for i in range(len(menu)):
                print(i+1, menu[i])
            choice = input("请输入你要执行的菜单:")
            if choice == "1":
                # 让管理员去添加新学生
                # 管理员对象????
                self.userinfo.create_student()
            elif choice == "2":
                # 让管理员去创建课程
                self.userinfo.create_course()
            elif choice == "3":
                self.userinfo.show_all_courses()
            elif choice == "4":
                self.userinfo.show_all_students()
            elif choice == "5":
                print("程序退出")
                return
            else:
                print("输入有误. 请重新输入")

    def stu_client(self):
        print("学生登录了")
        while 1:
            menu = ("查看所有课程", "选择课程", "查看所选课程", "删除已选课程", "退出")
            for i in range(len(menu)):
                print(i+1, menu[i])
            choice = input("请输入你要执行的菜单:")
            if choice == "1":
                # 学生查看所有课程
                self.userinfo.show_all_courses()
            elif choice == "2":
                # 学生选课
                self.userinfo.choice()
            elif choice == "3":
                # 学生查看自己选了哪些课
                self.userinfo.show_my_courses()
            elif choice == "4":
                # 学生删除课程-自己的课程
                self.userinfo.del_my_couse()
            elif choice == "5":
                print("程序退出")
                return
            else:
                print("输入有误. 请重新输入")


class Admin:
    def __init__(self, username, password, usertype):
        self.username = username
        self.password = password
        self.usertype = usertype
    def create_student(self):
        username = input("请输入学生的姓名:")
        # 创建学生对象
        s = Student(username, "123456", 1)
        s.write_to_file()  # 学生把自己的信息写入文件中

    def create_course(self):
        cour_name = input("请输入课程名称:")
        c = Course(cour_name)
        c.write_to_file()

    def show_all_courses(self):  # 管理员登录了. 想看所有课程信息.
        lst = Course.get_all_courses()
        # 显示所有课程的信息
        for c in lst:
            print(c.name)

    def show_all_students(self):  # 最后去写他
        # 拿到所有学生信息
        lst = Student.get_all_students()
        for stu in lst:
            stu.show_my_courses()  # 直接调用学生显示自己的课程信息


class Student:
    def __init__(self, username, password, usertype, cour_list=None):  # 自己回去思考. 为什么这里不写[]
        self.username = username
        self.password = password
        self.usertype = usertype
        self.cour_list = cour_list if cour_list else []  # [1,2,3]

    def write_to_file(self):
        with open("userinfo", mode="a", encoding="utf-8") as f:
            # d = {"username": self.username, "password": self.password.....}
            f.write(json.dumps(self.__dict__)+"\n")

    def show_all_courses(self):
        # 拿到所有课程信息
        lst = Course.get_all_courses()
        for i in range(len(lst)):
            print(i+1, lst[i].name)

    def choice(self):  # userinfo
        # 先显示所有的课程. 然后让用户选择
        lst = Course.get_all_courses()
        while 1:
            self.show_all_courses()
            # 1 抽烟
            # 2 喝酒
            # 3 烫头
            c = input("请输入你想学习的课程编号(Q退出):")
            if c.upper() == "Q":
                break
            if c.isdigit():  # 是不是数字
                n = int(c)
                if n >= 1 and n <= len(lst):  # 有没有超过范围
                    if n in self.cour_list:  # 有没有已经选择过了
                        print("您已经选择过这一门课了")
                    else:  # 没选过这一门课
                        self.cour_list.append(n)
                else:
                    print("您输入的课程编号有误, 请重新输入")
            else:
                print('请输入数字')
        # 选完了. 当前选择的课都在内存里. 还没有存到文件里.
        # 把文件的学生信息进行更新
        self.write_course_to_file()
        print("课程信息保存完毕!")

    def write_course_to_file(self):  # userinfo
        with open("userinfo", mode="r", encoding="utf-8") as f1, \
             open("userinfo_副本", mode="w", encoding="utf-8") as f2:
            for line in f1:
                line = line.strip()
                d = json.loads(line)
                if d['username'] == self.username:  # ????
                    f2.write(json.dumps(self.__dict__) + "\n")  # 当前登录的那个人的数据
                else:
                    f2.write(json.dumps(d)+"\n")  # 其他人数据
        os.remove("userinfo")
        os.rename("userinfo_副本", "userinfo")

    def del_my_couse(self):
        while 1:
            self.show_my_courses()
            c = input("请输入你要删除的课程(Q退出):")
            if c.upper() == "Q":
                break
            if c.isdigit():
                c = int(c)
                if c in self.cour_list:
                    self.cour_list.remove(c)
                else:
                    print("没这个课")
            else:
                print('重新输入')

        self.write_course_to_file()

    def show_my_courses(self):   # 某个学生的具体课程信息
        # 学生选了那些课. 早就放在学生的cour_list里面了
        # self.cour_list  # [1,2,3]
        lst = Course.get_all_courses()  #  ???????? [抽烟, 喝酒, 烫头, 保健]
        print(f"{self.username}一共选择了以下课程:")
        for i in self.cour_list:  # 1 2 3
            print(i, lst[i - 1].name)

    @staticmethod
    def get_all_students():
        lst = []
        with open("userinfo", mode="r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                d = json.loads(line)
                if d['usertype'] == 0:  # 筛掉管理员
                    continue
                s = Student(d['username'], d["password"],d['usertype'], d['cour_list'])
                lst.append(s)
        return lst


class Course:
    def __init__(self, name):
        self.name = name

    def write_to_file(self):
        with open("course", mode="a", encoding="utf-8") as f:
            f.write(self.name+"\n")

    @staticmethod
    def get_all_courses():  # 拿到所有课程信息. 拿到所有课程对象
        lst = []
        with open("course", mode="r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                c = Course(line)   # str
                lst.append(c)
        return lst  # 返回所有课程对象的列表


if __name__ == '__main__':
    c = Client()
    c.startup()
