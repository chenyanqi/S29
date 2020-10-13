# def login(username,password):
#     """
#     此函数用于用户登录验证
#     :param username:用户名
#     :param password:密码
#     :return:True 表示用户验证成功，False 表示用户验证失败
#     """
#     with open("login.txt","r",encoding="utf-8") as f:
#      for line in f:
#         #默认strip无参数:删除字符串左右两边的空格或者换行符
#         #有参数：删除两侧指定的值
#         line_new=line.strip()
#         #指定分隔符对字符串进行切片，最终输出一个列表
#         line_list=line_new.split("&")
#         if username==line_list[0] and password==line_list[1]:
#             return True
#      return False
#
# def register(username,password):
#     """
#     此函数用于用户注册
#     :param username: 用户名
#     :param password: 密码
#     :return: True表示用户注册成功
#     """
#     with open("login.txt","a",encoding="utf-8") as f:
#         temp="\n"+username+"&"+password
#         f.write(temp)
#     return True
#
#
# def user_exist(username):
#     """
#     此函数用于判断用户是否已注册
#     :param username: 用户名
#     :return: True表示注册成功，False表示注册失败
#     """
#     with open("login.txt", "r", encoding="utf-8") as f:
#         for line in f:
#             line_new=line.strip()
#             line_list=line_new.split("&")
#             if username==line_list[0]:
#                 return True
#     return False
#
# #定义一个主函数，执行操作
# def main():
#   while 1:
#      print("欢迎登录学生选课系统")
#      inp=input("1,登录，2，注册:")
#
#      if inp=="1":
#          user = input('请输入用户名:')
#          pwd = input('请输入密码:')
#          is_login = login(user, pwd)
#          if is_login:
#              print("登录成功")
#          else:
#              print("登录失败")
#      elif inp=="2":
#          user = input('请输入用户名:')
#          pwd = input('请输入密码:')
#          is_exist=user_exist(user)
#          if is_exist:
#              print("该用户已注册")
#          else:
#              result=register(user,pwd)
#              if result:
#                  print("注册成功")
#              else:
#                  print("注册失败")
#
# main()
#
#
# =============================================================

import json
import os
#初始化管理员进系统
# with open("userinfo",encoding="utf-8",mode='w') as f:
#     d = {"username": "admin", "password": 12345, "usertype": 0}
#     d_json = json.dumps(d)
#     f.write(d_json)

class Client:
    def __init__(self):
        self.userinfo = None

    def login(self):
        while 1:
            print("****欢迎登陆选课系统，请进行登陆****")
            username = input("请输入您的用户名:")
            password = input("请输入您的密码:")
            with open("userinfo",mode="r",encoding="utf-8") as  f:
                for line in f:
                    line = line.strip()
                    d = json.loads(line)
                    #print(d)
                    if username == d['username'] and password == d['password']:
                        print("登陆成功")
                        if d['usertype'] == 0:  # 管理员
                            self.userinfo = Admin(d['username'], d['password'], d['usertype'])   # 管理员对象-> 管理员类
                        else:  # 学生
                            self.userinfo = Student(d['username'], d['password'], d['usertype'], d['cour_list'])  # 学生对象  ->  学生类
                        return
                else:
                    print("登陆失败")

    def startup(self):
        self.login()
        if self.userinfo.usertype == 0:
            print(f"欢迎管理员{self.userinfo.username}登陆")
            self.admin_client()
        else:
            print("欢迎%s同学"% self.userinfo.username )
            self.stu_client()


    def admin_client(self):
        while 1:
            menu = ("创建学生","创建课程", "查看所有课程", "查看所有学生的选课情况", "退出")
            for i in range(len(menu)):
                print(i+1,menu[i])
            choice = input("请输入您要执行的菜单：")
            if choice == "1":
                ls = self.userinfo.create_student()
                print(ls)
            elif choice == "2":
                self.userinfo.create_course()
            elif choice == "3":
                self.userinfo.show_all_course()
            elif choice == "4":
                self.userinfo.show_all_student()
            elif choice == "5":
                print("程序退出")
                return
            else:
                print("输入有误，请重新输入")




    def stu_client(self):
        pass

class Admin():
    def __init__(self,username,password,usertype):
        self.username = username
        self.password = password
        self.usertype = usertype

    def create_student(self):
        username = input("请输入要添加的学生的姓名：")
        s = Student(username,"123456",1)
        s.write_to_file()
        return f"哇,{username}|同学创建成功"

    def create_course(self):
        cour_name = input("请输入课程名称：")
        c = Course(cour_name)
        c.write_to_file()

class Student():
    def __init__(self,username,password,usertype,cour_list=None):
        self.username = username
        self.password = password
        self.usertype = usertype
        self.cour_list = cour_list if cour_list else []

    def write_to_file(self):
        with open("userinfo",mode='a',encoding='utf-8') as f:
            f.write(json.dumps(self.__dict__)+"\n")
        return "创建同学成功"


class Course:
    def __init__(self,name):
        self.name = name

    def write_to_file(self):
        with open("course",mode="a",encoding="utf-8") as f:
            f.write(self.name+"\n")


if __name__ == '__main__':
    c = Client()
    c.startup()
