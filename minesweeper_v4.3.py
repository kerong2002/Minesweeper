#2022-04-19 陳科融
#踩地雷
from tkinter import *
import tkinter.messagebox
from threading import Timer
from tkinter import ttk
from random import randint
import random
window=Tk()
window.title("minesweeper")
window.configure(bg='#d0d0d0')
# window.geometry("360x380+600+200")
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
trigger=False   #觸發判定
'''=========================<說明>=============================='''
def how_to_play():
    help_text = tkinter.Toplevel()
    help_text.geometry("560x380+500+270")
    help_text.title("How to play")
    help_text.configure(bg='#68daff')
    tkinter.Label(help_text, text='遊玩方式: 以鼠標選取該方塊，開始掃雷，場上\n'
                                  '數字是以選取點為中心的九宮格，標示炸彈的數量\n'
                                  '例： 💣 💣 1                      \n'
                                  '    💣 4  2                      \n'
                                  '     1  2 💣                      \n'
                                  '數字4周圍九宮格含有四顆炸彈，中間標示數字為4\n'
                                  '滑鼠左鍵:點擊開啟該選取之方塊                  \n'
                                  '滑鼠右鍵:點擊插上旗幟，再次點選取消插上的旗幟  \n'
                                  '滑鼠(中鍵)和(左右鍵):對著數字點擊，周遭有相對應\n'
                                  '                  旗幟數量，將會擴散地圖\n'
                                  '目標: 不要踩到任何炸彈，除去非炸彈的位置，即可獲勝\n'
                                  '  不插旗幟，點完全圖非炸彈位置，也視為勝利',font=('標楷體',15),bg='#68daff').pack(expand=True)
'''=========================<作者顯示，感謝玩家>=============================='''
def show(i):  #help呼叫
    tkinter.messagebox.showwarning(title='Author : Ke-Rong,Chen ', message='Thanks for playing!')
'''=======================<幫助提示>========================================'''
def give_help(i):
    global appear_flag,the_game,bomb_number_cnt,btn
    bombx = []
    bomby = []
    del bomby[:]
    del bombx[:]
    for y in range(bomb_number):
        bombx.append([])
        bomby.append([])
    cnt=0
    for y in range(game_Y_size):
        for x in range(game_X_size):
            if(appear_flag[y][x]!='🚩' and chess[y][x]=='💣'):
                bombx[cnt].append(x) #紀錄剩下炸彈座標
                bomby[cnt].append(y) #紀錄剩下炸彈座標
                cnt+=1
    for i in range(bomb_number-cnt):
        bombx.pop()
        bomby.pop()
    if(len(bombx)==0):
        return
    else:
        ans=randint(0,len(bombx)-1)
        x_set=bombx[ans][0]
        y_set=bomby[ans][0]
        btn[y_set][x_set].config(text='🚩', fg='#17b32b')
        appear_flag[y_set][x_set] = '🚩'
        the_game[y_set][x_set]= '🚩'
        bomb_number_cnt -= 1
        remain_bomb.set(str(bomb_number_cnt))
'''=========================<自訂義>================================'''
def show_input():
    global width_input,height_input,bomb_input,custom_window,window,frame2
    global smile,bomb_text,time_text,frame1
    w_text=w_get   #獲取寬度數字
    h_text=h_get   #獲取高度數字
    b_text=b_get   #獲取炸彈數字
    global game_X_size,game_Y_size,bomb_number
    if(w_text>=4 and w_text<=36):
        if(h_text>=4 and h_text<=20):
            if(b_text>0 and b_text<=w_text*h_text):
                custom_window.destroy()
                game_X_size = w_text
                game_Y_size = h_text
                bomb_number = b_text
                smile_do(True)   #刷新
'''=================<無旗幟模式>======================'''
Active_no_flag=False
def no_flag():
    global menu_no_flag,Active_no_flag,the_game,appear_flag,bomb_number_cnt
    if(menu_no_flag.get()):
        Active_no_flag=True
        for y in range(game_Y_size):
            for x in range(game_X_size):
                if (the_game[y][x] == '🚩'):
                    btn[y][x].config(text=' ')
                    the_game[y][x]=''
                    appear_flag[y][x]=''
                    bomb_number_cnt += 1
                    remain_bomb.set(str(bomb_number_cnt))
    else:
        Active_no_flag=False
