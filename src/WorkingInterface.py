import os
from tkinter import *
from tkinter import messagebox

import BasicSettings
from frame.checkingHistoryMode.CheckingHistoryModeFrame import CheckingHistoryModeFrame
from frame.ChoosingQTypeFrame import ChoosingQTypeFrame


class WorkingInterface(Toplevel):
    my_title = 'PY Q&A'
    initWidth = 1000
    initHeight = 600
    bgColor = 'white'

    def __init__(self, user):
        super(WorkingInterface, self).__init__()
        self.user = user
        self.setUI()

    def setUI(self):
        BasicSettings.setBasic(self)
        self.bottomImage = PhotoImage(file='./resource/assets/MainWindowBackground.gif')

        canvas = Canvas(self, bg='black', width=750, height=self.initHeight)
        canvas.create_image(750, 600, image=self.bottomImage, anchor=SE)
        canvas.place(x=250, y=0, anchor=NW)

        def answer():
            frm = ChoosingQTypeFrame(self, self.user, mode='answer')
            frm.place(x=250, y=0)

        def learn():
            frm = ChoosingQTypeFrame(self, self.user, mode='learn')
            frm.place(x=250, y=0)

        def checkHistory():
            frm = CheckingHistoryModeFrame(self, self.user)
            frm.place(x=250, y=0)

        def practiceDifficulty():
            frm = ChoosingQTypeFrame(self, self.user, mode='practice')
            frm.place(x=250, y=0)

        Button(self, text='做题模式', command=answer).place(x=125, y=100, anchor=N)
        Button(self, text='背题模式', command=learn).place(x=125, y=150, anchor=N)
        Button(self, text='历史记录', command=checkHistory).place(x=125, y=200, anchor=N)
        Button(self, text='难度分级', command=practiceDifficulty).place(x=125, y=250, anchor=N)

        Label(self, text=self.user.name, bg=self.bgColor, font=('Times', 20, 'bold')).place(x=125, y=400, anchor=N)

        Button(self, text='退出', command=self.destroy).place(x=125, y=450, anchor=N)

        def _destroyAccount():
            wannaDestroy = messagebox.askyesno(title='提示', message='确定想注销你的账户吗？\n你将丢失你的所有信息')
            if wannaDestroy:
                os.remove(f'./resource/usrInfos/usr_{self.user.name}.pkl')
                self.destroy()

        Button(self, text='注销并退出', command=_destroyAccount).place(x=125, y=500, anchor=N)
