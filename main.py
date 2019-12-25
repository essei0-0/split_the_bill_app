import tkinter as tk
import tkinter.ttk as ttk


# 画像
'''def photo(root, name, x, y):

    global img
    img = tk.PhotoImage(file = name)
    cv = tk.Canvas(root, bg = root['bg'], width = 300, height = 200)
    cv.create_image(150, 100, image = img)
    cv.grid(column = x, row = y)
'''



# start

def pushed_start():

    root_start.destroy()

    main_money()

def main_start():

    global root_start
    root_start = tk.Tk()
    root_start.title('アプリ')
    root_start.geometry('600x400')
    root_start.configure(bg = 'white')

    root_start.columnconfigure(0, weight=1)
    root_start.rowconfigure(0, weight=1)

    button_start = tk.Button(root_start, text='start', command=pushed_start)
    button_start.grid(column=0, row=0)


    """
    photo(root_start, 'main_photo.png', 2, 2)

    img = tk.PhotoImage(file = 'money_photo.png')

    img_Label = tk.Label(root_start, image = img)
    img_Label['bg'] = root_start['bg']
    img_Label.grid(column = 2, row = 2)
    """

    root_start.mainloop()



# money

def pushed_back_start():
    root_money.destroy()
    main_start()

def pushed_decision_money():

    global value_money
    #int(整数以外)とすると、エラーが起こるため、ここではstr型のまま扱う
    value_money = input_money.get()

    #数字だけの文字列か判断する
    if value_money.isnumeric():
        if int(value_money) > 0:
            value_money = int(value_money)

            print('金額:{}'.format(value_money))
            print('---------------------')

            root_money.destroy()

            main_number()

    else:
        # （位置を特定すればエラーの文字は上書きされる）
        error_Label_money = tk.Label(root_money, text='error')
        error_Label_money.grid(column=0, row=4)



def main_money():

    global root_money
    root_money = tk.Tk()
    root_money.title('アプリ')
    root_money.geometry('600x600')
    root_money.configure(bg = 'white')

    root_money.columnconfigure(0, weight=1)

    root_money.rowconfigure(0, weight=1)
    root_money.rowconfigure(1, weight=1)
    root_money.rowconfigure(2, weight=1)
    root_money.rowconfigure(3, weight=1)

    label_money = tk.Label(root_money, text='金額')
    label_money.grid(column=0, row=0, sticky=tk.S)

    global input_money
    input_money = tk.Entry(root_money)
    input_money.grid(column=0, row=1, ipadx=30, ipady=5)

    button_decision_money = tk.Button(root_money, text='決定', command=pushed_decision_money)
    button_decision_money.grid(column=0, row=2,sticky=tk.N)

    button_back_start = tk.Button(root_money, text='戻る', command=pushed_back_start)
    button_back_start.grid(column=0, row=3)


    """
    img = tk.PhotoImage(file = 'main_photo.png')

    img_Label = tk.Label(root_money, image = img)
    img_Label['bg'] = root_money['bg']
    img_Label.grid(column = 4, row = 4)
    """

    root_money.mainloop()




#　人数

def pushed_back_money():
    root_number.destroy()
    main_money()

def pushed_decision_number():

    global value_number
    value_number = input_number.get()

    if value_number.isnumeric():
        if int(value_number) > 0:
            value_number = int(value_number)

            print('人数:{}'.format(value_number))
            print('------------------------')
            root_number.destroy()

            main_personal()

    else:
        error_number = tk.Label(root_number, text='error')
        error_number.grid(column=0, row=4)


def main_number():

    global root_number
    root_number = tk.Tk()
    root_number.title('アプリ')
    root_number.geometry('600x600')

    root_number.columnconfigure(0, weight=1)

    root_number.rowconfigure(0, weight=1)
    root_number.rowconfigure(1, weight=1)
    root_number.rowconfigure(2, weight=1)
    root_number.rowconfigure(3, weight=1)

    label_number = tk.Label(root_number, text='人数')
    label_number.grid(column=0, row=0, sticky=tk.S)

    global input_number
    input_number = tk.Entry(root_number)
    input_number.grid(column=0, row=1)

    button_decision_number = tk.Button(root_number, text='決定', command=pushed_decision_number)
    button_decision_number.grid(column=0, row=2, sticky=tk.N)

    button_back_money = tk.Button(root_number, text='戻る', command=pushed_back_money)
    button_back_money.grid(column=0, row=3)

    root_number.mainloop()







