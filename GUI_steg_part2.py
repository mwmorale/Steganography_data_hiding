import tkinter as tk
from tkinter import *

from GUI_steg import embed
from GUI_steg import extract









def get_users_msg():
    wind = tk.Tk()
    wind.title("MESSAGE TO EMBED")
    greeting = tk.Label( text='Enter desired secret message that will be embedded within the image\n')
    greeting.pack()
    wind.geometry('800x400')
    wind['bg'] = '#26dddd'

    entry = Entry(wind, width=300)
    entry.pack(pady=0, padx=50)

    the_msg = []

    def get_message_from_user():
        #print( entry.get() )
        the_msg.append( entry.get() )
        wind.destroy()

    Button(
        wind,
        text="GO",
        fg='white',
        bg='black',
        padx=5,
        pady=5,
        command=get_message_from_user,
        ).pack()

    wind.mainloop()

    return the_msg[0]

















def get_pic_path():
    user_path = ''
    the_path = []

    wind1 = tk.Tk()
    wind1.title("Enter path to image")
    greeting = tk.Label( text='Below, please enter the path to the desired image like the following example:\n'+r"C:\Users\user\image"+'\n' )#, width=20)
    greeting.pack()
    wind1.geometry('420x105')

    entry = Entry(wind1, width=55)

    entry.pack(pady=0, padx=50)


    def do_destroy():
        wind1.destroy()


    def get_user_path_chars():
        the_path.append( entry.get() )
        do_destroy()


    Button(
        wind1,
        text="GO",
        fg='white',
        bg='black',
        padx=5,
        pady=5,
        command=get_user_path_chars,
        ).pack()


    wind1.mainloop()


    return the_path










# --- ENDING CONTROL PANEL CALLING OP FUNC'S ---

if( embed[0]==True and extract[0]==False ):
    the_msg = get_users_msg()

the_path = get_pic_path()


