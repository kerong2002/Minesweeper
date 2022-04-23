#2022-04-19 陳科融
#踩地雷
from tkinter import *
import tkinter.messagebox
from threading import Timer
import random
window=Tk()
window.title("minesweeper")
window.configure(bg='#d0d0d0')
window.geometry("510x670+400+70")
bomb_number=10  #炸彈
game_Y_size=9   #高度
game_X_size=9   #寬度
btn=[]          #按鈕
number_list=[]  #數組
the_game=[]     #遊玩結果
appear_chess=[] #出現的chess
appear_flag=[] #出現的旗幟
can_play=True   #開始條件
time_end=False  #結束條件
bomb_number_cnt=bomb_number #剩餘
win_answer=[]   #勝利條件
is_win=False    #是否勝利
stop_now=False  #是否強制暫停
trigger=False
'''=========================<mune>=============================='''
def show(i):
    tkinter.messagebox.showwarning(title='Author : Ke-Rong,Chen ', message='Thanks for playing!')
    print('help')
def menu_operation():
    smile_do(True)
menuBar = Menu(window)
menuFile =Menu(menuBar, tearoff=False)
menuBar.add_cascade(label='set',font=('Inconsolata',10), menu=menuFile)        #menu set
menuFile.add_command(label='New game',font=('Inconsolata',10), command=menu_operation)#新局
menuFile.add_command(label='Exit',font=('Inconsolata',10), command=window.destroy)#清除
menuHelp = Menu(menuBar, tearoff=False)
menuBar.add_cascade(label='help',font=('Inconsolata',10), menu=menuHelp)
menuHelp.add_command(label='Help',font=('Inconsolata',10), command=lambda: show('Help'))
window.config(menu=menuBar)
'''=========================<數字顏色>============================'''
text_color={
' ':'black',
'💣':'#f712fc',
"1" : 'Blue',
'2':'#01ab30',
'3':'#ff0d0d',
'4':'#011e7e',
'5':'#7e291d',
'6':'#2d7c8a',
'7':'#c27807',
'8':'#681a62'
}
'''=========================<清空配置>============================'''
def clear_array():
    del chess[:]
    del the_game[:]
    del appear_chess[:]
    del appear_flag[:]
    del win_answer[:]
    del bomb[:]
    del btn[:]
'''=========================<笑臉功能>============================'''
done_do_time=False
def smile_do(event):
    global begin,can_play,counter,time_end,bomb_number_cnt,can_paly,begin,done_do_time,is_win
    if(trigger==True):
        pause()
    if(event):
        done_do_time=True
    can_paly=0
    is_win = False
    begin = 1
    bomb_number_cnt=bomb_number
    remain_bomb.set(str(bomb_number_cnt))
    begin=0
    counter = 0
    time_end=False
    labelText.set(str(counter))
    can_play=True
    change_smile.set('🙂')
    clear_array()
    new_set_chess()
    boom_set()
    new_set_number()
    win_set()
    new_play_game()
    set_button()
    done_do_time = False
    print('smile')
'''=========================<計時器>============================'''
t = None
counter = 0
def change_time():
    global stop_now
    global labelText
    global counter
    global t
    global is_win
    global done_do_time
    # print(done_do_time,stop_now,sep='.')
    if(done_do_time==True):
        return
    if(stop_now==True):
        return
    # print(time_end,is_win,can_play,sep=',')
    if(time_end==False and is_win==False and can_paly==1):
        counter = counter + 1
        labelText.set(str(counter))
        cnt_win=0
        for i in range(game_Y_size):
            if(appear_chess[i]==win_answer[i]):
                cnt_win+=1
        if(cnt_win==game_Y_size):
            is_win=True
            change_smile.set('😎')
            for ay in range(game_Y_size):
                for ax in range(game_X_size):
                    if(chess[ay][ax]=='💣'):
                        appear_flag[ay][ax]='🚩'
                        the_game[ay][ax]='🚩'
                        remain_bomb.set('0')
                        btn[ay][ax].config(text='🚩',fg='red')
            return
        t = Timer(1, change_time)
        t.start()
    elif(time_end==True):
        return
'''=========================<暫停>============================'''
def pause():
    global window
    global t
    t.cancel()

