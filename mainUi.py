from tkinter import *
import tkinter.font
import tkinter.ttk
# 메인 UI
w = Tk()
w.title("초성 Quiz!")
w.geometry("400x297")
# 메인 이미지 넣기
photo = PhotoImage(file="./image/main.png")
pLabel = Label(w, image=photo)
pLabel.pack(expand=1, anchor=N)
# 랭킹페이지 새창 생성
def create_rank_page():
    newWindow = Toplevel(w)
    newWindow.title('랭킹현황')
    newWindow.geometry("250x297")
    rank = Label(newWindow, text='순위', fg='blue')
    rank.place(x=20, y=10)
    name = Label(newWindow, text='닉네임', fg='red')
    name.place(x=75, y=10)
    score = Label(newWindow, text='점수', fg='purple')
    score.place(x=145, y=10)
    time = Label(newWindow, text='시간', fg='green')
    time.place(x=200, y=10)
    listbox = Listbox(newWindow, width=32, height=15)
    listbox.place(x=10, y=40)
# 게임 설명 페이지
def create_how_page():
    newWindow = Toplevel(w)
    newWindow.title('게임설명')
    newWindow.geometry("250x297")
# 게임 페이지 새창 생성
def create_game_page():
    newWindow = Toplevel(w)
    newWindow.title('초성 Quiz!')
    newWindow.geometry("400x297")
    # 버튼들
    how_btn = Button(newWindow, text='게임설명', height=3, width=17, command=create_how_page)
    how_btn.place(x=1, y=240)
    start_btn = Button(newWindow, text='게임시작!', height=3, width=17)
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
    progress_bar = tkinter.ttk.Progressbar(newWindow, length=190, maximum=100, value=30)
    progress_bar.place(x=100, y=155)
    # 초성 입력 부분
    font = tkinter.font.Font(size=20)
    chosung_input = Entry(newWindow, width=12, font=font, justify='center')
    chosung_input.place(x=98, y=190)
    # 라운드 수 표시
    font2 = tkinter.font.Font(size=15, weight='bold')
    round = Label(newWindow, text='라운드 : ',width=12, font=font2, justify='center')
    count = Label(newWindow, text='정답수 : ', width=12, font=font2, justify='center')
    round.place(x=85, y=10)
    count.place(x=85, y=40)
# 랭킹보기 버튼
rank_btn = Button(text='랭킹보기', height=3, width=17, command=create_rank_page)
rank_btn.place(x=1, y=240)
# 퀴즈풀러 가기 버튼
quiz_btn = Button(text='퀴즈풀러 가기', height=3, width=17, command=create_game_page)
quiz_btn.place(x=135, y=240)
# 종료 버튼
def close_window():
    w.destroy()
exit_btn = Button(text='종   료', height=3, width=17, command=close_window)
exit_btn.place(x=270, y=240)

w.mainloop()