# 個人情報

def pushed_back_number():
    root_personal.destroy()
    main_number()

#　決定ボタンを押すとこれが作動する
def pushed_decision_personal():

    print('性別：{}'.format(get_sex))
    print('職業：{}'.format(get_job))
    print('------------')

    for i in range(1, value_number+1):

        print('player：{}'.format(i))
        print('性別：{}'.format(get_sex[i-1]))
        print('職業：{}'.format(get_job[i-1]))
        print('----------------')


    for i in range(1, value_number+1):

        if get_sex[i-1] == '未選択':
            get_sex[i-1] = 5

        if get_sex[i-1] == '男性':
            get_sex[i-1] = 7

        if get_sex[i-1] == '女性':
            get_sex[i-1] = 3


    for i in range(1, value_number+1):

        if get_job[i-1] == '未選択':
            get_job[i-1] = 5

        if get_job[i-1] == '会社員':
            get_job[i-1] = 7

        if get_job[i-1] == '学生':
            get_job[i-1] = 3.5

        if get_job[i-1] == 'フリーター':
            get_job[i-1] = 3

        if get_job[i-1] == 'ニート':
            get_job[i-1] = 1

    root_personal.destroy()

    main_final()


# 個人情報のフレームを作る
def main_personal():

    global root_personal
    root_personal = tk.Tk()
    root_personal.title('アプリ')
    root_personal.geometry('600x600')


    for i in range(0, value_number+1):
        root_personal.columnconfigure(i, weight=1)

    for i in range(0, 6):
        root_personal.rowconfigure(i, weight=1)

    label_personal = tk.Label(root_personal, text='個人情報')
    label_personal.grid(column=0, row=0, columnspan=value_number+1)

    # プレーヤー
    for i in range(1, value_number+1):

        label_player = tk.Label(root_personal, text='player {}'.format(i))
        label_player.grid(column=i, row=1)




    # 性別
    label_sex = tk.Label(root_personal, text='性別')
    label_sex.grid(column=0, row=2)

    def select_cb_sex(event):

        for i in range(1, value_number+1):
            get_sex[i-1] = list_txt_sex[i-1].get()


    list_cb_sex = []
    list_txt_sex = []

    #　初期値設定
    global get_sex
    get_sex = []
    for i in range(1, value_number+1):
        get_sex.append('未選択')

    for i in range(1, value_number+1):

        list_cb_sex.append("cb" + str(i))
        list_txt_sex.append("txt" + str(i))

        list_txt_sex[i-1] = tk.StringVar()

        list_cb_sex[i-1] = ttk.Combobox(root_personal, textvariable = list_txt_sex[i-1], state = "readonly", width = 8)
        list_cb_sex[i-1].bind('<<ComboboxSelected>>', select_cb_sex)
        list_cb_sex[i-1]['values']=('未選択','男性','女性')
        list_cb_sex[i-1].set("未選択")
        list_cb_sex[i-1].grid(column=i, row=2)



    # 職業
    label_job = tk.Label(root_personal, text='職業')
    label_job.grid(column=0, row=3)

    def select_cb_job(event):

        for i in range(1, value_number+1):
            get_job[i-1] = list_txt_job[i-1].get()



    list_cb_job = []
    list_txt_job = []

    global get_job
    get_job = []
    for i in range(1, value_number+1):
        get_job.append('未選択')

    for i in range(1, value_number+1):

        list_cb_job.append("cb" + str(i))
        list_txt_job.append("txt" + str(i))

        list_txt_job[i-1] = tk.StringVar()

        list_cb_job[i-1] = ttk.Combobox(root_personal, textvariable = list_txt_job[i-1], state = "readonly", width = 8)
        list_cb_job[i-1].bind('<<ComboboxSelected>>', select_cb_job)
        list_cb_job[i-1]['values']=('未選択','会社員','学生','フリーター','ニート')
        list_cb_job[i-1].set("未選択")
        list_cb_job[i-1].grid(column=i, row=3)





    #　決定
    button_decision_personal = tk.Button(root_personal, text='決定', command=pushed_decision_personal)
    button_decision_personal.grid(column=0, row=4, columnspan=value_number+1, sticky=tk.N)

    button_back_number = tk.Button(root_personal, text='戻る', command=pushed_back_number)
    button_back_number.grid(column=0, row=5, columnspan=value_number+1)

    root_personal.mainloop()