'''========================<建置棋盤>========================='''
chess=[]
def new_set_chess():
    global chess
    for y in range(game_Y_size):
        chess.append([])
        the_game.append([])
        appear_chess.append([])
        appear_flag.append([])
        win_answer.append([])
        for x in range(game_X_size):
            chess[y].append(' ')
            the_game[y].append(' ')
            appear_chess[y].append('')
            appear_flag[y].append('')
            win_answer[y].append('')
new_set_chess()
'''==========================<炸彈>==========================='''
bomb=[]
def boom_set():
    bomb.append(random.sample(range(0, game_Y_size*game_X_size),bomb_number))
    for i in range(bomb_number):
        y=int(int(bomb[0][i])/game_X_size)
        x=int(int(bomb[0][i])%game_X_size)
        chess[int(y)][int(x)]='💣'
boom_set()
'''========================<建置數字>========================='''
def new_set_number():
    for y in range(game_Y_size):
        for x in range(game_X_size):
            if(chess[y][x]=='💣'):
                continue
            elif(chess[y][x]!='💣'):
                found=0
                for i in range(y-1,y+2):
                    if(i<0):
                        continue
                    if(i>=game_Y_size):
                        continue
                    for j in range(x-1,x+2):
                        if(j<0):
                            continue
                        if(j>=game_X_size):
                            continue
                        if(chess[i][j]=='💣'):
                            found+=1
                if(found!=0):
                    chess[y][x]=str(found)