'''=========================<下拉選單獲取值>================================'''
def combobox_set_number(event):
    global width_combobox,height_combobox,h_get,w_get,b_get,bomb_combobox
    if(width_combobox.get() and height_combobox.get()):
        w_get=int(width_combobox.get())
        h_get=int(height_combobox.get())
        bomb_combobox['values'] = tuple([i for i in range(1, h_get * w_get+1)])
    if(bomb_combobox.get()):
        b_get=int(bomb_combobox.get())
        show_input()
h_get=1
w_get=1
'''=========================<自訂義配置>================================'''
def custom():
    global width_input,height_input,bomb_input,custom_window,height_combobox,width_combobox,h_get,w_get,bomb_combobox
    custom_window= tkinter.Toplevel()
    custom_window.geometry("500x200+500+300")
    custom_window.title('Custom')
    custom_window.configure(bg='#68daff')
    width_text=Label(custom_window,text='width:(4~36)',font='80',bg='#68daff')                  #寬度文字
    width_text.place(y=70,x=50)
    width_combobox = ttk.Combobox(custom_window,width='10')#下拉選單
    width_combobox['values'] = tuple([i for i in range(4, 37)])
    width_combobox.place(y=100, x=50)
    width_combobox.bind("<<ComboboxSelected>>", combobox_set_number)
    height_text = Label(custom_window, text='hight:(4~20)', font='80', bg='#68daff')            #高度文字
    height_text.place(y=70, x=190)
    height_combobox = ttk.Combobox(custom_window,width='10')#下拉選單
    height_combobox['values'] = tuple([i for i in range(4, 21)])
    height_combobox.place(y=100, x=190)
    height_combobox.bind("<<ComboboxSelected>>", combobox_set_number)
    bomb_text = Label(custom_window, text='bomb:(1~hight*width)', font='80', bg='#68daff')      #炸彈文字
    bomb_text.place(y=70, x=320)
    bomb_combobox = ttk.Combobox(custom_window, width='10')  # 下拉選單
    bomb_combobox['values'] = tuple([i for i in range(1, h_get*w_get)])
    bomb_combobox.place(y=100, x=320)
    bomb_combobox.bind("<<ComboboxSelected>>", combobox_set_number)
'''=========================<new_game>=============================='''
def menu_operation():
    smile_do(True)
'''=========================<簡單模式>=============================='''
def easy_mod():
    global smile,bomb_text,time_text
    global game_X_size,game_Y_size,bomb_number
    game_X_size = 9
    game_Y_size = 9
    bomb_number = 10
    smile_do(True)
'''=========================<普通模式>=============================='''
def normal_mod():
    global smile,bomb_text,time_text
    global game_X_size,game_Y_size,bomb_number
    game_X_size = 16
    game_Y_size = 16
    bomb_number = 40
    smile_do(True)
'''=========================<困難模式>=============================='''
def hard_mod():
    global smile,bomb_text,time_text
    global game_X_size,game_Y_size,bomb_number
    game_X_size = 30
    game_Y_size = 16
    bomb_number = 99
    smile_do(True)
'''=========================<快捷鍵觸發刷新>====================================='''
def keyboard(event):   #刷新
    smile_do(True)
def leave(event):      #離開
    global window
    window.destroy()
