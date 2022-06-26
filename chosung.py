# 전역 변수 및 상수 --------------------------
DIR_WORD = './word/'
DIR_NAME = './name/'

import os
if not os.path.exists(DIR_WORD):    # dict 폴더 존재 여부 체크 없으면 만들기
    os.makedirs(DIR_WORD)

if not os.path.exists(DIR_NAME):    # name 폴더 존재 여부 체크 없으면 만들기
    os.makedirs(DIR_NAME)

nameList = os.listdir(DIR_NAME)     # name 폴더 안 파일들의 이름들을 리스트로 만들기

import time

import numpy as np                  # 넘파이 np로 쓸거에요 우리


# 함수 세팅 ------------------------

def print_title():      # 맨 처음 타이틀 화면
    print('=' * 30)
    print('아름다운 우리말! 훈민정음 게임!\n\n\n')
    print('로그인할 이름을 적어주세요\nx를 입력하면 게임을 종료합니다.')
    print('=' * 30)

def print_main():      # 메인 화면
    print('=' * 30)
    print('아름다운 우리말! 훈민정음 게임!\n\n\n')
    print('1. 게임 시작')
    print('2. 순위 확인')
    print('3. 게임 설명')
    print('x를 입력하면 초기 화면으로 돌아갑니다.')
    print('=' * 30)

def print_help():       # 게임 설명
    print('애옹')

def show_rank():        # 랭킹 확인
    print('순위 닉네임 점수 시간')
    print('애옹')

def save_result(name):      # 게임 결과 저장
    name = name.replace(" ", "")    # 이름의 공백 제거
    rank_time = time.localtime()  # 게임 결과 데이터 저장 시에 저장할 시간값

    filename = f'{DIR_NAME + name}.txt' # 저장할 결과값의 파일 이름
    with open(filename, mode = 'a', encoding = 'utf-8') as file:
        file.write(f'{score} {time.strftime("%y/%m/%d %H:%M:%S", rank_time)} {time.time()}\n')
        # 점수 저장, 보기 좋게 시간 표시 양식을 바꿔서 저장, 하나는 시간 비교용으로 원본값 저장



score = 20

save_result("오우영")



# 게임 구현 ------------------------
print('게임이 시작되었습니다.')

while True:
    print_title()
    name = input("닉네임 : ") # 닉네임 미리 저장

    if name != 'x' and name != 'X':     # x말고 다른거 누르면 다음 화면으로 넘어갈거야
        while True:
            print_main()
            select = input("메뉴 선택 : ")

            if select == '1': # 게임 시작
                pass

            elif select == '2': # 랭킹 확인
                show_rank()

            elif select == '3': print_help() # 게임 설명

            elif select == 'x' or select == 'X': break # x 누르면 초기화면으로 돌아갈거야

            else: print('잘못된 접근입니다.')

    elif name == 'x' or name == 'X': break # 게임 종료
