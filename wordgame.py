import time
import re
import numpy


class 게임:
    #초성 리스트=map(chr, list(range(4352, 4371)))
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

    #입력값이 공백, 영어, 특수문자가 없는 한글인지 확인
    def 사용자입력(단어: str) -> bool:
        if 0 < len(단어) < 3:
            if isinstance(단어, str):
                p=re.findall("([^a-zA-Z!@ #$%^&*()+=`~?<>\"'])", 단어)
                if p is None: return False
        else: return False

    def 초성추출(단어: str) -> str:
        '''
        초성 시작 인덱스 = 4352
        자음모음 시작 인덱스 = 44032
        자음모음 종료 인덱스 = 55203
        자음모음 회전 = 588
        '''
        if 게임.사용자입력(단어):
            result=''
            for 입력값 in 단어:
                result+=chr(((ord(입력값)-44032)//588)+4352)
            return result

    #@초성추출2
    #def 게임랭킹():


if __name__=='__main__':

    #hangul_syllables=numpy.array([chr(code) for code in range(44032, 55204)])
    #hangul_syllables=hangul_syllables.reshape(19, 21, 28)

    라운드=5
    시작시간=time.strftime('%x %X')

    #게임 설명 화면

    #게임 시작 동의 -> 사용자 프로필 입력
    #사용자 프로필() + 1라운드 START 22/06/26 00:00:00

    #while 사용자 프로필 입력값 있을때:
    #가나다 제시
    #try:
    #  게임.초성추출2(사용자입력값)
    #  랭킹 표시 + 종료시간
    #
    #except: 사용자입력값에서 오류 생겼을 경우 처리
    #finally: