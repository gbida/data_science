import tkinter
import tkinter.font
import tkinter.messagebox
import tkinter.ttk as ttk
from tkinter import *
from tkinter import simpledialog
import pandas
import time


# class로 chosungApp 기본 프레임 묶어주기
class chosungApp(Tk):
    def __init__(w):
        super().__init__()
        w.title('아름다운 우리말 초성게임')
        w.geometry('500x500')
        w.working_frame = ttk.Frame(w)
        w.working_frame.grid(row=0, column=0, sticky='nsew')
        w.window1()

    # 전환 창 정의
    def window1(w):
        w.working_frame.destroy()
        w.working_frame = ttk.Frame(w, width=500, height=500, relief='groove')
        w.working_frame.pack_propagate(False)
        # 메인 gui 이미지 넣기
        main = PhotoImage(file='../image/mainimage.png')
        main_label = tkinter.Label(w.working_frame, image=main)
        main_label.place(x=0, y=0)
        # 랭킹보기 클릭하면 rank.xlxs 파일을 txt로 변환 후 읽어서 listbox에 표시한다.
        ttk.Button(w.working_frame, text='랭킹보기', width=17, command=w.window2).place(x=50, y=450)
        ttk.Button(w.working_frame, text='퀴즈풀기', width=17, command=w.window3).place(x=185, y=450)
        ttk.Button(w.working_frame, text='종료', width=17, command=w.destroy).place(x=320, y=450)
        w.working_frame.pack(side='top', pady=(0, 0))
        w.mainloop()

    def window2(w):
        w.working_frame.destroy()
        w.working_frame = ttk.Frame(w, width=500, height=500, relief='groove')
        w.working_frame.pack_propagate(False)
        font = tkinter.font.Font(size=30, weight='bold')
        ttk.Label(w.working_frame, text='랭 킹 현 황', font=font).place(x=148, y=32)
        ttk.Button(w.working_frame, text='퀴즈풀기', command=w.window3, width=17).place(x=50, y=450)
        ttk.Button(w.working_frame, text='초기화면', command=w.window1, width=17).place(x=185, y=450)
        ttk.Button(w.working_frame, text='종료', width=17, command=w.destroy).place(x=320, y=450)
        font = tkinter.font.Font(size=16, weight='bold')
        # rnak엑셀파일 열어서 txt 저장
        data = pandas.read_excel("./rank.xlsx")
        row = data.iloc[:, :4]
        row.to_csv('rank.txt', index=0)
        # 리스트 박스에 순위 담기
        listbox1 = Listbox(w.working_frame, width=6, height=11, font=font)
        listbox1.place(x=30, y=110)
        listbox2 = Listbox(w.working_frame, width=14, height=11, font=font)
        listbox2.place(x=95, y=110)
        listbox3 = Listbox(w.working_frame, width=7, height=11, font=font)
        listbox3.place(x=260, y=110)
        listbox4 = Listbox(w.working_frame, width=13, height=11, font=font)
        listbox4.place(x=310, y=110)
        with open(r'./rank.txt', mode='r', encoding='utf-8') as rank_txt:
            for i in range(1, 11):
                if i == 1:
                    txt = str(rank_txt.readlines(i))
                    txt = txt.split(',')
                    listbox1.insert(i, '  순위')
                    listbox2.insert(i, '         ' + txt[1])
                    listbox3.insert(i, ' ' + txt[2])
                    listbox4.insert(i, '        ' + txt[3][:2])
                txt = str(rank_txt.readlines(i))
                txt = txt.split(',')
                time = txt[3].split('/')[1] + '/' + txt[3].split('/')[2][:8]
                listbox1.insert(i, '    ' + txt[0][2:])
                listbox2.insert(i, '   ' + txt[1])
                listbox3.insert(i, '  ' + txt[2])
                listbox4.insert(i, '  ' + time)
        w.working_frame.pack(side='top', pady=(0, 0))

    def window3(w):
        w.working_frame.destroy()
        w.working_frame = ttk.Frame(w, width=500, height=500, relief='groove')
        w.working_frame.pack_propagate(False)

        def timer():
            how_btn['state'] = 'disabled'
            start_btn['state'] = 'disabled'
            # 닉네임 입력받는 부분, name으로 저장된다.
            a = 0
            while a == 0:
                name = tkinter.simpledialog.askstring('닉네임 입력', '')
                if name != '':
                    a = 1
                else:
                    tkinter.messagebox.showwarning('', '닉네임을 입력하세요')
                    a = 0
            # 타이머 초과 시 게임종료 부분, 게임 진짜 실행 부분 코드구현 필요.
            j = 0
            for i in range(300):
                j += 1
                curr_progress.set(i)
                progress_bar.update()
                time.sleep(0.01)
                if j == 300:
                    font = tkinter.font.Font(size=40, weight='bold')
                    timeout = Label(w.working_frame, font=font, text='시간초과!', fg='red')
                    chosung_input['state'] = 'disabled'
                    timeout.place(x=140, y=150)
                    # 타임아웃이 되면 정답수, 닉네임, 기록 세운 시간 저장할 것.
                    break

        # 버튼삽입
        how_btn = Button(w.working_frame, text='게임설명', height=3, width=17, command=w.window4)
        how_btn.place(x=30, y=400)
        # 게임시작을 누르면 timer 함수가 실행된다.
        start_btn = Button(w.working_frame, text='게임시작!', height=3, width=17, command=timer)
        start_btn.place(x=185, y=400)
        exit_btn2 = Button(w.working_frame, text='종   료', height=3, width=17, command=w.destroy)
        exit_btn2.place(x=340, y=400)
        # 초성 표시 부분
        chosung1 = Label(w.working_frame, height=6, width=12, anchor='center', relief='ridge', borderwidth=5)
        chosung1.place(x=150, y=130)
        chosung2 = Label(w.working_frame, height=6, width=12, anchor='center', relief='ridge', borderwidth=5)
        chosung2.place(x=270, y=130)
        # 남은시간 타이머 표시
        curr_progress = tkinter.DoubleVar()
        progress_bar = tkinter.ttk.Progressbar(w.working_frame, length=300, maximum=300, variable=curr_progress)
        progress_bar.place(x=107, y=255)
        # 정답 입력 부분
        font = tkinter.font.Font(size=40)
        chosung_input = Entry(w.working_frame, font=font, width=10, justify='center')
        chosung_input.place(x=105, y=300)
        # 라운드 수 표시
        font = tkinter.font.Font(size=35, weight='bold')
        count = Label(w.working_frame, text='정답수 : ', font=font, width=12, justify='center')
        count.place(x=45, y=40)
        w.working_frame.pack(side='top', pady=(0, 0))

    def window4(w):
        w.working_frame.destroy()
        w.working_frame = ttk.Frame(w, width=500, height=500, relief='groove')
        w.working_frame.pack_propagate(False)
        page = PhotoImage(file='../image/guide.png')
        page_label = tkinter.Label(w.working_frame, image=page)
        page_label.place(x=0, y=0)
        ttk.Button(w.working_frame, text='초기화면', command=w.window1, width=17).place(x=190, y=465)
        w.working_frame.pack(side='top', pady=(0, 0))
        w.mainloop()


if __name__ == '__main__':
    chosungApp().mainloop()