'''=========================<菜單建置>====================================='''
menuBar = Menu(window)
menuFile =Menu(menuBar, tearoff=False) #設定一個file的主選單
menuBar.add_cascade(label='set',font=('Inconsolata',10), menu=menuFile)        #menu set
menuFile.add_command(label='New game',font=('Inconsolata',10), command=menu_operation,accelerator='(F2)')#新局
window.bind('<F2>', lambda event: keyboard(True))                                         #按鈕觸發
menuDifficulty = tkinter.Menu(menuFile, tearoff=False)                                    #母菜單
menuFile.add_cascade(label='Difficulty', menu=menuDifficulty)                             #子菜單建立
menuDifficulty.add_command(label='Easy',font=('Inconsolata',10), command=easy_mod,accelerator='(F3)')        #簡單難度(子菜單)
window.bind('<F3>',lambda event:easy_mod())
menuDifficulty.add_command(label='Normal',font=('Inconsolata',10), command=normal_mod,accelerator='(F4)')    #普通難度(子菜單)
window.bind('<F4>',lambda event:normal_mod())
menuDifficulty.add_command(label='Hard',font=('Inconsolata',10), command=hard_mod,accelerator='(F5)')        #困難難度(子菜單)
window.bind('<F5>',lambda event:hard_mod())
menuFile.add_command(label='How to play',font=('Inconsolata',10), command=how_to_play)    #如何遊玩
menuFile.add_command(label='Custom',font=('Inconsolata',10), command=custom)              #自訂義
menu_no_flag=BooleanVar()           #創建複選框按鈕
menu_no_flag.set(False)             #設定初始直為false
menuFile.add_checkbutton(label='No_Flag',font=('Inconsolata',10),command=no_flag,variable=menu_no_flag)      #複選按鈕
menuFile.add_command(label='Exit',font=('Inconsolata',10), command=window.destroy,accelerator='(Ctrl+Z)')    #離開遊戲
window.bind('<Control-z>',lambda event: leave(True))                                                         #按鈕觸發
menuHelp = Menu(menuBar, tearoff=False)
menuBar.add_cascade(label='help',font=('Inconsolata',10), menu=menuHelp)               #幫助
menuHelp.add_command(label='Auther',font=('Inconsolata',10), command=lambda: show('Help'))
menuHelp.add_command(label='Help',font=('Inconsolata',10), command=lambda:give_help('help_me'),accelerator='(Ctrl+H)')
window.bind('<Control-h>',lambda event: give_help('help_me'))
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
    global begin,can_play,counter,time_end,bomb_number_cnt,can_paly,begin,done_do_time,is_win,smile,bomb_text,time_text,frame1,frame2
    '''==========<清除上場建置的按鈕、smile和Label>================'''
    frame1.destroy()#下方的按鈕
    frame2.destroy()#上方smile和Label
    '''=============<trigger的觸發>==================='''
    if(trigger==True): #防止玩加第一次就按刷新遊戲
        pause()
    '''==============<開始由玩遊戲>==================='''
    if(event):
        done_do_time=True
    can_paly=0
    is_win = False
    begin = 1
    bomb_number_cnt=bomb_number
    remain_bomb.set(str(bomb_number_cnt))   #炸彈數量調整
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
    set_button()
    new_play_game()
    done_do_time = False
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
    if(done_do_time==True):
        return
    if(stop_now==True):
        return
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
                        appear_flag[ay][ax]='🚩' #贏了將炸彈處，插滿旗幟
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
    '''===========<透過3x3方塊掃描方式建置數字>============'''
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
                # if (chess[y - 1][x - 1] == ' ' and chess[y - 1][x - 1] != '💣'):
                #     play(True,)
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
    if (appear_flag[y][x] == '🚩'): #確保點選那個方塊不是旗幟
        return
    if(event  and appear_chess[y][x]==''):#確保已經開始遊戲
        can_paly=1
    if(begin==0 and can_paly==1):#開始計數
        begin=1
        t = Timer(1, change_time)
        t.start()
    global can_play,time_end
    if(can_play==True and appear_flag[y][x]!='🚩'):#採到的地方不是旗幟，開始做判定
        change_smile.set('🙂')  # oops
        if(chess[y][x]!='💣'):
            btn[y][x].config(text=chess[y][x],bg='#f0f0ee',fg=text_color[chess[y][x]])
            appear_chess[y][x]=chess[y][x]
            # 特別處理
            if(chess[y][x]==' '):
                flood_fill(y,x)
        elif(chess[y][x]=='💣'): #採到炸彈處理
            time_end=True
            can_play=False
            for ay in range(game_Y_size):
                for ax in range(game_X_size):
                    if(the_game[ay][ax]=='🚩' and chess[ay][ax]!='💣'):
                        btn[ay][ax].config(text='❌',bg='Magenta',fg='red') #標示出旗幟插到不是炸彈位置的地方
                    elif(chess[ay][ax]=='💣'):
                        if(the_game[ay][ax]!='🚩'):
                            btn[ay][ax].config(bg='#f0f0ee',text=chess[ay][ax],fg='black')#標示出炸彈
            btn[y][x].config(text=chess[y][x], bg='Red')#採到炸彈那格會設定紅色
            change_smile.set('😱')
'''=========================<裝飾器>============================'''
def handlerAdaptor(fun, **kwds):
	'''事件處裡函數的配飾器，相當於一個中介'''
	return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)
