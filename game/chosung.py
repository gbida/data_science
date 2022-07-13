import pandas
import os


hangeulDF = pandas.DataFrame({
    '초성': ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ',
           'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
           'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ',
           'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
})


# 단어의 초성 인덱스 번호 찾기
def index(word):
    word_idx = []
    for w in word:
        if '가' <= w <= '힣':
            cho_idx = (ord(w)-44032)//588
            word_idx.extend([cho_idx])
    return word_idx


# play time이 적은 것을 기준으로 10위까지의 랭킹 기록
def updateRank(id, score, playtime):
    if not os.path.exists('./rank.csv'):
        rank = pandas.DataFrame({'id': id,
                                 'score': score,
                                 'play time': playtime},
                                index=['id'])
        rank.to_csv('./rank.csv')
    else:
        rank = pandas.read_csv('./rank.csv')
        pl_new = pandas.DataFrame({'id': id,
                                'score': score,
                                'play time': playtime},
                               index=['id'])
        rank_new = pandas.concat([rank, pl_new], names='chosung game rank')
        rank_new.sort_values(by=['play time'], inplace=True)
        if rank_new.shape[0] == 10:
            rank_new = rank_new.iloc[:10, :]
        rank_new.to_csv('./rank.csv')
