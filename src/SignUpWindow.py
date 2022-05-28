import os
import pickle
from tkinter import *
from tkinter import messagebox

import BasicSettings
from user import User


class SignUpWindow(Toplevel):
    my_title = 'Sign Up'
    initWidth = 500
    initHeight = 400
    bgColor = 'lightGreen'

    def __init__(self):
        super(SignUpWindow, self).__init__()
        self.setUI()

    def setUI(self):
        BasicSettings.setBasic(self)

        l1 = Label(self, bg=self.bgColor, text='用户名：')
        l2 = Label(self, bg=self.bgColor, text='密码：')
        l3 = Label(self, bg=self.bgColor, text='确认密码：')
        l1.place(x=180, y=100, anchor=NE)
        l2.place(x=180, y=140, anchor=NE)
        l3.place(x=180, y=180, anchor=NE)

        e1 = Entry(self, show=None)
        e2 = Entry(self, show='*')
        e3 = Entry(self, show='*')
        e1.place(x=200, y=100)
        e2.place(x=200, y=140)
        e3.place(x=200, y=180)

        def usrSignUp():
            username = e1.get()  # 获得用户输入的新用户名
            pw1 = e2.get()  # 获得用户第一遍输入的新密码
            pw2 = e3.get()  # 获得用户第二遍输入的新密码
            if os.path.exists(f'./resource/usrInfos/usr_{username}.pkl'):  # 在本地找到该用户名用户的注册信息
                messagebox.showerror(title='Error', message='用户名已存在！')  # 已注册过，注册失败
                return
            elif pw1 != pw2:  # 两次输入的密码不一致
                messagebox.showerror(title='Error', message='两次输入的密码不一致！')  # 两次输入的密码不一致，注册失败
                return
            else:  # 满足所有新用户注册条件
                with open(f'./resource/usrInfos/usr_{username}.pkl', 'wb') as f:
                    # 在本地创建新用户
                    newUser = User(username, pw1)
                    pickle.dump(newUser, f)
            self.destroy()  # 退出注册窗口

        Button(self, bd=0, text='确认', command=usrSignUp).place(x=225, y=280, anchor=NE)
        Button(self, bd=0, text='取消', command=self.destroy).place(x=275, y=280, anchor=NW)
