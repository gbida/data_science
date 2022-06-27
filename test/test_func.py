import os
import time
import pandas
import re
import random

DIR_WORD= '../word/'
nameList=os.listdir(DIR_WORD)

if __name__=='__main__':
    class chsgame:
        ranklist = []
        chos = [
            'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ',
            'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ',
            'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
        ]
        jungs = [
            'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ',
            'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ',
            'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
        ]
        jongs = [
            ' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ',
            'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ',
            'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
            'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
        ]

        def isHangeul(self, answer):
            if 0 < len(answer) < 3:
                if isinstance(answer, str):
                    p = re.findall("([^a-zA-Z!@ #$%^&*()=`+~?<>\"'])", answer)
                    if p is None: return False
            else:
                return False

        def getChos(self, word):
            result = ''
            for w in word:
                result += chr(((ord(w) - 44032) // 588) + 4352)
            return result

        def 게임시작(self, nickname):
            point = 0
            if nickname:
                # 초성 제시
                testfile = []
                wordfile = random.choice(nameList)
                with open(wordfile, mode='r', encoding='utf-8') as wf:
                    for line in wf.readlines():
                        testfile.append(line.replace('\n', ''))
                return random.choice(testfile)

        def 정답은(self, answer, anstime):
            point = 0
            if chsgame.getChos(answer) == chsgame.게임시작(nickname):
                point += 1
                chsgame.ranklist.append({'닉네임': nickname, '점수': point, '시간': anstime})
                print('정답입니다')
