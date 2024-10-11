from tkinter import *
import mysql.connector
#reminder
from datetime import *
from pygame import mixer
import threading
def Start():
    log_out()
    global label
    label = Label(prj, text="Hello", bg="grey", fg="white")
    label.grid(row=0, column=1)
    global labels
    labels = Label(prj, text="-choose seconds (0-59s):", height=2, width=40, )
    labels.grid(row=1, column=2)
    global s
    s = Spinbox(prj, from_=0, to=59, width=18)
    s.grid(row=2, column=2)
    global labelm
    labelm = Label(prj, text="-choose minutes (0-59m):", height=2, width=40, )
    labelm.grid(row=1, column=1)
    global m
    m = Spinbox(prj, from_=0, to=59, width=18)
    m.grid(row=2, column=1)
    global labelh
    labelh = Label(prj, text="choose hours (0-3H):", height=2, width=40, )
    labelh.grid(row=1, column=0)
    global h
    h = Spinbox(prj, from_=0, to=3, width=18)
    h.grid(row=2, column=0)
    global  label3
    label3 = Label(prj, text=f"you choosed {h.get()}h{m.get()}m{s.get()}s")
    z = Label(prj, text="--Count Down--")
    global Start_but
    Start_but = Button(prj, text="Start", command=lambda: threading.Thread(target=countdown, args=(z,)).start())
    Start_but.grid(row=5, column=1)
def countdown(zer):
    label.grid_remove()
    Log_out.grid_remove()
    lab_e1.grid_remove()
    lab_e.grid_remove()
    labels.grid_remove()
    s.grid_remove()
    labelm.grid_remove()
    m.grid_remove()
    labelh.grid_remove()
    h.grid_remove()
    label3.grid(row=3, column=1)
    zer.grid(row=4, column=1)
    if int(s.get()) > 59:
        labelse = Label(prj, text="--choose between 0<s>59--")
        labelse.pack()
    if int(m.get()) > 59:
        labelme = Label(prj, text="--choose between 0<m>59--")
        labelme.pack()
    if int(h.get()) > 3:
        labelhe = Label(prj, text="--choose between 0<h>3--")
        labelhe.pack()
    label3.config(text=f"you choosed {h.get()}h{m.get()}m{s.get()}s ")
    Start_but.grid_remove()
    stpre_btn.grid(row=5,column=1)
    finish_time = (datetime.now() + timedelta(seconds=int(h.get()) * 3600 + int(m.get()) * 60 + int(s.get())))
    b = finish_time.strftime("%X %x")
    x = ''
    while super:
        a = datetime.now().strftime("%X %x")
        if int(str(finish_time - datetime.now()).split(':')[0]) >= 10:
            z = (
                f"{str(finish_time - datetime.now()).split(':')[0]}H : {str(finish_time - datetime.now()).split(':')[1]}M : {str(finish_time - datetime.now()).split(':')[2].split('.')[0]}S")
        if int(str(finish_time - datetime.now()).split(':')[0]) < 10:
            z = (
                f"0{str(finish_time - datetime.now()).split(':')[0]}H : {str(finish_time - datetime.now()).split(':')[1]}M : {str(finish_time - datetime.now()).split(':')[2].split('.')[0]}S")
        if str(finish_time - datetime.now()).split(':')[0] == "0":
            z = (
                f"{str(finish_time - datetime.now()).split(':')[1]}M : {str(finish_time - datetime.now()).split(':')[2].split('.')[0]}S")
        if int(str(finish_time - datetime.now()).split(':')[1]) == 0:
            z = (f"{str(finish_time - datetime.now()).split(':')[2].split('.')[0]}S")
        if a == b:
            if int(str(finish_time - datetime.now()).split(':')[0]) >= 0 and int(str(finish_time - datetime.now()).split(':')[1]) >= 0 and int(str(finish_time - datetime.now()).split(':')[2].split('.')[0])>=0:
                mixer.init()
                mixer.music.load('alarmSong.mp3')
                mixer.music.play(loops=100)
                Start_but.config(text="Restart", command=lambda: threading.Thread(target=restart, args=(zer,)).start())
                Start_but.grid(row=3,column=1)
                break
        else:
            if x != z:
                x = z
                zer.config(text=z)
    label3.grid_remove()
    zer.grid_remove()
