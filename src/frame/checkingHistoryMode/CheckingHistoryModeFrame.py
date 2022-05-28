from tkinter import *

from QuestionType import qType as qt

from frame.checkingHistoryMode.CheckHistoryFrame import CheckHistoryFrame


class CheckingHistoryModeFrame(Frame):
    initWidth = 750
    initHeight = 600
    bgColor = 'lemonChiffon'

    def __init__(self, parent, user):
        super(CheckingHistoryModeFrame, self).__init__(parent, bg=self.bgColor, width=self.initWidth,
                                                       height=self.initHeight)
        # 问题：frame一定要初始化尺寸！否则默认值会很小，根本看不见

        Label(self, text='请选择题目类型：', bg=self.bgColor, font=('Times', 20, 'bold italic'), width=30,
              height=2).place(x=10, y=10)

        def chooseMulti():
            checkFrame = CheckHistoryFrame(self, user, qt.MULTI)
            checkFrame.place(x=0, y=0)

        def chooseJudge():
            checkFrame = CheckHistoryFrame(self, user, qt.JUDGE)
            checkFrame.place(x=0, y=0)

        def chooseShort():
            checkFrame = CheckHistoryFrame(self, user, qt.SHORT)
            checkFrame.place(x=0, y=0)

        frm = Frame(self, bg='darkKhaki', width=200, height=80)
        frm.place(x=375, y=90, anchor=N)

        btn1 = Button(frm, text='单选题', width=15, height=5, command=chooseMulti)
        btn1.grid(row=0, column=0, padx=30, pady=30)
        btn2 = Button(frm, text='判断题', width=15, height=5, command=chooseJudge)
        btn2.grid(row=1, column=0, padx=30, pady=30)
        btn3 = Button(frm, text='简答题', width=15, height=5, command=chooseShort)
        btn3.grid(row=2, column=0, padx=30, pady=30)
        # command的函数尽量不要有参数，可能会导致先初始化，界面出现顺序错误