new_set_number()
'''================<搜尋空白演算法>============================'''
def  flood_fill(y,x):
    if(x < game_X_size-1):
        if(chess[y][x+1] == ' ' and appear_chess[y][x+1]!=' '):
            btn[y][x+1].config(text=chess[y][x+1], bg='#f0f0ee')
            appear_chess[y][x+1] = chess[y][x+1]
            the_game[y][x + 1] = chess[y][x + 1]
            flood_fill(y,x+1)
        elif(chess[y][x+1] != ' ' and chess[y][x+1]!='💣' ):
            btn[y][x + 1].config(text=chess[y][x + 1], bg='#f0f0ee')
            appear_chess[y][x + 1] = chess[y][x + 1]
            the_game[y][x + 1] = chess[y][x + 1]
            if (y > 0 and x > 0):
                if (chess[y - 1][x - 1] != ' ' and chess[y - 1][x - 1] != '💣'):
                    btn[y - 1][x - 1].config(text=chess[y - 1][x - 1], bg='#f0f0ee',fg=text_color[chess[y - 1][x - 1]])
                    appear_chess[y - 1][x - 1] = chess[y - 1][x - 1]
                    the_game[y - 1][x - 1] = chess[y - 1][x - 1]
            if (x < game_X_size - 1 and y < game_Y_size - 1):
                if (chess[y + 1][x + 1] != ' ' and chess[y + 1][x + 1] != '💣'):
                    btn[y + 1][x + 1].config(text=chess[y + 1][x + 1], bg='#f0f0ee',fg=text_color[chess[y + 1][x + 1]])
                    appear_chess[y + 1][x + 1] = chess[y + 1][x + 1]
                    the_game[y + 1][x + 1] = chess[y + 1][x + 1]
            if (x > 0 and y < game_Y_size - 1):
                if (chess[y + 1][x - 1] != ' ' and chess[y + 1][x - 1] != '💣'):
                    btn[y + 1][x - 1].config(text=chess[y + 1][x - 1], bg='#f0f0ee',fg=text_color[chess[y + 1][x - 1]])
                    appear_chess[y + 1][x - 1] = chess[y + 1][x - 1]
                    the_game[y + 1][x - 1] = chess[y + 1][x - 1]
            if (y > 0 and x < game_X_size - 1):
                if (chess[y - 1][x + 1] != ' ' and chess[y - 1][x + 1] != '💣'):
                    btn[y - 1][x + 1].config(text=chess[y - 1][x + 1], bg='#f0f0ee',fg=text_color[chess[y - 1][x + 1]])
                    appear_chess[y - 1][x + 1] = chess[y - 1][x + 1]
                    the_game[y - 1][x + 1] = chess[y - 1][x + 1]
    if(x > 0):
        if(chess[y][x-1]==' ' and appear_chess[y][x-1] != ' '):
            btn[y][x-1].config(text=chess[y][x-1], bg='#f0f0ee')
            appear_chess[y][x-1] = chess[y][x-1]
            the_game[y][x-1] = chess[y][x-1]
            flood_fill(y,x-1)
        elif (chess[y][x-1]!= ' ' and chess[y][x-1]!= '💣'):
            btn[y][x-1].config(text=chess[y][x-1], bg='#f0f0ee', fg=text_color[chess[y][x-1]])
            appear_chess[y][x-1] = chess[y][x-1]
            the_game[y][x - 1] = chess[y][x - 1]
            if (y > 0 and x > 0):
                if (chess[y - 1][x - 1] != ' ' and chess[y - 1][x - 1] != '💣'):
                    btn[y - 1][x - 1].config(text=chess[y - 1][x - 1], bg='#f0f0ee', fg=text_color[chess[y - 1][x - 1]])
                    appear_chess[y - 1][x - 1] = chess[y - 1][x - 1]
                    the_game[y - 1][x - 1] = chess[y - 1][x - 1]
            if (x < game_X_size - 1 and y < game_Y_size - 1):
                if (chess[y + 1][x + 1] != ' ' and chess[y + 1][x + 1] != '💣'):
                    btn[y + 1][x + 1].config(text=chess[y + 1][x + 1], bg='#f0f0ee', fg=text_color[chess[y + 1][x + 1]])
                    appear_chess[y + 1][x + 1] = chess[y + 1][x + 1]
                    the_game[y + 1][x + 1] = chess[y + 1][x + 1]
            if (x > 0 and y < game_Y_size - 1):
                if (chess[y + 1][x - 1] != ' ' and chess[y + 1][x - 1] != '💣'):
                    btn[y + 1][x - 1].config(text=chess[y + 1][x - 1], bg='#f0f0ee', fg=text_color[chess[y + 1][x - 1]])
                    appear_chess[y + 1][x - 1] = chess[y + 1][x - 1]
                    the_game[y + 1][x - 1] = chess[y + 1][x - 1]
            if (y > 0 and x < game_X_size - 1):
                if (chess[y - 1][x + 1] != ' ' and chess[y - 1][x + 1] != '💣'):
                    btn[y - 1][x + 1].config(text=chess[y - 1][x + 1], bg='#f0f0ee', fg=text_color[chess[y - 1][x + 1]])
                    appear_chess[y - 1][x + 1] = chess[y - 1][x + 1]
                    the_game[y - 1][x + 1] = chess[y - 1][x + 1]
    if (y < game_Y_size - 1):
        if (chess[y + 1][x] == ' ' and appear_chess[y + 1][x]!= ' '):
            btn[y + 1][x].config(text=chess[y + 1][x], bg='#f0f0ee')
            appear_chess[y + 1][x] = chess[y + 1][x]
            the_game[y + 1][x] = chess[y + 1][x]
            flood_fill(y + 1, x)
        elif (chess[y + 1][x]!= ' ' and chess[y + 1][x]!= '💣'):
            btn[y + 1][x].config(text=chess[y + 1][x], bg='#f0f0ee', fg=text_color[chess[y + 1][x]])
            appear_chess[y + 1][x]= chess[y + 1][x]
            the_game[y + 1][x] = chess[y + 1][x]
            if (y > 0 and x > 0):
                if (chess[y - 1][x - 1] != ' ' and chess[y - 1][x - 1] != '💣'):
                    btn[y - 1][x - 1].config(text=chess[y - 1][x - 1], bg='#f0f0ee', fg=text_color[chess[y - 1][x - 1]])
                    appear_chess[y - 1][x - 1] = chess[y - 1][x - 1]
                    the_game[y - 1][x - 1] = chess[y - 1][x - 1]
            if (x < game_X_size - 1 and y < game_Y_size - 1):
                if (chess[y + 1][x + 1] != ' ' and chess[y + 1][x + 1] != '💣'):
                    btn[y + 1][x + 1].config(text=chess[y + 1][x + 1], bg='#f0f0ee', fg=text_color[chess[y + 1][x + 1]])
                    appear_chess[y + 1][x + 1] = chess[y + 1][x + 1]
                    the_game[y + 1][x + 1] = chess[y + 1][x + 1]
            if (x > 0 and y < game_Y_size - 1):
                if (chess[y + 1][x - 1] != ' ' and chess[y + 1][x - 1] != '💣'):
                    btn[y + 1][x - 1].config(text=chess[y + 1][x - 1], bg='#f0f0ee', fg=text_color[chess[y + 1][x - 1]])
                    appear_chess[y + 1][x - 1] = chess[y + 1][x - 1]
                    the_game[y + 1][x - 1] = chess[y + 1][x - 1]
            if (y > 0 and x < game_X_size - 1):
                if (chess[y - 1][x + 1] != ' ' and chess[y - 1][x + 1] != '💣'):
                    btn[y - 1][x + 1].config(text=chess[y - 1][x + 1], bg='#f0f0ee', fg=text_color[chess[y - 1][x + 1]])
                    appear_chess[y - 1][x + 1] = chess[y - 1][x + 1]
                    the_game[y - 1][x + 1] = chess[y - 1][x + 1]
    if(y > 0):
        if(chess[y - 1][x] == ' ' and appear_chess[y - 1][x]!= ' '):
            btn[y-1][x].config(text=chess[y-1][x], bg='#f0f0ee')
            appear_chess[y-1][x] = chess[y-1][x]
            the_game[y - 1][x] = chess[y - 1][x]
            flood_fill(y-1,x)
        elif (chess[y-1][x]!= ' ' and chess[y-1][x]!= '💣'):
            btn[y-1][x].config(text=chess[y-1][x], bg='#f0f0ee', fg=text_color[chess[y-1][x]])
            appear_chess[y-1][x]= chess[y-1][x]
            the_game[y - 1][x] = chess[y - 1][x]
            if (y > 0 and x > 0):
                if (chess[y - 1][x - 1] != ' ' and chess[y - 1][x - 1] != '💣'):
                    btn[y - 1][x - 1].config(text=chess[y - 1][x - 1], bg='#f0f0ee', fg=text_color[chess[y - 1][x - 1]])
                    appear_chess[y - 1][x - 1] = chess[y - 1][x - 1]
                    the_game[y - 1][x - 1] = chess[y - 1][x - 1]
            if (x < game_X_size - 1 and y < game_Y_size - 1):
                if (chess[y + 1][x + 1] != ' ' and chess[y + 1][x + 1] != '💣'):
                    btn[y + 1][x + 1].config(text=chess[y + 1][x + 1], bg='#f0f0ee', fg=text_color[chess[y + 1][x + 1]])
                    appear_chess[y + 1][x + 1] = chess[y + 1][x + 1]
                    the_game[y + 1][x + 1] = chess[y + 1][x + 1]
            if (x > 0 and y < game_Y_size - 1):
                if (chess[y + 1][x - 1] != ' ' and chess[y + 1][x - 1] != '💣'):
                    btn[y + 1][x - 1].config(text=chess[y + 1][x - 1], bg='#f0f0ee', fg=text_color[chess[y + 1][x - 1]])
                    appear_chess[y + 1][x - 1] = chess[y + 1][x - 1]
                    the_game[y + 1][x - 1] = chess[y + 1][x - 1]
            if (y > 0 and x < game_X_size - 1):
                if (chess[y - 1][x + 1] != ' ' and chess[y - 1][x + 1] != '💣'):
                    btn[y - 1][x + 1].config(text=chess[y - 1][x + 1], bg='#f0f0ee', fg=text_color[chess[y - 1][x + 1]])
                    appear_chess[y - 1][x + 1] = chess[y - 1][x + 1]
                    the_game[y - 1][x + 1] = chess[y - 1][x + 1]
