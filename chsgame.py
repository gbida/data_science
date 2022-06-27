import os
import random


class chsgame:
    # 초성, 중성, 종성 리스트
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

    # 초성 분리
    def getchos(self, word: str) -> str:
        result = ''
        for w in word:
            result += chr(((ord(w) - 44032) // 588) + 4352)
        return result

    # 게임 시작
    def startgame(self, player: str) -> tuple:
        score = 0
        player_say = []
        i = 0
        # 초성 랜덤 제시
        if player:
            testfile = []
            wordfile = random.choice(os.listdir('../word/'))
            with open(wordfile, mode='r', encoding='utf-8') as wf:
                for line in wf.readlines():
                    testfile.append(line.replace('\n', ''))
            correct = random.choice(testfile)
            # 정답이면 score+1
            if player_say[i] == correct:
                if player_say[i] not in player_say:
                    score += 1
                    i += 1
                    return (correct, score)