def restart(ber):
    mixer.music.stop()
    countdown(ber)
def Stop_re():
    Start_but.grid_remove()
    mixer.init()
    mixer.music.stop()
    global super
    super = False
    Start()
    super = True
#login-sign------------------------------------------------------------------------------------
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydb"
)
mycursor =mydb.cursor()
def login():
    lab_s1.grid_remove()
    lab_e1.grid_remove()
    sign_e.grid_remove()
    lab_p1.grid_remove()
    sign_p.grid_remove()
    submit1.grid_remove()
    but_back.grid_remove()
    but_s1.grid_remove()
    c = login_e.get()
    d = login_p.get()
    sql = "SELECT * FROM users WHERE email = %s"
    adr = (c,)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    x=('','')
    if c != '' and d != '':
        for x in myresult:
            if x[0] == c and x[1] == d:
                global s
                global m
                global h
                global super
                s = IntVar()
                m = IntVar()
                h = IntVar()
                super = True
                Start()
                ps.grid_remove()
                em.grid_remove()
                lab_wi.grid_remove()
                lab_wp.grid_remove()
                lab.grid_remove()
                lab_e.grid_remove()
                login_e.grid_remove()
                lab_P.grid_remove()
                login_p.grid_remove()
                submit.grid_remove()
                but_g_e.grid_remove()
                lab_s.grid_remove()
                but_s.grid_remove()
                print("1")
            elif x[0] == c and x[1] != d:
                em.grid_remove()
                lab_wi.grid_remove()
                ps.grid_remove()
                lab_wp.grid(row=6,column=2)
                print("3")
        if x[0] != c:
            print(x[0])
            ps.grid_remove()
            em.grid_remove()
            lab_wp.grid_remove()
            lab_wi.grid(row=6, column=2)
            print("2")
    elif c == '':
        ps.grid_remove()
        lab_wp.grid_remove()
        lab_wi.grid_remove()
        em.grid(row=6,column=2)
        print("4")
    elif c != '' and d == '':
        lab_wp.grid_remove()
        lab_wi.grid_remove()
        em.grid_remove()
        ps.grid(row=6,column=2)
        print("5")
def deletel():
    login_p.delete(0, 'end')
    login_e.delete(0,'end')
def deletes():
    sign_p.delete(0, 'end')
    sign_e.delete(0,'end')
def log_out():
    lab_e.grid_remove()
    lab_e1.grid_remove()
    deletel()
    Log_out.grid(row=5,column=2)
def delete_press():
    label.grid_remove()
    labels.grid_remove()
    labelm.grid_remove()
    labelh.grid_remove()
    s.grid_remove()
    m.grid_remove()
    h.grid_remove()
    Start_but.grid_remove()
    stpre_btn.grid_remove()
    start_log()
def sign_up():
    lab_wi.grid_remove()
    lab_wp.grid_remove()
    lab.grid_remove()
    login_e.grid_remove()
    login_p.grid_remove()
    but_g_e.grid_remove()
    lab_s.grid_remove()
    but_s.grid_remove()
    submit.grid_remove()
    lab_e1.grid_remove()
    lab_e.grid_remove()
    lab_s1.grid(row=0, column=2)
    lab_e1.grid(row=1, column=2)
    sign_e.grid(row=2, column=2)
    lab_p1.grid(row=3, column=2)
    sign_p.grid(row=4, column=2)
    submit1.grid(row=4,column=3)
    but_back.grid(row=8,column=2)
    but_s1.grid(row=7, column=2)