'''=========================<旗幟處發>============================'''
flag_cnt=0
def flag(event,x,y):
    global appear_flag,bomb_number_cnt,is_win,Active_no_flag
    if(Active_no_flag==True):
        return
    if(is_win==True): #贏了停止旗幟插旗
        return
    if (can_play == True and appear_chess[y][x]==''): #正常插旗幟
        if(appear_flag[y][x]==''):   #第一次插旗幟
            btn[y][x].config(text='🚩',fg='red')
            appear_flag[y][x]='🚩'
            the_game[y][x]='🚩'
            bomb_number_cnt-=1
            remain_bomb.set(str(bomb_number_cnt))
        elif(appear_flag[y][x]=='🚩'): #拔除旗幟
            btn[y][x].config(text=' ')
            appear_flag[y][x]=''
            the_game[y][x]=' '
            bomb_number_cnt += 1
            remain_bomb.set(str(bomb_number_cnt))
'''=========================<勝利數組配置>============================'''
def win_set():
    # for y in range(game_Y_size):
    #     print(chess[y])
    for y in range(game_Y_size):
        for x in range(game_X_size):
            if(chess[y][x]!='💣'):
                win_answer[y][x]=chess[y][x]
win_set()
'''=========================<初始設定>============================'''
change_smile=StringVar()
change_smile.set('🙂')                   #笑臉
remain_bomb=StringVar()
remain_bomb.set(str(bomb_number_cnt))   #剩餘炸彈數量
labelText = StringVar()
labelText.set(str(counter))             #計數時間
'''=========================<新遊戲設定>============================'''
def new_play_game():
    global bomb_text,time_text,smile,frame2,game_X_size,game_Y_size,frame1
    frame1.update()
    frame2 = Frame(bg="#d0d0d0", bd=3, relief=SUNKEN, width=frame1.winfo_width()-10, height=60)
    bomb_text=Label(frame2, textvariable=remain_bomb,font='160',height='2',bg='#d0d0d0')
    bomb_text.place(relx=0.10-0.008*(game_X_size/4),rely=0.5,anchor=CENTER)
    time_text=Label(frame2, textvariable=labelText,font='160',height='2',bg='#d0d0d0')
    time_text.place(relx=0.94+0.003*(game_X_size/4),rely=0.5,anchor=CENTER)
    smile=Button(frame2,textvariable=change_smile,font='200',height='2',bg='Snow',cursor="hand2")
    smile.bind("<Button-1>",smile_do)#左鍵
    smile.place(relx=0.5,rely=0.5,anchor="center")
    frame2.place(x=15,y=20)
'''=========================<滑鼠中鍵搜尋>============================'''
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
'''===============<臉部表情oops>========================'''
def oops(event,x,y):
    global  time_end
    if (time_end==True): #確保點選那個方塊不是旗幟
        return
    change_smile.set('😮')  #oops
'''=========================<配置按鈕>============================'''
def set_button():
    global text_color,test_Frame,frame1
    '''=========================<配置外框>============================'''
    frame1 = Frame(bg="#302f33", bd=5, relief=SUNKEN, width=200, height=100)
    for y in range(game_Y_size):
        btn.append([])
        for x in range(game_X_size):
            btn[y].append(Button(frame1,width = 3,height = 1, relief=RAISED,anchor='center'))
            btn[y][x].bind("<Button-1>", handlerAdaptor(oops, x=x, y=y))          #滑鼠左鍵觸發
            btn[y][x].bind("<ButtonRelease-1>",handlerAdaptor(play,x=x,y=y))      #滑鼠左鍵觸發
            btn[y][x].bind("<Button-2>", handlerAdaptor(search, x=x, y=y))        #滑鼠中鍵觸發
            btn[y][x].bind("<Button-1><Button-3>", handlerAdaptor(search, x=x, y=y))  # 滑鼠左右鍵觸發
            btn[y][x].bind("<Button-3><Button-1>", handlerAdaptor(search, x=x, y=y))  # 滑鼠左右鍵觸發
            btn[y][x].bind("<ButtonRelease-3>", handlerAdaptor(flag, x=x, y=y))   #滑鼠右鍵觸發
            btn[y][x].config(text=' ',font='30', bg='#c6c6d3',fg=text_color[chess[y][x]])
            btn[y][x].grid(row=y,column=x)
    frame1.place(x=10,y=100)
    frame1.update() #抓取所需視窗大小
    window.geometry(f'{frame1.winfo_width()+20}x{frame1.winfo_height()+110}+{700-20*(game_X_size-4)}+{250-10*(game_Y_size-4)}') #配置位置
set_button()
new_play_game()
window.mainloop()