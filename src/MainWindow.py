from tkinter import *
from tkinter import messagebox
import pickle

import BasicSettings

from SignUpWindow import SignUpWindow
from WorkingInterface import WorkingInterface


class MainWindow(Tk):
    my_title = 'PY Q&A Login'
    initWidth = 500
    initHeight = 300
    bgColor = 'white'

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setUI()

    def setUI(self):
        BasicSettings.setBasic(self)

        self.icon = PhotoImage(file='./resource/assets/icon.png')
        self.iconphoto(True, self.icon)

        # PhotoImage加载图片时这点很重要，必须是全局的/或在类中声明为类拥有的变量
        # # 方法一：global image
        # # 方法二：
        # https://blog.csdn.net/qq_23985359/article/details/86777367
        self.image = PhotoImage(file='./resource/assets/Welcome.gif')
        canvas = Canvas(self, bg='white', height=80, width=self.initWidth)
        canvas.create_image(360, 30, image=self.image)
        canvas.place(x=250, y=0, anchor=N)

        l1 = Label(self, bg=self.bgColor, text='用户名：')
        l2 = Label(self, bg=self.bgColor, text='密码：')
        l1.place(x=120, y=100)
        l2.place(x=120, y=140)

        e1 = Entry(self, bd=0, show=None)
        e2 = Entry(self, bd=0, show='*')
        e1.place(x=200, y=100)
        e2.place(x=200, y=140)

        def usrSignUp():
            # 新建用户注册窗口
            signUpWindow = SignUpWindow()
            signUpWindow.mainloop()

        def usrLogin():
            username = e1.get()  # 获得用户输入的用户名
            password = e2.get()  # 获得用户输入的密码
            try:
                with open(f'./resource/usrInfos/usr_{username}.pkl', 'rb') as f:
                    # 尝试打开本地用户文件，存在则证明该用户已注册过
                    currentUser = pickle.load(f)  # 获取该用户信息
                    if currentUser.password == password:  # 密码输入正确
                        # 登录成功，新建并进入工作窗口
                        workingInterface = WorkingInterface(currentUser)
                        workingInterface.mainloop()
                        # self.destroy()
                    else:  # 密码输入错误
                        messagebox.showerror(title='Error', message='密码错误！')  # 弹出错误提示框
            except FileNotFoundError:
                # 打开用户文件失败，该用户未注册过
                wantToSignUp = messagebox.askyesno(title='提示',
                                                   message="你还没注册过呢。\n你现在想注册一个新的账户吗？")  # 弹出错误提示框，询问是否需要注册新用户
                if wantToSignUp:  # 用户需要注册
                    usrSignUp()  # 跳至用户注册功能函数

        def _quit():
            # save user
            self.quit()
            self.destroy()

        Button(self, bd=0, text='注册', command=usrSignUp).place(x=175, y=210, anchor=NE)
        Button(self, bd=0, text='登录', command=usrLogin).place(x=250, y=210, anchor=N)
        Button(self, bd=0, text='退出', command=_quit).place(x=325, y=210, anchor=NW)