'''=========================<開始遊玩觸發>============================'''
begin=0
def play(event,x,y):
    global t,begin,time_end,appear_flag,bomb_number_cnt,can_paly,trigger
    trigger = True
    if (appear_flag[y][x] == '🚩'):
        return
    if(event  and appear_chess[y][x]==''):
        can_paly=1
    if(begin==0 and can_paly==1):#開始計數
        begin=1
        t = Timer(1, change_time)
        t.start()
    global can_play,time_end
    if(can_play==True and appear_flag[y][x]!='🚩'):
        if(chess[y][x]!='💣'):
            btn[y][x].config(text=chess[y][x],bg='#f0f0ee',fg=text_color[chess[y][x]])
            appear_chess[y][x]=chess[y][x]
            # 特別處理
            if(chess[y][x]==' '):
                flood_fill(y,x)
        elif(chess[y][x]=='💣'):
            time_end=True
            can_play=False
            for ay in range(game_Y_size):
                for ax in range(game_X_size):
                    if(the_game[ay][ax]=='🚩' and chess[ay][ax]!='💣'):
                        btn[ay][ax].config(text='❌',bg='Magenta',fg='red')
                    elif(chess[ay][ax]=='💣'):
                        if(the_game[ay][ax]!='🚩'):
                            btn[ay][ax].config(bg='#f0f0ee',text=chess[ay][ax],fg='black')
            btn[y][x].config(text=chess[y][x], bg='Red')
            change_smile.set('😱')
