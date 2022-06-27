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

if not os.path.exists(DIR_WORD+'ETT/'):
    os.mkdir(DIR_WORD+'ETT/')


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
                p=re.findall("([^a-zA-Z!@ #$%^&*()=`+~?<>\"'])", answer)
                if p is None: return False
        else: return False

    def getChos(self, word):
        result=''
        for w in word:
            result += chr(((ord(w) - 44032) // 588)+4352)
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

def ETT(excel):
    data=pandas.read_excel(ori+excel+'.xlsx')
    row=data.iloc[:,:3]
    col=row[((row['구성 단위']=='단어') & (row['고유어 여부']=='고유어')) | ((row['구성 단위']=='단어') & (row['고유어 여부']=='한자어'))]
    col=col.rename(columns={'어휘':'가'})
    txt=col.iloc[:,:1]
    txt.to_csv(DIR_WORD+'ETT/'+excel+'.txt', index=0)

def clean_txt(txt_file):
    if not os.path.exists(DIR_WORD+'clean_txt'): os.mkdir(DIR_WORD+'clean_txt')
    with open(DIR_WORD+'ETT/'+txt_file+'.txt', mode='r', encoding='utf-8') as txt:
        with open(DIR_WORD+'clean_txt/' + txt_file + '.txt', mode='w', encoding='utf-8') as txt2:
            while True:
                word=txt.readline()
                word=re.sub('[^가-힣]', '', word)
                txt2.write(word+'\n')
                if not word: break

def wordTwo(txt_file):
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

def set_txt(txt_file):
    if not os.path.exists(DIR_WORD+'set_txt'): os.mkdir(DIR_WORD+'set_txt')
    with open(DIR_WORD+'wordTwo/'+txt_file+'.txt', mode='r', encoding='utf-8') as txt:
        with open(DIR_WORD+'set_txt/'+txt_file+'.txt', mode='w', encoding='utf-8') as txt2:
            txtList=list(set(txt.readlines()))
            txtList.sort()
            for i in txtList: txt2.write(i)

def chosung(txt_file):
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


if __name__=='__main__':
    for i in range(1, 16):
        i=str(i)
        ETT(i)
        clean_txt(i)
        wordTwo(i)
        set_txt(i)
        chosung(i)

    redir=['ETT/', 'clean_txt/', 'wordTwo/', 'set_txt/']
    for i in redir:
        for j in range(1, 16):
            j=str(j)
            os.remove(DIR_WORD+i+j+'.txt')
        os.rmdir(DIR_WORD+i)

    # 게임시작 -> 초성제시
    nickname = input('닉네임')
    chsgame.게임시작(nickname)

    # 사용자 입력, 입력시간 기록
    answer = input('정답은?')
    anstime = time.strftime('%x %X')
    print(chsgame.정답은(answer, anstime))

    # 랭킹보기
    rank=pandas.DataFrame(chsgame.ranklist)
    rank.sort_values(anstime)
    print(rank)