def get_sign():
    a = sign_e.get()
    b = sign_p.get()
    z=True
    if a != '' and b != '':
        try:
            sql_e = "INSERT INTO users(email,password) VALUES(%s,%s)"
            val = (a, b)
            mycursor.execute(sql_e, val)
            mydb.commit()
            z = False
        except mysql.connector.errors.IntegrityError :
            labl_du.grid_remove()
            lab_khwae.grid_remove()
            lab_khwap.grid_remove()
            lab_khwa.grid_remove()
            labl_du.grid(row=9,column=2)
    if z==False:
        start_log()
    elif a=='' and b=='':
        labl_du.grid_remove()
        lab_khwae.grid_remove()
        lab_khwap.grid_remove()
        lab_khwa.grid(row=9,column=2)
    elif a=='':
        labl_du.grid_remove()
        lab_khwap.grid_remove()
        lab_khwa.grid_remove()
        lab_khwae.grid(row=9,column=2)
    elif b=='':
        labl_du.grid_remove()
        lab_khwae.grid_remove()
        lab_khwa.grid_remove()
        lab_khwap.grid(row=9,column=2)
    lab_s1.grid_remove()
def hide1():
    sign_p.config(show='*')
    submit1.config(text='Show password',command=show1)
def show1():
    sign_p.config(show='')
    submit1.config(text='Hide password',command=hide1)
def hide():
    login_p.config(show='*')
    submit.config(text='Show password',command=show)
def show():
    login_p.config(show='')
    submit.config(text='Hide password',command=hide)
def start_log():
    Log_out.grid_remove()
    but_back.grid_remove()
    lab_s1.grid_remove()
    lab_khwae.grid_remove()
    lab_khwap.grid_remove()
    lab_khwa.grid_remove()
    labl_du.grid_remove()
    lab.grid(row=0,column=2)
    lab_e.grid(row=1,column=2)
    login_e.grid(row=2,column=2)
    lab_P.grid(row=3,column=2)
    login_p.grid(row=4,column=2)
    submit.grid(row=4,column=3)
    but_g_e.grid(row=5,column=2)
    lab_s.grid(row=7,column=2)
    but_s.grid(row=8,column=2)
prj = Tk()
prj.geometry("900x400")
prj.title("WATER REMINDER 0.2")
global stpre_btn
stpre_btn=Button(prj,text="Stop", command=lambda: Stop_re())
#login
global lab_wp
lab_wp = Label(prj, text="wrong password")
global lab_wi
lab_wi = Label(prj, text="invalide informations.")
global em
em=Label(prj,text="please enter your email first.")
global ps
ps=Label(prj,text="please enter your password first.")
#log_out
global Log_out
Log_out = Button(prj,text="LOG-OUT",command=lambda: delete_press())
#sign
global submit1
submit1 = Button(prj, text='Show password', command=show1)
global lab_s1
lab_s1 = Label(prj,text="--SIGN-UP NOW--")
global sign_e
sign_e = Entry(prj, width=50)
global lab_e1
lab_e1 = Label(prj, text="-PLEASE ENTER YOUR E-MAIL:")
global sign_p
sign_p = Entry(prj, width=50,show='*')
lab_p1 = Label(prj, text="-PLEASE ENTER YOUR PASSWORD:")
global but_s1
but_s1 = Button(prj, text="SIGN-UP", command=lambda: get_sign())
global but_back
but_back = Button(prj, text="GO back", command=lambda:[start_log(),deletes()])
#getsign
global labl_du
labl_du = Label(prj,text="This email is already used,Enter another one.")
global lab_khwae
lab_khwae = Label(prj, text="please enter your email first.")
global lab_khwap
lab_khwap = Label(prj, text="please enter your password  first.")
global lab_khwa
lab_khwa = Label(prj, text="please enter your informations first.")
#start_log
global lab
lab = Label(prj, text="hello")
global lab_e
lab_e = Label(prj, text="-PLEASE ENTER YOUR E-MAIL:")
global lab_P
lab_P = Label(prj, text="-PLEASE ENTER YOUR PASSWORD:")
global submit
submit = Button(prj, text='Show password', command=show)
global but_g_e
but_g_e = Button(prj, text="ENTER",command=lambda: login())
global lab_s
lab_s = Label(prj, text="SIGN-UP?")
global but_s
but_s = Button(prj, text="SIGN-UP", command=lambda:[sign_up(),deletes()])
global login_e
login_e = Entry(prj, width=50)
global login_p
login_p = Entry(prj, width=50, show='*')

start_log()

prj.mainloop()