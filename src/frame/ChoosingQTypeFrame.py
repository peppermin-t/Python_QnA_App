from tkinter import *

from frame.answeringMode import JudgeAnswerFrame
from frame.answeringMode import MultiAnswerFrame
from frame.answeringMode import ShortAnswerFrame
from frame.learningMode import JudgeLearnFrame
from frame.learningMode import MultiLearnFrame
from frame.learningMode import ShortLearnFrame


class ChoosingQTypeFrame(Frame):
    initWidth = 750
    initHeight = 600
    bgColor = 'paleGreen'

    def __init__(self, parent, user, mode):
        self.bottomImage = PhotoImage(file='./resource/assets/MainWindowBackground.gif')
        super(ChoosingQTypeFrame, self).__init__(parent, bg=self.bgColor, width=self.initWidth, height=self.initHeight)
        # 问题：frame一定要初始化尺寸！否则默认值会很小，根本看不见

        Label(self, text='请选择题目类型：', bg='yellowGreen', font=('Times', 20, 'bold italic'), width=30,
              height=2).place(x=10, y=10)

        def chooseMulti(shuffle, diff=None):
            if mode == 'answer':
                frm_son = MultiAnswerFrame.AnswerFrame(self, user, shuffle)
            elif mode == 'learn':
                frm_son = MultiLearnFrame.AnswerFrame(self, user, shuffle)
            else:
                frm_son = MultiAnswerFrame.AnswerFrame(self, user, shuffle, difficulty=diff)

            frm_son.place(x=0, y=0)

        def chooseJudge(shuffle, diff=None):
            if mode == 'answer':
                frm_son = JudgeAnswerFrame.AnswerFrame(self, user, shuffle)
            elif mode == 'learn':
                frm_son = JudgeLearnFrame.AnswerFrame(self, user, shuffle)
            else:
                frm_son = JudgeAnswerFrame.AnswerFrame(self, user, shuffle, difficulty=diff)
            frm_son.place(x=0, y=0)

        def chooseShort(shuffle, diff=None):
            if mode == 'answer':
                frm_son = ShortAnswerFrame.AnswerFrame(self, user, shuffle)
            elif mode == 'learn':
                frm_son = ShortLearnFrame.AnswerFrame(self, user, shuffle)
            else:
                frm_son = ShortAnswerFrame.AnswerFrame(self, user, shuffle, difficulty=diff)
            frm_son.place(x=0, y=0)

        frm = Frame(self, bg='yellowGreen', width=200, height=80)
        frm.place(x=375, y=90, anchor=N)

        btn1 = Button(frm, text='单选题', width=15, height=5, command=lambda: chooseMulti(False))
        btn3 = Button(frm, text='判断题', width=15, height=5, command=lambda: chooseJudge(False))
        btn5 = Button(frm, text='简答题', width=15, height=5, command=lambda: chooseShort(False))
        btn2 = Button(frm, text='单选题\n乱序', width=15, height=5, command=lambda: chooseMulti(True))
        btn4 = Button(frm, text='判断题\n乱序', width=15, height=5, command=lambda: chooseJudge(True))
        btn6 = Button(frm, text='简答题\n乱序', width=15, height=5, command=lambda: chooseShort(True))
        # command的函数尽量不要有参数，可能会导致先初始化，界面出现顺序错误
        # command有参数，则采用lambda函数

        if mode != 'practice':
            btn1.grid(row=0, column=0, padx=30, pady=30)
            btn3.grid(row=1, column=0, padx=30, pady=30)
            btn5.grid(row=2, column=0, padx=30, pady=30)
            btn2.grid(row=0, column=1, padx=30, pady=30)
            btn4.grid(row=1, column=1, padx=30, pady=30)
            btn6.grid(row=2, column=1, padx=30, pady=30)

        else:
            btn1.config(state=DISABLED)
            btn3.config(state=DISABLED)
            btn5.config(state=DISABLED)
            btn1.grid(row=0, column=0, padx=30, pady=30, rowspan=3)
            btn3.grid(row=3, column=0, padx=30, pady=30, rowspan=3)
            btn5.grid(row=6, column=0, padx=30, pady=30, rowspan=3)

            btn11 = Button(frm, text=f'Level 1', width=15, height=1, command=lambda: chooseMulti(False, diff=1))
            btn11.grid(row=0, column=1, padx=1, pady=1)
            btn12 = Button(frm, text=f'Level 2', width=15, height=1, command=lambda: chooseMulti(False, diff=2))
            btn12.grid(row=1, column=1, padx=1, pady=1)
            btn13 = Button(frm, text=f'Level 3', width=15, height=1, command=lambda: chooseMulti(False, diff=3))
            btn13.grid(row=2, column=1, padx=1, pady=1)

            btn21 = Button(frm, text=f'Level 1', width=15, height=1, command=lambda: chooseJudge(False, diff=1))
            btn21.grid(row=3, column=1, padx=1, pady=1)
            btn22 = Button(frm, text=f'Level 2', width=15, height=1, command=lambda: chooseJudge(False, diff=2))
            btn22.grid(row=4, column=1, padx=1, pady=1)
            btn23 = Button(frm, text=f'Level 3', width=15, height=1, command=lambda: chooseJudge(False, diff=3))
            btn23.grid(row=5, column=1, padx=1, pady=1)

            btn31 = Button(frm, text=f'Level 1', width=15, height=1, command=lambda: chooseShort(False, diff=1))
            btn31.grid(row=6, column=1, padx=1, pady=1)
            btn32 = Button(frm, text=f'Level 2', width=15, height=1, command=lambda: chooseShort(False, diff=2))
            btn32.grid(row=7, column=1, padx=1, pady=1)
            btn33 = Button(frm, text=f'Level 3', width=15, height=1, command=lambda: chooseShort(False, diff=3))
            btn33.grid(row=8, column=1, padx=1, pady=1)

            # 用循环diff = i+1会覆盖，不知道为什么
