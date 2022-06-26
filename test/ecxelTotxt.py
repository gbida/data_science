# 모듈
import pandas
import os
import re

# 폴더
ori='./dic/'                    # 처리할 엑셀파일 위치
txt_dir='./word/'               # 최종 txt 파일 저장 폴더
if not os.path.exists(txt_dir): os.mkdir(txt_dir)

# 함수 정의

# 엑셀 처리후 txt로 변환
def ETT(excel):
    if not os.path.exists(txt_dir+'ETT/'): os.mkdir(txt_dir+'ETT/')
    data=pandas.read_excel(ori+excel)
    row=data.iloc[:,:3]
    col=row[((row['구성 단위']=='단어') & (row['고유어 여부']=='고유어')) | ((row['구성 단위']=='단어') & (row['고유어 여부']=='한자어'))]
    col=col.rename(columns={'어휘':'가'})
    txt=col.iloc[:,:1]
    txt.to_csv(txt_dir+'ETT/'+excel[:-5]+'.txt', index=0)

# 한글 제외한 모든 문자 제거
def clean_txt(txt_file):
    if not os.path.exists(txt_dir+'clean_txt'): os.mkdir(txt_dir+'clean_txt')
    with open(txt_dir+'ETT/'+txt_file, mode='r',encoding='utf-8') as txt:
        with open(txt_dir+'clean_txt/'+txt_file, mode='w', encoding='utf-8') as txt2:
            while True:
                word=txt.readline()
                word=re.sub('[^가-힣]', '', word)
                txt2.write(word+'\n')
                if not word: break

# 2글자 아닌 단어 제거
def wordTwo(txt_file):
    if not os.path.exists(txt_dir+'wordTwo'): os.mkdir(txt_dir+'wordTwo')
    with open(txt_dir+'clean_txt/'+txt_file, mode='r',encoding='utf-8') as txt:
        with open(txt_dir+'wordTwo/'+txt_file, mode='w',encoding='utf-8') as txt2:
            while True:
                word=txt.readline()
                if len(word)==3:
                    txt2.write(word)
                elif not word:
                    break
                else: pass

# 중복제거
def set_txt(txt_file):
    if not os.path.exists(txt_dir+'set_txt'): os.mkdir(txt_dir+'set_txt')
    with open(txt_dir+'wordTwo/'+txt_file, mode='r', encoding='utf-8') as txt:
        with open(txt_dir+'set_txt/'+txt_file, mode='w', encoding='utf-8') as txt2:
            txtList = list(set(txt.readlines()))
            txtList.sort()
            for i in txtList: txt2.write(i)

# 초성 판별 후 ㄱㄱ~ㅎㅎ.txt에 각각 저장
def chosung(txt_file):
    chosungList = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    with open(txt_dir+'set_txt/'+txt_file, mode='r', encoding='utf-8') as txt:
        while True:
            word=txt.readline().strip()
            chosung1=''
            if not word: break
            else:
                for i in list(word):
                    code=((ord(i)-ord('가'))//588)
                    chosung1+=chosungList[code]
                with open(txt_dir+chosung1+'.txt',mode='a',encoding='utf-8') as txt2:
                    txt2.write(word+'\n')

# 기능 구현
excelList=os.listdir(ori)
for i in excelList:
    ETT(i)
    i=i[:-5]+'.txt'
    clean_txt(i)
    wordTwo(i)
    set_txt(i)
    chosung(i)



# 필요없는 파일,폴더 삭제
reList=os.listdir(txt_dir)
dirlist=[]
for i in reList:
    if not '.txt' in i:
        dirlist+=[i]
for i in dirlist:
    for j in os.listdir(txt_dir+i):
        os.remove(txt_dir+i+'/'+j)
    os.rmdir(txt_dir+i)