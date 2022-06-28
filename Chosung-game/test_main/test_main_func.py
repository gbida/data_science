import os
import time
import pandas as pd
import random
import openpyxl


DIR_WORD_PATH = '../dic/word/'
FILE_EXCEL_PATH = './rank.xlsx'


player1 = None
player2 = None


# set a data frame for players
class player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    # set instance values of player
    def setname(self, name):
        self.name = name
        return self.name

    def setscore(self, score):
        self.score += score
        return self.score

    # get instance values of player
    def getname(self):
        return self.name

    def getscore(self):
        return self.score


# takes players info
def setplayer(name):
    """Return player1 as a player class type object if new,
     otherwise player2 as a same object for existing users"""
    global player1, player2
    if player1 is None:
        player1 = player(name)
        return player1
    else:
        player2 = player(name)
        return player2


# seperate chosung from a random word
def getchosung(word):
    """Return chosung as a string from a two letters word"""
    if isinstance(word, str):
        chosung = ''
        for w in word:
            chosung += chr(((ord(w) - 44032) // 588) + 4352)
        return chosung


# to show chosung to player
def givechosung():
    """Return two letters word and its chosung as a tuple """
    pickword = []  # 'ㄷㅇ.txt'
    randomfile = random.choice(os.listdir(DIR_WORD_PATH))
    with open(randomfile, encoding='utf-8') as f:
        for line in f.readlines():
            pickword.append(line.replace('\n', ''))
    correct = random.choice(pickword)  # '단어'
    correct_chs = getchosung(correct)  # 'ㄷㅇ'
    return correct, correct_chs


# 랭킹 확인
def highscore():
    # rank.xlsx 열기, 시간
    highscore=pd.read_excel(FILE_EXCEL_PATH, engine='openpyxl', index_col=0, usecols=[0, 1, 2, 3])
    return highscore.loc[1:10]  # 10등까지만 보여주기


# 게임 종료 후 결과 저장
def save_result(player):
    data=pd.read_excel(FILE_EXCEL_PATH, engine='openpyxl', index_col=0)  # 랭킹 엑셀 읽기
    player=player.replace(' ', '')  # 공백 제거
    rank_time=time.localtime()  # 현재 시간 저장
    data.loc[11]=[player, setplayer(name).getscore(), time.strftime("%y/%m/%d %H:%M:%S", rank_time), f'{time.time():.2f}']

    # 새로운 게임 결과를 11등 위치에 저장
    cols=['점수', '시간값']
    tups=data[cols].sort_values(by=cols, ascending=(False, False)).apply(tuple, axis=1)

    # 점수, 시간값 2가지 기준에 따라 정렬
    f, i=pd.factorize(tups)
    factorized=pd.Series(f+1, tups.index)

    # 새로운 순위를 'rank'행에 저장
    data['rank']=factorized
    data=data.sort_values(by=['rank'])  # 'rank'에 따라 정렬
    data.index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # 다시 1~10위 부여하기
    data=data.drop('rank', axis=1)  # 'rank'행 삭제
    data=data.drop(11)  # 11위 삭제
    data.to_excel(FILE_EXCEL_PATH)  # rank.xlsx에 덮어쓰기


if __name__ == '__main__':
    name = input('create a player name')
    setplayer(name)

    print(givechosung()[1])
    player_say = input('say answer')

    while True:
        try:
            if player_say == givechosung()[0]:
                setplayer(name).setscore(1)
            else: print(givechosung()[1])
        except Exception as e:
            print(e)
            break