#　割り勘金額
def pushed_back_personal():
    root_final.destroy()
    main_personal()

def pushed_back_top():
    root_final.destroy()
    main_start()

def main_final():

    # フレーム作成
    global root_final
    root_final = tk.Tk()
    root_final.title('アプリ')
    root_final.geometry('600x600')

    for i in range(0, value_number):
        root_final.columnconfigure(i, weight=1)

    for i in range(0, 6):
        root_final.rowconfigure(i, weight=1)

    # total_get, total 作成
    total_get = []
    total = 0
    for i in range(1, value_number+1):
        total_get.append(get_sex[i-1] + get_job[i-1])
        total += total_get[i-1]



    # プレーヤーごとの金額
    player_value = []
    pay = 0

    for i in range(1, value_number+1):

        print('player{}'.format(i))

        player_value.append((total_get[i-1]/total)*value_money)

        # 四捨五入
        player_value[i-1] = (round(player_value[i-1]/100))*100
        print('割り勘金額:{}'.format(player_value[i-1]))
        print('-------------')

        pay += player_value[i-1]

    print(pay)

    reduce = pay-value_money
    print('おつり={}'.format(reduce))



    # おつりがマイナスになったときの処理　ランダムで誰かに追加
    if reduce < 0:

        print('--おつりがマイナスになりました--')

        import random
        from math import ceil, fabs

        pay = 0
        # ランダム作成
        r = random.randrange(1, value_number+1)
        print('random_player={}'.format(r))

        for i in range(1, value_number+1):

            player_value.append((total_get[i-1]/total)*value_money)
            player_value[i-1] = (round(player_value[i-1]/100))*100



        #　ランダムで選択したプレーヤーにだけreduceを追加して10の位を切り上げ
        player_value[r-1] = player_value[r-1]+fabs(reduce)
        player_value[r-1] = (player_value[r-1])/100
        player_value[r-1] = ceil(player_value[r-1])
        player_value[r-1] = int(player_value[r-1]*100)


        for i in range(1, value_number+1):

            print('player{}'.format(i))
            print('割り勘金額:{}'.format(player_value[i-1]))
            print('-------------')

            pay += player_value[i-1]

        print(pay)

        reduce = pay-value_money
        print('おつり={}'.format(reduce))



    # 表示
    label_final = tk.Label(root_final, text='割り勘金額')
    label_final.grid(column=0, row=0, columnspan=value_number+1)


    for i in range(1, value_number+1):

        label_player = tk.Label(root_final, text='player{}'.format(i))
        label_player.grid(column=i-1, row=1)

        output = tk.Label(root_final, text=player_value[i-1])
        output.grid(column=i-1, row=2)

    value_money_label = tk.Label(root_final, text='金額は{}円です'.format(value_money))
    value_money_label.grid(column=0, row=3, columnspan=value_number+1)

    reduce_label = tk.Label(root_final, text='おつりは{}円です'.format(reduce))
    reduce_label.grid(column=0, row=4, columnspan=value_number+1)

    button_back_personal = tk.Button(root_final, text='戻る', command=pushed_back_personal)
    button_back_personal.grid(column=0, row=5)

    button_back_start = tk.Button(root_final, text='topに戻る', command=pushed_back_top)
    button_back_start.grid(column=value_number-1, row=5)



    root_final.mainloop()




# 起動
main_start()
