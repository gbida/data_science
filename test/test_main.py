import os
import time
import pandas
import re
import random


ori='./dic/'
DIR_WORD= '../word/'
DIR_NAME= '../name/'
nameList=os.listdir(DIR_NAME)

if not os.path.exists(DIR_WORD):
    os.makedirs(DIR_WORD)

if not os.path.exists(DIR_NAME):
    os.makedirs(DIR_NAME)

if not os.path.exists(DIR_NAME):
    os.makedirs(DIR_NAME)

if not os.path.exists(DIR_WORD):
    os.makedirs(DIR_WORD)


class ChosungGame:
    chos=[
        'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ',
        'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ',
        'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
    ]
    jungs=[
        'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ',
        'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ',
        'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
    ]
    jongs=[
        ' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ',
        'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ',
        'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
        'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
    ]


    def ETT(self, excel):
        if not os.path.exists(DIR_WORD+'ETT/'): os.mkdir(DIR_WORD + 'ETT/')
        data=pandas.read_excel(ori+excel+'.xlsx')
        row=data.iloc[:,:3]
        col=row[((row['구성 단위']=='단어') & (row['고유어 여부']=='고유어')) | ((row['구성 단위']=='단어') & (row['고유어 여부']=='한자어'))]
        col=col.rename(columns={'어휘':'가'})
        txt=col.iloc[:,:1]
        txt.to_csv(DIR_WORD+'ETT/'+excel+'.txt', index=0)

    def clean_txt(self, txt_file):
        if not os.path.exists(DIR_WORD+'clean_txt'): os.mkdir(DIR_WORD+'clean_txt')
        with open(DIR_WORD+'ETT/'+txt_file+'.txt', mode='r', encoding='utf-8') as txt:
            with open(DIR_WORD+'clean_txt/' + txt_file + '.txt', mode='w', encoding='utf-8') as txt2:
                while True:
                    word=txt.readline()
                    word=re.sub('[^가-힣]', '', word)
                    txt2.write(word+'\n')
                    if not word: break

    def wordTwo(self, txt_file):
        if not os.path.exists(DIR_WORD+'wordTwo'): os.mkdir(DIR_WORD+'wordTwo')
        with open(DIR_WORD+'clean_txt/'+txt_file+'.txt', mode='r', encoding='utf-8') as txt:
            with open(DIR_WORD+'wordTwo/'+txt_file+'.txt', mode='w', encoding='utf-8') as txt2:
                while True:
                    word=txt.readline()
                    if len(word)==3:
                        txt2.write(word)
                    elif not word:
                        break
                    else: pass

    def set_txt(self, txt_file):
        if not os.path.exists(DIR_WORD+'set_txt'): os.mkdir(DIR_WORD+'set_txt')
        with open(DIR_WORD+'wordTwo/'+txt_file+'.txt', mode='r', encoding='utf-8') as txt:
            with open(DIR_WORD+'set_txt/'+txt_file+'.txt', mode='w', encoding='utf-8') as txt2:
                txtList=list(set(txt.readlines()))
                txtList.sort()
                for i in txtList: txt2.write(i)

    def chosung(self, txt_file):
        chosungList=['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
        with open(DIR_WORD+'set_txt/'+txt_file+'.txt', mode='r', encoding='utf-8') as txt:
            while True:
                word=txt.readline().strip()
                chosung1=''
                if not word: break
                else:
                    for i in list(word):
                        code=((ord(i)-ord('가'))//588)
                        chosung1 += chosungList[code]
                    with open(DIR_WORD+chosung1+'.txt', mode='a', encoding='utf-8') as txt2:
                        txt2.write(word+'\n')

    def print_title(self):
        print('=' * 30)
        print('아름다운 우리말! 훈민정음 게임!\n\n\n')
        print('로그인할 이름을 적어주세요\nx를 입력하면 게임을 종료합니다.')
        print('=' * 30)

    def print_main(self):
        print('=' * 30)
        print('아름다운 우리말! 훈민정음 게임!\n\n\n')
        print('1. 게임 시작')
        print('2. 순위 확인')
        print('3. 도움말')
        print('x를 입력하면 초기 화면으로 돌아갑니다.')
        print('=' * 30)

    def save_result(self, name):
        name=name.replace(" ", "")
        rank_time=time.localtime()

        filename=f'{DIR_NAME + name}.txt'
        with open(filename, mode='a', encoding='utf-8') as file:
            file.write(f'{time.strftime("%y/%m/%d %H:%M:%S", rank_time)} {time.time()}\n')

    def isHangeul(self, answer: str) -> bool:
        if 0 < len(answer) < 3:
            if isinstance(answer, str):
                p=re.findall("([^a-zA-Z!@ #$%^&*()=`+~?<>\"'])", answer)
                if p is None: return False
        else: return False

    def getChos(self, word: str) -> str:
        result=''
        for w in word:
            result += chr(((ord(w) - 44032) // 588)+4352)
        return result

    def 랭킹현황(self):
        rank=0
        nickname, point, anstime
        pass

    def 퀴즈풀러가기(self):
        def 게임설명():
            pass

        def 게임시작():
            global nickname, point, anstime
            nickname=input('닉네임을 입력해주세요')
            point=0
            if nickname:
                # 초성 제시
                testfile=[]
                wordfile=random.choice(nameList)
                with open(wordfile, mode='r', encoding='utf-8') as wf:
                    for line in wf.readlines():
                        testfile.append(line.replace('\n', ''))
                correct=random.choice(testfile)
                print('게임 단어', correct)

                # 사용자 입력과 입력시간 기록
                answer=input('단어는 무엇일까요?')
                anstime=time.strftime('%x %X')

                if ChosungGame.getChos(answer)==correct:
                    point += 1
                    print('정답입니다')
                else:
                    print('다시 해볼까요?')
                    goto=input('게임설명 | 게임시작 | 종료')
                    if goto=='게임설명':
                        게임설명()
                    elif goto=='게임시작':
                        게임시작()
                    elif goto=='종료':
                        exit(0)

        goto=input('게임설명 | 게임시작 | 종료')
        if goto=='게임설명':
            게임설명()
        elif goto=='게임시작':
            게임시작()
        elif goto=='종료': exit(0)


if __name__=='__main__':
    for i in range(1, 16):
        i=str(i)
        ChosungGame.ETT(i)
        ChosungGame.clean_txt(i)
        ChosungGame.wordTwo(i)
        ChosungGame.set_txt(i)
        ChosungGame.chosung(i)

    redir=['ETT/', 'clean_txt/', 'wordTwo/', 'set_txt/']
    for i in redir:
        for j in range(1, 16):
            j=str(j)
            os.remove(DIR_WORD+i+j+'.txt')
        os.rmdir(DIR_WORD+i)

    while True:
        goto = input('랭킹보기 | 퀴즈풀러가기 | 종료')
        if goto == '종료':
            break
        elif goto == '랭킹보기':
            ChosungGame.랭킹현황()
        elif goto == '퀴즈풀러가기':
            ChosungGame.퀴즈풀러가기()
        else:
            break