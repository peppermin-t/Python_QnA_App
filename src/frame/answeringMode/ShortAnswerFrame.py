from random import shuffle
from tkinter import *
from tkinter import messagebox

from QuestionType import qType as qt

from QuestionBank import bank


class AnswerFrame(Frame):
    initWidth = 750
    initHeight = 600
    bgColor = 'khaki'

    def __init__(self, parent, user, shuffle_mode=False, bg=bgColor, width=750, height=600, difficulty=None):
        super(AnswerFrame, self).__init__(parent, bg=bg, width=width, height=height)
        # 载入需要的题库
        if difficulty is None:
            myBank = bank.localBank[qt.SHORT]
        else:
            myBank = {}
            for question in user.answerInfo.getQuestionListByDiff(qt.SHORT, difficulty):
                myBank[question] = bank.localBank[qt.SHORT][question]
        myQuestions = list(myBank.keys())
        if shuffle_mode:
            shuffle(myQuestions)
        # 当前界面问题序号
        global questionIndex
        # global变量在外部也必须声明为global，否则内部声明会覆盖，显示未初始化
        questionIndex = 0

        # 返回按钮，固定
        Button(self, text='返回', command=self.destroy).place(x=10, y=10)

        # 换题更新内容，不固定
        def updateWidgets():
            l_question.config(text=str(questionIndex + 1) + '. ' + myQuestions[questionIndex])
            l_feedback_note.config(text='')
            l_feedback.config(text='')
            btn1.config(state=DISABLED)
            btn2.config(state=DISABLED)
            note.delete('1.0', END)
            note.insert(INSERT, user.answerInfo.noteInfo[qt.SHORT][myQuestions[questionIndex]])

        # 选题索引列表，固定
        def goToQuestion(event):
            global questionIndex
            questionIndex = lb.get(lb.curselection()) - 1
            updateWidgets()

        Label(self, text='跳至题号：', bg=self.bgColor, font=('Arial', 12, 'italic')).place(x=10, y=75)
        inputList = StringVar()
        inputList.set(tuple(i + 1 for i in range(len(myBank))))
        lb = Listbox(self, listvariable=inputList, width=7)
        lb.bind('<Double-Button-1>', goToQuestion)
        lb.place(x=10, y=100)
        # 题干标签，固定
        l_question = Label(self, text='1. ' + myQuestions[0], wraplength=500, bg=self.bgColor, font=('Arial', 20))
        l_question.place(x=375, y=50, anchor=N)
        # 反馈标签，固定
        l_feedback_note = Label(self, text='', bg=self.bgColor, font=('Arial', 12, 'italic'))
        l_feedback_note.place(x=100, y=325)
        l_feedback = Label(self, text='', anchor=NW, wraplength=500, justify='left', bg=self.bgColor,
                           font=('Arial', 15))
        l_feedback.place(x=375, y=350, anchor=N)

        # 笔记，固定
        def saveNote():
            content = note.get('1.0', END)
            user.saveNote(qt.SHORT, myQuestions[questionIndex], content)

        Label(self, text='笔记：', bg=self.bgColor, font=('Arial', 12, 'italic')).place(x=10, y=440)
        Button(self, text='保存', command=saveNote).place(x=50, y=430)
        note = Text(self, font=('Arial', 13), width=10, height=8)
        note.place(x=10, y=590, anchor=SW)
        note.insert(INSERT, user.answerInfo.noteInfo[qt.SHORT][myQuestions[0]])

        # 切换题目、确认按键，固定
        def confirmChoice():
            l_feedback_note.config(text='参考答案：')
            l_feedback.config(text=myBank[myQuestions[questionIndex]])
            btn1.config(state=NORMAL)
            btn2.config(state=NORMAL)

        def goLast():
            global questionIndex
            if questionIndex == 0:
                messagebox.showerror(title='Error', message='已经是第一题啦！')
            else:
                questionIndex -= 1
                updateWidgets()

        def goNext():
            global questionIndex
            if questionIndex == len(myBank) - 1:
                messagebox.showerror(title='Error', message='已经是最后一题啦！')
            else:
                questionIndex += 1
                updateWidgets()

        Button(self, text='提交', command=confirmChoice).place(x=375, y=500, anchor=N)
        Button(self, text='上一题', command=goLast).place(x=200, y=500, anchor=N)
        Button(self, text='下一题', command=goNext).place(x=550, y=500, anchor=N)

        # 简答题输入，不固定
        Label(self, text='在此作答：', bg=self.bgColor, font=('Arial', 12, 'italic')).place(x=100, y=125)
        Text(self, font=('Arial', 15), width=60, height=8).place(x=375, y=150, anchor=N)

        # 记得选项，不固定
        def remember():
            user.answer(qt.SHORT, myQuestions[questionIndex], first_hand=True)

        def forget():
            user.answer(qt.SHORT, myQuestions[questionIndex], first_hand=False)

        btn1 = Button(self, text='我还记得', command=remember, state=DISABLED)
        btn1.place(x=300, y=450, anchor=N)
        btn2 = Button(self, text='我忘记了', command=forget, state=DISABLED)
        btn2.place(x=450, y=450, anchor=N)