'''=========================<裝飾器>============================'''
def handlerAdaptor(fun, **kwds):
	'''事件處裡函數的配飾器，相當於一個中介'''
	return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)
'''=========================<旗幟處發>============================'''
flag_cnt=0
def flag(event,x,y):
    global appear_flag,bomb_number_cnt,is_win
    if(is_win==True):
        return
    if (can_play == True and appear_chess[y][x]==''):
        if(appear_flag[y][x]==''):
            btn[y][x].config(text='🚩',fg='red')
            appear_flag[y][x]='🚩'
            the_game[y][x]='🚩'
            bomb_number_cnt-=1
            remain_bomb.set(str(bomb_number_cnt))
        elif(appear_flag[y][x]=='🚩'):
            btn[y][x].config(text=' ')
            appear_flag[y][x]=''
            the_game[y][x]=' '
            bomb_number_cnt += 1
            remain_bomb.set(str(bomb_number_cnt))
'''=========================<勝利數組配置>============================'''
def win_set():
    for y in range(game_Y_size):
        print(chess[y])
    for y in range(game_Y_size):
        for x in range(game_X_size):
            if(chess[y][x]!='💣'):
                win_answer[y][x]=chess[y][x]
win_set()
'''=========================<初始設定>============================'''
change_smile=StringVar()
change_smile.set('🙂')
remain_bomb=StringVar()
remain_bomb.set(str(bomb_number_cnt))
labelText = StringVar()
labelText.set(str(counter))
'''=========================<新遊戲設定>============================'''
def new_play_game():
    Label(window, textvariable=remain_bomb,font='160',height='3',bg='#d0d0d0').place(y = 10,x = 5*game_X_size)
    Label(window, textvariable=labelText,font='160',height='3',bg='#d0d0d0').place(y = 10,x = 50*game_Y_size)
    smile=Button(window,textvariable=change_smile,font='200',height='2',bg='Snow')
    smile.bind("<Button-1>",smile_do)#左鍵
    smile.place(y = 15,x = int(26*game_X_size+4/2))
new_play_game()
'''=========================<左右鍵搜尋>============================'''
def search(event,x,y):
    global appear_flag,game_Y_size,game_X_size,appear_chess
    if(chess[y][x]==' 'or appear_chess[y][x]=='' ):
        return
    pick_number=int(chess[y][x])
    search_flag=0
    for i in range(y-1,y+2):
        if(i<0):
            continue
        if(i>=game_Y_size):
            continue
        for j in range(x-1,x+2):
            if(j<0):
                continue
            if(j>=game_X_size):
                continue
            if(the_game[i][j]=='🚩'):
                search_flag+=1
    if(search_flag==pick_number):
        for i in range(y - 1, y + 2):
            if (i < 0):
                continue
            if (i >= game_Y_size):
                continue
            for j in range(x - 1, x + 2):
                if (j < 0):
                    continue
                if (j >= game_X_size):
                    continue
                if(i==y and j==x):
                    continue
                if(appear_chess[i][j]==''):
                    play(True,j,i)
'''=========================<配置按鈕>============================'''
def set_button():
    global text_color
    for y in range(game_Y_size):
        btn.append([])
        for x in range(game_X_size):
            btn[y].append(Button(window,width = 4,height = 2, relief='raised',anchor='center'))
            btn[y][x].bind("<Button-3>",handlerAdaptor(flag,x=x,y=y))
            btn[y][x].bind("<Button-1>",handlerAdaptor(play,x=x,y=y))
            btn[y][x].bind("<Button-2>", handlerAdaptor(search, x=x, y=y))
            btn[y][x].config(text=' ',font='35', bg='#c6c6d3',fg=text_color[chess[y][x]])
            btn[y][x].place(y = 57*y+80,x = 52*x+20)
set_button()
window.mainloop()