import time
import pandas as pd
import os
import openpyxl
import random


DIR_WORD_PATH = '../dic/word/'
DIRC_EXCEL = './rank.xlsx'

player1 = None
player2 = None


# 플레이어 데이터 저장
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

# 플레이어 생성
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

# 랜덤 단어에서 초성 분리
def getchosung(word):
    """Return chosung as a string from a two letters word"""
    if isinstance(word, str):
        chosung = ''
        for w in word:
            chosung += chr(((ord(w) - 44032) // 588) + 4352)
        return chosung

# 플레이어한테 초성 제시
def givechosung():
    """Return two letters chosung as a string"""
    randomfile = random.choice(os.listdir(DIR_WORD_PATH))  # ㄷㅇ.txt
    return randomfile

# 랭킹 확인
def highscore():
    # rank.xlsx 열기, 시간
    highscore=pd.read_excel(DIRC_EXCEL, engine='openpyxl', index_col=0, usecols=[0, 1, 2, 3])
    return highscore.loc[1:10]  # 10등까지만 보여주기

# 게임 종료 후 결과 저장
def save_result(player):

    if not os.path.exists(DIRC_EXCEL):  # rank.xlsx 없으면 랭킹에 쓸 기본 양식을 만들래
        df = pd.DataFrame({'이름':{0:"-", 1:"-", 2:"-", 3:"-", 4:"-", 5:"-", 6:"-", 7:"-", 8:"-", 9:"-"},
                           '점수':{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
                           '시간':{0:"-", 1:"-", 2:"-", 3:"-", 4:"-", 5:"-", 6:"-", 7:"-", 8:"-", 9:"-"},
                           '시간값':{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}})
        filename = 'rank.xlsx'
        df.to_excel(filename) # rank.xlsx 생성

    else:
        data=pd.read_excel(DIRC_EXCEL, engine='openpyxl', index_col=0)  # 랭킹 엑셀 읽기
        player=player.replace(' ', '')  # 공백 제거
        rank_time=time.localtime()  # 현재 시간 저장
        data.loc[11]=[player, player.getscore(), time.strftime("%y/%m/%d %H:%M:%S", rank_time), f'{time.time():.2f}']
        print(data)

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
        print(data)
        data.to_excel(DIRC_EXCEL)  # rank.xlsx에 덮어쓰기


if __name__ == '__main__':
    a = setplayer('user01')
    while True:
        print(givechosung()[:2])
        player_say = input('대답')
        try:
            with open(DIR_WORD_PATH+givechosung(), encoding='utf-8') as f:
                if player_say+'\n' in f.readlines():
                    a.setscore(1)
                    print('정답')
                    print(a.getscore())
                else:
                    print('오답')
                    print(a.getscore())
                    break
        except Exception as e:
            print(e)
            break
