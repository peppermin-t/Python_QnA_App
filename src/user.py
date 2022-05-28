import pickle

from QuestionType import qType as qt
from QuestionBank import bank
from AnswerInfo import AnswerInfo


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.answerInfo = AnswerInfo()

    def saveNote(self, qType, qIndex, content):
        self.answerInfo.updateNote(qType, qIndex, content)
        with open(f'./resource/usrInfos/usr_{self.name}.pkl', 'wb') as f:
            pickle.dump(self, f)

    def answer(self, qType, qIndex, answer=None, first_hand=True):
        userAnswer = answer
        if qType == qt.MULTI:
            stdAnswer = bank.multiAnswerBank[qIndex]
            boolean = (stdAnswer == userAnswer)
        elif qType == qt.JUDGE:
            stdAnswer = bank.localBank[qt.JUDGE][qIndex]
            boolean = (stdAnswer == userAnswer)
        else:  # SHORT
            boolean = first_hand

        self.answerInfo.update(qType, qIndex, boolean)
        with open(f'./resource/usrInfos/usr_{self.name}.pkl', 'wb') as f:
            pickle.dump(self, f)
        return boolean
