# 전역 변수 및 상수 --------------------------
import time
import numpy as np                  # 넘파이 np로 쓸거에요 우리
import pandas as pd                 # 판다스는 pd로 쓸거에요 우리
import openpyxl
import os

DIR_WORD = '../word/'

# 함수 세팅 ------------------------
def highscore():        # 랭킹 확인
    highscore = pd.read_excel('../rank.xlsx', engine='openpyxl', index_col=0, usecols=[0, 1, 2, 3])
    # rank.xlsx 열기, 시간까지만 보여주기
    highscore = highscore.loc[1:10]     # 10등까지만 보여주기
    print(highscore)

def save_result(player): # 게임 종료 후 결과 저장
    data = pd.read_excel('../rank.xlsx', engine='openpyxl', index_col=0) # 랭킹 엑셀 읽기
    player = player.replace(' ','') # 공백 제거
    rank_time = time.localtime()    # 현재 시간 저장
    data.loc[11] = [player, point, time.strftime("%y/%m/%d %H:%M:%S", rank_time), f'{time.time():.2f}']
    # 새로운 게임 결과를 11등 위치에 저장

    cols = ['점수', '시간값']
    tups = data[cols].sort_values(by= cols, ascending=(False, True)).apply(tuple, axis=1)
    # 점수, 시간값 2가지 기준에 따라 정렬
    f, i = pd.factorize(tups)
    factorized = pd.Series(f+1, tups.index)

    data['rank'] = factorized  #새로운 순위를 'rank'행에 저장
    data = data.sort_values(by=['rank']) # 'rank'에 따라 정렬
    data.index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]    # 다시 1~10위 부여하기
    data = data.drop('rank', axis=1)    # 'rank'행 삭제
    data = data.drop(11)                # 11위 삭제
    data.to_excel('../rank.xlsx')       # rank.xlsx에 덮어쓰기

# point는 몇 개 맞췄는지 저장
# point = 20              # 테스트용 점수
# player = '리오니'        # 테스트용 닉네임
#
# save_result(player)     # 테스트용 함수

