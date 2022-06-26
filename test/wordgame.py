import os
import time
import re
import random


초성=(
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ',
    'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ',
    'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
)
중성=(
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ',
    'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ',
    'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
)
종성=(
    ' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ',
    'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ',
    'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
    'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
)

#공백, 영어, 특수문자 제거
def ishangeul(answer: str) -> bool:
    if 0 < len(answer) < 3:
        if isinstance(answer, str):
            p=re.findall("([^a-zA-Z!@ #$%^&*()+=`~?<>\"'])", answer)
            if p is None: return False
    else: return False

#사용자 입력값에서 초성 추출
def getChos(word: str) -> str:
    result=''
    for w in word:
        result+=chr(((ord(w)-44032)//588)+4352)
    return result


# 랭킹 보기
def 랭킹현황():
    rank = 0
    nickname, point, anstime
    # 사용자별 점수, 시간 저장할 데이터 공간 필요


# 초성 게임 진입
def 퀴즈풀러가기():
    def 게임설명():
        pass

    def 게임시작():
        global nickname, point, anstime
        nickname = input('닉네임을 입력해주세요')
        point = 0
        if nickname:
            # 초성 제시
            testfile = []
            wordfile = random.choice(os.listdir('../word/'))
            with open(wordfile, mode='r', encoding='utf-8') as wf:
                for line in wf.readlines():
                    testfile.append(line.replace('\n', ''))
            correct = random.choice(testfile)
            print('게임 단어', correct)

            # 사용자 입력과 입력시간 기록
            answer = input('단어는 무엇일까요?')
            anstime = time.strftime('%x %X')

            if getChos(answer) == correct:
                point += 1
                print('정답입니다')
            else:
                print('다시 해볼까요?')
                goto = input('게임설명 | 게임시작 | 종료')
                if goto == '게임설명':
                    게임설명()
                elif goto == '게임시작':
                    게임시작()
                elif goto == '종료':
                    exit(0)

    goto = input('게임설명 | 게임시작 | 종료')
    if goto == '게임설명':
        게임설명()
    elif goto == '게임시작':
        게임시작()
    elif goto == '종료':
        exit(0)
