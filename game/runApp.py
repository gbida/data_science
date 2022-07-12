import time
import pandas
import chosung


def runApp():
    # create player id and clocking a play time
    id = input('id for chosung game ')
    play_start = time.time()

    # 5round for game
    answer_list = []
    for n in range(5):
        word = '단어'
        one = chosung.index(word)[0]
        two = chosung.index(word)[1]
        print(chosung.hangeulDF['초성'][one]
              + chosung.hangeulDF['초성'][two])

        answer = input('무슨 단어일까요? ')
        if answer == word:
            answer_list.append(answer)
        else: break
    play_exit = time.time()
    play_time = round(play_exit-play_start, 2)
    chosung.updateRank(id, score=5, playtime=play_time)

    # show up rank list
    pandas.read_csv('../rank.csv')


if __name__ == '__main__':
    try: runApp()
    except Exception as e:
        print(e)
        exit(0)