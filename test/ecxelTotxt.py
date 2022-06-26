# 모듈
import pandas
import os
import re

# 폴더
ori='./dic/'             # 처리할 엑셀파일 위치
p='./word/'              # 최종 txt 파일 저장 폴더
if not os.path.exists(p): os.makedirs(p)

# 함수 정의

# 엑셀 처리후 txt로 변환
def ETT(excel):
    if not os.path.exists(p+'ETT/'): os.mkdir(p + 'ETT/')
    data=pandas.read_excel(ori+excel+'.xlsx')
    row=data.iloc[:,:3]
    col=row[((row['구성 단위']=='단어') & (row['고유어 여부']=='고유어')) | ((row['구성 단위']=='단어') & (row['고유어 여부']=='한자어'))]
    col=col.rename(columns={'어휘':'가'})
    txt=col.iloc[:,:1]
    txt.to_csv(p+'ETT/'+excel+'.txt', index=0)

# 한글 제외한 모든 문자 제거
def clean_txt(txt_file):
    if not os.path.exists(p+'clean_txt'): os.mkdir(p+'clean_txt')
    with open(p+'ETT/'+txt_file+'.txt', mode='r',encoding='utf-8') as txt:
        with open(p+'clean_txt/' + txt_file + '.txt', mode='w', encoding='utf-8') as txt2:
            while True:
                word=txt.readline()
                word=re.sub('[^가-힣]', '', word)
                txt2.write(word+'\n')
                if not word: break

# 2글자 아닌 단어 제거
def wordTwo(txt_file):
    if not os.path.exists(p+'wordTwo'): os.mkdir(p+'wordTwo')
    with open(p+'clean_txt/'+txt_file+'.txt', mode='r',encoding='utf-8') as txt:
        with open(p+'wordTwo/'+txt_file+'.txt', mode='w',encoding='utf-8') as txt2:
            while True:
                word=txt.readline()
                if len(word)==3:
                    txt2.write(word)
                elif not word:
                    break
                else: pass

# 중복제거
def set_txt(txt_file):
    if not os.path.exists(p+'set_txt'): os.mkdir(p+'set_txt')
    with open(p+'wordTwo/'+txt_file+'.txt', mode='r', encoding='utf-8') as txt:
        with open(p+'set_txt/'+txt_file+'.txt', mode='w', encoding='utf-8') as txt2:
            txtList = list(set(txt.readlines()))
            txtList.sort()
            for i in txtList: txt2.write(i)

# 초성 판별 후 ㄱㄱ~ㅎㅎ.txt에 각각 저장
def chosung(txt_file):
    chosungList = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    with open(p+'set_txt/'+txt_file+'.txt', mode='r', encoding='utf-8') as txt:
        while True:
            word=txt.readline().strip()
            chosung1=''
            if not word: break
            else:
                for i in list(word):
                    code=((ord(i)-ord('가'))//588)
                    chosung1+=chosungList[code]
                with open(p+chosung1+'.txt',mode='a',encoding='utf-8') as txt2:
                    txt2.write(word+'\n')

# 기능 구현
for i in range(1,16):
    i=str(i)
    ETT(i)
    clean_txt(i)
    wordTwo(i)
    set_txt(i)
    chosung(i)

# 필요없는 파일,폴더 삭제
redir=['ETT/','clean_txt/','wordTwo/','set_txt/']
for i in redir:
    for j in range(1,16):
        j=str(j)
        os.remove(p+i+j+'.txt')
    os.rmdir(p+i)