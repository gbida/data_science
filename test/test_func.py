import time
import pandas as pd
import os
import random

# 초성 분리
def getchs(word: str) -> str:
    result = ''
    for w in word:
        result += chr(((ord(w) - 44032) // 588) + 4352)
    return result

# 게임 시작
def startchs(player: str) -> tuple:
    global score
    score = 0
    answerlist = []
    i = 0
    # 초성 랜덤 제시
    if player:
        testfile = []
        wordfile = random.choice(os.listdir('../word/'))
        with open(wordfile, mode='r', encoding='utf-8') as f:
            for line in f.readlines():
                testfile.append(line.replace('\n', ''))
        correct = random.choice(testfile)
        correct_chs = getchs(correct)
        # player 대답 저장
        # answerlist.append(chosung_input)
        if answerlist[i] == correct:
            if answerlist[i] not in answerlist:
                score += 1
                i += 1
                return correct, score

# 랭킹 확인
def highscore():
    # rank.xlsx 열기, 시간
    highscore=pd.read_excel('./rank.xlsx', engine='openpyxl', index_col=0, usecols=[0, 1, 2, 3])
    return highscore.loc[1:10]  # 10등까지만 보여주기

# 게임 종료 후 결과 저장
def save_result(player):
    data=pd.read_excel('./rank.xlsx', engine='openpyxl', index_col=0)  # 랭킹 엑셀 읽기
    player=player.replace(' ', '')  # 공백 제거
    rank_time=time.localtime()  # 현재 시간 저장
    data.loc[11]=[player, score, time.strftime("%y/%m/%d %H:%M:%S", rank_time), f'{time.time():.2f}']

    # 새로운 게임 결과를 11등 위치에 저장
    cols=['점수', '시간값']
    tups=data[cols].sort_values(by=cols, ascending=(False, True)).apply(tuple, axis=1)

    # 점수, 시간값 2가지 기준에 따라 정렬
    f, i=pd.factorize(tups)
    factorized=pd.Series(f+1, tups.index)

    # 새로운 순위를 'rank'행에 저장
    data['rank']=factorized
    data=data.sort_values(by=['rank'])  # 'rank'에 따라 정렬
    data.index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # 다시 1~10위 부여하기
    data=data.drop('rank', axis=1)  # 'rank'행 삭제
    data=data.drop(11)  # 11위 삭제
    data.to_excel('./rank.xlsx')  # rank.xlsx에 덮어쓰기