from tkinter import *

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class CheckHistoryFrame(Frame):
    initWidth = 750
    initHeight = 600
    bgColor = 'lemonChiffon'

    def __init__(self, parent, user, qType):
        super(CheckHistoryFrame, self).__init__(parent, bg=self.bgColor, width=self.initWidth, height=self.initHeight)

        answerInfo = user.answerInfo
        Button(self, text='返回', command=self.destroy).place(x=10, y=10)

        errorRateList = []
        for info in answerInfo.getQuestionInfo(qType).values():
            try:
                errorRateList.append(info[0] / info[1])
            except ZeroDivisionError:
                errorRateList.append(0)

        def drawBar():
            f.clear()  # 清空画布上原有的图像
            ax = f.add_subplot(111)  # 在图像上添加子图

            length = len(answerInfo.getQuestionInfo(qType))  # 获得所要分析的题目数量
            data = np.array(errorRateList[: length])  # 获得纵轴值列表
            ind = np.arange(1, length + 1)  # 构造横轴值列表
            width = .5  # 设置每个条所占的宽度
            ax.bar(ind, data, width)  # 绘图
            ax.set_title("Correct Rate Bar Chart")  # 设置标题

            canvas.draw()  # 将图画在画布上

        def drawLine():
            f.clear()
            ax = f.add_subplot(111)

            length = len(answerInfo.getQuestionInfo(qType))
            data = np.array(errorRateList[: length])
            ind = np.arange(1, length + 1)  # the x locations for the groups
            width = .5
            ax.plot(ind, data, width)
            ax.set_title("Correct Rate Line Chart")

            canvas.draw()

        def drawPie():
            f.clear()
            ax = f.add_subplot(111)

            def getPercent(myList):
                sum = 0
                myNewList = myList.copy()
                for i in myNewList:
                    sum += i
                if sum != 0:
                    for i in range(len(myNewList)):
                        myNewList[i] /= sum
                return myNewList

            length = len(answerInfo.getQuestionInfo(qType))
            newErrorRateList = getPercent(errorRateList)
            data = np.array(newErrorRateList[: length]).astype(float)
            ind = np.arange(1, length + 1)  # the x locations for the groups
            ax.pie(data, labels=ind, autopct='%.1f%%', startangle=90, counterclock=False,
                   wedgeprops=dict(width=0.6, edgecolor='w'))
            ax.set_title("Correct Rate Pie Chart")
            ax.axis("equal")

            canvas.draw()

        frm_option = Frame(self, bg=self.bgColor, width=100, height=30)
        frm_option.place(x=10, y=200)
        Button(frm_option, text='条形图', command=drawBar).grid(row=0, column=0, pady=10)
        Button(frm_option, text='折线图', command=drawLine).grid(row=1, column=0, pady=10)
        Button(frm_option, text='饼状图', command=drawPie).grid(row=2, column=0, pady=10)

        frm = Frame(self, bg=self.bgColor, width=400, height=300)
        frm.place(x=375, y=300, anchor=CENTER)

        f = Figure(figsize=(5.4, 4.05), dpi=100)  # 建立新图像
        canvas = FigureCanvasTkAgg(f, frm)  # 创建放置图像的画布
        canvas.get_tk_widget().pack()  # 将画布放置在框架上

# 一个bug：canvas = FigureCanvasTkAgg(f, self)的话会覆盖self这个frame，只有在同一层次上place这个frame才行，因此我多加了一个frame
