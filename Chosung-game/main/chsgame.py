import os
import time
import random
import pandas
from pandas import DataFrame


DIR_WORD_PATH = '../word/'
RANK_FILE_PATH = './rank.csv'


class player:
    def __init__(self, name: str, score=0):
        self.name = name.replace(' ', '')
        self.score = score

    def setname(self, name):
        self.name = name.replace(' ', '')

    def setscore(self, score):
        self.score += score

    def getname(self):
        return self.name

    def getscore(self):
        return self.score


def initRank():
    """make a rank file if it's not exist"""
    game_data = {'player': [], 'score': [],
                 'play time': [], 'time(sec)': []}
    if not os.path.exists(RANK_FILE_PATH):
        df = DataFrame(game_data)
        df.to_csv('rank.csv')
        return df
    df = DataFrame(game_data)
    return df


def updateRank(pl_name: str, pl_score=0, pl_time=0.0, dt=initRank(), i=0):
    dt.loc[i] = [pl_name, pl_score,
                 time.strftime('%y/%m/%d %X'), round(pl_time, 2)]
    dt.set_index(['player', 'score', 'play time', 'time(sec)'])
    dt.sort_values(['score', 'play time'])
    i += 1
    

def runGame():
    # make player name
    player_name = input('make your player name ')
    new = player(player_name)
    # start game
    cnt = 0
    while cnt < 5:
        # present initial sound from a word
        chs = random.choice(os.listdir(DIR_WORD_PATH))
        print(chs[:2])
        # check player's answer is correct
        player_say = input('the answer is? ')
        start = time.time()
        answer_list = []
        with open(DIR_WORD_PATH+chs, encoding='utf-8') as f:
            if player_say in f.read():
                end = time.time()
                new.setscore(1)
                answer_list.append(player_say)
                # whether player's answer is duplicated
                if new.getscore() == 1:
                    updateRank(new.getname(), new.getscore(), round(end-start, 2))
                else:
                    df = pandas.DataFrame(answer_list)
                    d = list(df.duplicated().iloc[:])
                    if True in d: break
                    updateRank(new.getname(), new.getscore(), round(end-start, 2))
                cnt += 1
            break

    # game clear, display rank data
    print(pandas.read_csv('rank.csv', usecols=[1, 2, 3]))


if __name__ == '__main__':
    try: runGame()
    except Exception as e:
        print(e)
