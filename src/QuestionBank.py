import json
import os

from QuestionType import qType as qt


class QBank:
    def __init__(self):
        self.localBank = {qt.MULTI: {}, qt.JUDGE: {}, qt.SHORT: {}}
        f = open('./resource/questions/QuestionBankMulti.json', encoding='utf-8')
        self.localBank[qt.MULTI] = json.load(f)
        f = open('./resource/questions/AnswerBankMulti.json', encoding='utf-8')
        self.multiAnswerBank = json.load(f)
        f = open('./resource/questions/QuestionBankJudge.json', encoding='utf-8')
        self.localBank[qt.JUDGE] = json.load(f)
        f = open('./resource/questions/QuestionBankShort.json', encoding='utf-8')
        self.localBank[qt.SHORT] = json.load(f)


bank = QBank()
