from tkinter import *
import tkinter.font
import tkinter.ttk
import pandas
import time


# 메인 UI
w = Tk()
w.title("초성 Quiz!")
w.geometry("400x297")


# 메인 이미지 넣기
photo = PhotoImage(file="../image/example2.png")
pLabel = Label(w, image=photo)
pLabel.pack(expand=1, anchor=N)


# 랭킹페이지 새창 생성
def create_rank_page():
    data = pandas.read_excel('./test_main_rank.xlsx')
    row = data.iloc[:, :4]
    row.to_csv('rank.txt', index=0)
    newWindow = Toplevel(w)
    newWindow.title('랭킹현황')
    newWindow.geometry("250x217")
    rank = Label(newWindow, text='순위', fg='blue')
    rank.place(x=19, y=10)
    name = Label(newWindow, text='닉네임', fg='red')
    name.place(x=70, y=10)
    score = Label(newWindow, text='점수', fg='purple')
    score.place(x=130, y=10)
    time = Label(newWindow, text='시간', fg='green')
    time.place(x=183, y=10)
    listbox1 = Listbox(newWindow, width=6, height=10)
    listbox1.place(x=10, y=40)
    listbox2 = Listbox(newWindow, width=10, height=10)
    listbox2.place(x=54, y=40)
    listbox3 = Listbox(newWindow, width=5, height=10)
    listbox3.place(x=126, y=40)
    listbox4 = Listbox(newWindow, width=11, height=10)
    listbox4.place(x=160, y=40)
    with open(r'./rank.txt', mode='r', encoding='utf-8') as rank_txt:
        for i in range(1, 11):
            txt = str(rank_txt.readlines(i))
            txt = txt.split(',')
            time = txt[3].split('-')[1] + txt[3].split('-')[2][:8]
            listbox1.insert(i, '    ' + txt[0][2:])
            listbox2.insert(i, '   ' + txt[1])
            listbox3.insert(i, '  ' + txt[2])
            listbox4.insert(i, '  ' + time)


# 게임 설명 페이지
def create_how_page():
    newWindow = Toplevel(w)
    newWindow.title('게임 설명')
    newWindow.geometry("500x500")
    page = PhotoImage(file='../image/guide.png')
    page_label = tkinter.Label(newWindow, image=page)
    page_label.place(x=0, y=0)
    w.mainloop()


# 게임 페이지 새창 생성
def create_game_page():
    newWindow = Toplevel(w)
    newWindow.title('초성 Quiz!')
    newWindow.geometry("400x297")
    # 타이머(프로그래스바)

    def timer():
        how_btn['state'] = 'disabled'
        start_btn['state'] = 'disabled'
        j = 0
        for i in range(300):
            j += 1
            curr_progress.set(i)
            progress_bar.update()
            time.sleep(0.01)
            if j == 300:
                font = tkinter.font.Font(size=45, weight='bold')
                timeout = Label(newWindow, text='시간초과!', fg='red', font=font)
                chosung_input['state'] = 'disabled'
                timeout.place(x=70, y=70)
                break

    # 버튼들
    how_btn = Button(newWindow, text='게임설명', height=3, width=17, command=create_how_page)
    how_btn.place(x=1, y=240)
    start_btn = Button(newWindow, text='게임시작!', height=3, width=17, command=timer)
    start_btn.place(x=135, y=240)
    exit_btn2 = Button(newWindow, text='종   료', height=3, width=17, command=newWindow.destroy)
    exit_btn2.place(x=270, y=240)

    # 초성 표시 부분
    chosung1 = Label(newWindow, height=4, width=10, anchor='center', relief='ridge', borderwidth=5)
    chosung1.place(x=110, y=70)
    chosung2 = Label(newWindow, height=4, width=10, anchor='center', relief='ridge', borderwidth=5)
    chosung2.place(x=200, y=70)

    # 남은시간 타이머
    curr_progress = tkinter.DoubleVar()
    progress_bar = tkinter.ttk.Progressbar(newWindow, length=190, maximum=300, variable=curr_progress)
    progress_bar.place(x=100, y=155)

    # 초성 입력 부분
    font = tkinter.font.Font(size=20)
    chosung_input = Entry(newWindow, width=12, font=font, justify='center')
    chosung_input.place(x=98, y=190)

    # 라운드 수 표시
    font2 = tkinter.font.Font(size=15, weight='bold')
    round = Label(newWindow, text='라운드 : ', width=12, font=font2, justify='center')
    count = Label(newWindow, text='정답수 : ', width=12, font=font2, justify='center')
    round.place(x=85, y=10)
    count.place(x=85, y=40)


# 랭킹보기 버튼
rank_btn = Button(text='랭킹보기', height=3, width=17, command=create_rank_page)
rank_btn.place(x=1, y=240)


# 퀴즈풀러 가기 버튼
quiz_btn = Button(text='퀴즈풀러 가기', height=3, width=17, command=create_game_page)
quiz_btn.place(x=135, y=240)


# 종료 기능 선언
def close_window():
    w.destroy()


# 종료 버튼 구현
exit_btn = Button(text='종   료', height=3, width=17, command=close_window)
exit_btn.place(x=270, y=240)


# 메인UI 구동
w.mainloop()