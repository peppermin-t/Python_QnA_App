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
            myBank = bank.localBank[qt.JUDGE]
        else:
            myBank = {}
            for question in user.answerInfo.getQuestionListByDiff(qt.JUDGE, difficulty):
                myBank[question] = bank.localBank[qt.JUDGE][question]
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
            l_feedback.config(text='')
            note.delete('1.0', END)
            note.insert(INSERT, user.answerInfo.noteInfo[qt.JUDGE][myQuestions[questionIndex]])

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
        # 选项和题目、反馈的frame，固定
        frm = Frame(self, bg=self.bgColor, width=500, height=300)
        frm.place(x=375, y=50, anchor=N)
        # 题干标签，固定
        l_question = Label(frm, text='1. ' + myQuestions[0], wraplength=500, bg=self.bgColor, font=('Arial', 20))
        l_question.grid(row=0, column=0, pady=15)
        # 反馈标签，固定
        l_feedback = Label(frm, bg=self.bgColor, font=('Arial', 15))
        l_feedback.grid(row=3, column=0, pady=15)

        # 笔记，固定
        def saveNote():
            content = note.get('1.0', END)
            user.saveNote(qt.JUDGE, myQuestions[questionIndex], content)

        Label(self, text='笔记：', bg=self.bgColor, font=('Arial', 12, 'italic')).place(x=10, y=440)
        Button(self, text='保存', command=saveNote).place(x=50, y=430)
        note = Text(self, font=('Arial', 13), width=10, height=8)
        note.place(x=10, y=590, anchor=SW)
        note.insert(INSERT, user.answerInfo.noteInfo[qt.JUDGE][myQuestions[0]])

        # 切换题目、确认按键，固定
        def confirmChoice():
            isCorrect = user.answer(qt.JUDGE, myQuestions[questionIndex], answer=var_r.get())
            # 根据user类中的answer方法获得答题正误
            if isCorrect:  # 回答正确，反馈标签变绿色显示正确
                l_feedback.config(text='回答正确！', bg='limeGreen')
            else:  # 回答错误，反馈标签变红色显示错误
                l_feedback.config(text='回答错误！', bg='tomato')

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

        # 选项，不固定
        var_r = StringVar()
        r1 = Radiobutton(frm, text='T', bg=self.bgColor, variable=var_r, value='T')
        r1.grid(row=1, column=0, pady=15)
        r2 = Radiobutton(frm, text='F', bg=self.bgColor, variable=var_r, value='F')
        r2.grid(row=2, column=0, pady=15)
