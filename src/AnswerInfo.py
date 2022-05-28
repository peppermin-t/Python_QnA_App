from math import ceil

from QuestionType import qType as qt
from QuestionBank import bank


class AnswerInfo:
    def __init__(self):
        self.questionInfo = {qt.MULTI: {}, qt.JUDGE: {}, qt.SHORT: {}}
        self.noteInfo = {qt.MULTI: {}, qt.JUDGE: {}, qt.SHORT: {}}
        multi = self.questionInfo[qt.MULTI]
        multi_note = self.noteInfo[qt.MULTI]
        for q in bank.multiAnswerBank.keys():
            multi[q] = [0, 0]
            multi_note[q] = ''
        judge = self.questionInfo[qt.JUDGE]
        judge_note = self.noteInfo[qt.JUDGE]
        for q in bank.localBank[qt.JUDGE].keys():
            judge[q] = [0, 0]
            judge_note[q] = ''
        short = self.questionInfo[qt.SHORT]
        short_note = self.noteInfo[qt.SHORT]
        for q in bank.localBank[qt.SHORT].keys():
            short[q] = [0, 0]
            short_note[q] = ''

    def update(self, qType, qIndex, isCorrect):
        self.questionInfo[qType][qIndex][1] += 1  # 总次数加一
        self.questionInfo[qType][qIndex][0] += isCorrect  # 总正确次数

    def updateNote(self, qType, qIndex, content):
        self.noteInfo[qType][qIndex] = content

    def getQuestionInfo(self, qType):
        return self.questionInfo[qType]

    def getQuestionListByDiff(self, qType, diff):
        originalQuestions = self.questionInfo[qType]

        def getCorrectRate(correct, all):
            try:
                return correct / all
            except ZeroDivisionError:
                return 0
        sortedQuestions = sorted(originalQuestions.items(), key=lambda d: (getCorrectRate(d[1][0], d[1][1])))
        countPerLevel = ceil(len(originalQuestions) / 3)
        startIndex = countPerLevel * (diff - 1)
        endIndex = countPerLevel * diff
        if endIndex > len(originalQuestions):
            endIndex = len(originalQuestions)
        return [i[0] for i in sortedQuestions[startIndex: endIndex]]
